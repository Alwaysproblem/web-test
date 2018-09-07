from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired

class PersonForm(FlaskForm):
    Name = StringField("Name", validators=[DataRequired()])
    Male = BooleanField("Male")
    Female = BooleanField("Female")
    Weight = StringField("Weight", validators=[DataRequired()])
    Credits = SelectField(
        "Credits", 
        choices=[("PS", "50"), ("CR", "65"), ("D", "75"), ("HD", "85")])
    submit = SubmitField("Submit")

