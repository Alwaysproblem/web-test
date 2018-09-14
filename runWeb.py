from flask import Flask, render_template, url_for, flash, redirect
from form import PersonForm

import sys
import sqlite3
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

# keys = [
#     "UserEmail", 
#     "HouseID", 
#     "RoomNo",
#     "Street",
#     "Suburb",
#     "State",
#     "Postcode",
#     "RoomType",
#     "Star",
#     "CheckIn",
#     "CheckOut",
#     "Price"
#     ]

# info_tuples = (
#     "regan@gmail.com",
#     '8b4e8226-dd15-46a4-80af-e14a995a38d3',
#     "unit 1704",
#     "39 Rhodes",
#     "Hillsdale",
#     "NSW",
#     "2036",
#     "double",
#     "5",
#     "12/2/2018",
#     "12/12/2018",
#     780
# )


# def address_for(Rooms, Streets, Suburb, State, Postcode):
#     """
#     forming the real address.
#     """
#     return Rooms + '/' + ' ' + Streets + 'st' + " " + Suburb + \
#             ' ' + State + ' '+ Postcode

def tupletodict(keys, tup):
    return dict(zip(keys, tup))

def comd_gen(Pform):
    cmd = None
    UserEmail = Pform.UserEmail.data
    HouseID = str(uuid.uuid4())
    Rooms = Pform.Room.data.strip()
    Streets = Pform.Street.data.strip()
    Suburb = Pform.Suburb.data.strip()
    State = Pform.State.data.strip()
    Postcode = Pform.Postcode.data.strip()
    RoomType = Pform.RoomType.data
    Star = Pform.Star.data
    CheckIn = Pform.check_in_date.data
    CheckOut = Pform.check_out_date.data
    Price = Pform.Price.data

    cmd = f"""INSERT INTO hotel VALUES (
                    "{UserEmail}",
                    "{HouseID}",
                    "{Rooms}",
                    "{Streets}",
                    "{Suburb}",
                    "{State}",
                    "{Postcode}",
                    "{RoomType}",
                    "{Star}",
                    "{CheckIn}",
                    "{CheckOut}",
                    "{Price}"
                )"""
    return cmd

@app.route("/")
@app.route("/show")
def show():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()
    keys = [
        "UserEmail", 
        "HouseID", 
        "RoomNo",
        "Street",
        "Suburb",
        "State",
        "Postcode",
        "RoomType",
        "Star",
        "CheckIn",
        "CheckOut",
        "Price"
        ]
    info_tuples = cur.execute("""SELECT * FROM hotel;""")
    posts = [tupletodict(keys, tup) for tup in info_tuples]

    # posts=[tupletodict(keys,info_tuples)] ## just for test.
    
    # print(posts)
    conn.close()
    return render_template('show.html', posts=posts)


@app.route("/add", methods=['GET', "POST"])
def add():
    AcForm = PersonForm()
    if AcForm.validate_on_submit():
        cmd_db = comd_gen(AcForm)
        conn = sqlite3.connect("info.db")
        cur = conn.cursor()
        with conn:
            cur.execute(cmd_db)
        conn.close()
        flash("the information is added", "success")
        return redirect(url_for('show'))
    return render_template('add.html', title='Add', form = AcForm)


if __name__ == '__main__':
    conn = sqlite3.connect('info.db', detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread = False)
    with conn:
        conn.execute("""create table if not exists hotel (
                        useremail char(50),
                        HouseID char(50) not null,
                        RoomNo char(50),
                        Street char(50),
                        Suburb char(50),
                        State char(50),
                        Postcode char(50),
                        RoomType char(50),
                        Star char(50),
                        check_in_date char(50),
                        check_out_date char(50),
                        price int(50));
                        """)
    conn.close()
    app.run(debug = True, port=37722)
