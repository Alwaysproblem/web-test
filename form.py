from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, email

class PersonForm(FlaskForm):
    UserEmail = StringField(
            "UserEmail", 
            validators = [DataRequired(), email(message="please imput an email address not a joke.")])
    HouseID = StringField("HouseID")
    Room = StringField("Room", validators=[DataRequired()])
    Street = StringField("Street",)
    # Name = StringField("Name", validators=[DataRequired()])
    # Male = BooleanField("Male")
    # Female = BooleanField("Female")
    # Weight = StringField("Weight", validators=[DataRequired()])
    # Credits = SelectField(
    #     "Credits", 
    #     choices=[("PS", "50"), ("CR", "65"), ("D", "75"), ("HD", "85")])
    # submit = SubmitField("Submit")

