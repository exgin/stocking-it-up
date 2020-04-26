from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Length


class RegisterForm(FlaskForm):
    """Form for registering a user"""

    username = StringField("Username", validators=[InputRequired(), Length(min=1, max=30)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=6)])

class LoginForm(FlaskForm):
    """Form for registering a user"""

    username = StringField("Username", validators=[InputRequired(), Length(max=20)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=6)])