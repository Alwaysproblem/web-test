from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, SelectField, DateField
from wtforms.validators import DataRequired, email

class PersonForm(FlaskForm):
    UserEmail = StringField(
            "UserEmail", 
            validators = [
                DataRequired(), 
                email(message="please imput an email address not a joke.")
            ])
    HouseID = StringField("HouseID")
    Room = StringField("Room Number", validators=[DataRequired()])
    Street = StringField("Street", validators=[DataRequired()])
    Suburb = StringField("Suburb", validators=[DataRequired()])
    State = StringField("State", validators=[DataRequired()])
    Postcode = StringField("Postcode", validators=[DataRequired()])
    RoomType = SelectField("Room Type", validators=[DataRequired()])
    Star = SelectField(
                "Star Ratings", 
                validators=[DataRequired()],
                choices=[
                    ('1', '1'),
                    ('2', '2'),
                    ('3', '3'),
                    ('4', '4'),
                    ('5', '5')
                ])
    check_in_date = DateField(
                "CheckIn Date(DD/MM/YY)", 
                validators=[DataRequired()],
                format='%D/%m/%Y')
    check_out_date = DateField(
                "CheckOut Date(DD/MM/YY)", 
                validators=[DataRequired()],
                format='%D/%m/%Y')
    Price = IntegerField("Renting Price per week", validators=[DataRequired()])

    # Name = StringField("Name", validators=[DataRequired()])
    # Male = BooleanField("Male")
    # Female = BooleanField("Female")
    # Weight = StringField("Weight", validators=[DataRequired()])
    # Credits = SelectField(
    #     "Credits", 
    #     choices=[("PS", "50"), ("CR", "65"), ("D", "75"), ("HD", "85")])
    # submit = SubmitField("Submit")

