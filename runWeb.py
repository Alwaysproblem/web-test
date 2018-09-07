from flask import Flask, render_template, url_for, flash, redirect
from form import PersonForm

import sys
import sqlite3
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


def tupletodict(keys, tup):
    return dict(zip(keys, tup))

def comd_gen(Pform):
    if Pform.Male.data is True:
        cmd = f"INSERT INTO info VALUES (\"{Pform.Name.data}\", \"Male\", \"{Pform.Weight.data}kg\")"
    elif Pform.Female.data is True:
        cmd = f"INSERT INTO info VALUES (\"{Pform.Name.data}\", \"Female\", \"{Pform.Weight.data}kg\")"
    # cmd = f"INSERT INTO info VALUES (\"{Pform.Name.data}\", \"Female\", \"{Pform.Weight.data}kg\")"
    return cmd

@app.route("/")
@app.route("/show")
def show():
    conn = sqlite3.connect("info.db")
    cur = conn.cursor()
    keys = ["Name", "Gender", "Weight"]
    info_tuples = cur.execute("""SELECT * FROM info;""")
    posts = [tupletodict(keys, tup) for tup in info_tuples]
    print(posts)
    conn.close()
    return render_template('show.html', posts=posts)


@app.route("/add", methods=['GET', "POST"])
def add():
    AcForm = PersonForm()
    if AcForm.validate_on_submit():

        print(f"the Credits is {AcForm.Credits.data}")

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
        conn.execute("""CREATE TABLE IF NOT EXISTS Info (
                    Name    varchar(20),
                    Gender  varchar(20),
                    Weight   varchar(20)
                )""")
        # conn.execute("""create table hotel (
        #                 ID int primary key not null,
        #                 hotelid char(50) not null,
        #                 usermail char(50),
        #                 hotel char(50),
        #                 hotel_suburb char(50),
        #                 check_in_date char(50),
        #                 check_out_date char(50),
        #                 hotel_class char(50),
        #                 room_type char(50),
        #                 price int(50));
        #                 """)
    conn.close()
    app.run(debug = True, port=37722)
