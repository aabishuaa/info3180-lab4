from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed  

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    file = FileField('Upload File', validators=[
        InputRequired(),
        FileAllowed(['jpg', 'jpeg', 'png'], 'Only .jpg, .jpeg, and .png files are allowed.')  # <-- Updated extensions
    ])