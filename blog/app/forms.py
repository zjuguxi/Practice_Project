from flask_wtf import Form
from wtforms import TexrField, BooleanField, PasswordField
from wtforms.validators import Required

class LoginForm(Form):
    name = TextField('Name', validators = [Required()])
    password = PasswordField('password', validators = [Required()])
    remember_me = BooleanField('Remember_me', default = False)

