from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, InputRequired, Length

class SignupForm(FlaskForm):
  first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
  last_name = StringField('Last name', validators=[DataRequired("Please enter your last name")])
  email = StringField('Email', validators=[DataRequired("An email address is required. "), Email("Please enter your email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password"), Length(min=6, message="Password must be 6 characters or more.")])
  submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email('Please enter your email address.')])
    password = PasswordField('Password', validators=[DataRequired("Please enter your password.")])
    submit = SubmitField("Sign in")
class AddressForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired("Please enter an address")])
    submit = SubmitField("Search")

class PetProfileForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
    last_name = StringField('Last name', validators=[DataRequired("Please enter your last name")])
    email = StringField('Email', validators=[DataRequired("An email address is required. "), Email("Please enter your email address.")])

    dropOffDate = DateField('Drop Off Date', format='%Y-%m-%d')
    dropOffTime = StringField('Drop Off Time', validators=[DataRequired("Please enter drop off time.")])
    # first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
    # first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
    # first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
    # first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])

    submit = SubmitField("Submit")
