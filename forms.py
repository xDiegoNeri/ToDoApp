from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, BooleanField, FileField
from wtforms.validators import DataRequired, Length, Optional

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), Length(max=150)
    ])
    password = PasswordField('Password', validators=[DataRequired()])

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), Length(max=150)
    ])
    password = PasswordField('Password', validators=[DataRequired()])

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[
        DataRequired(), Length(max=100)
    ])
    description = TextAreaField('Description', validators=[Optional()])
    priority = SelectField('Priority', choices=[
        (1, 'Baja'), (2, 'Media'), (3, 'Alta'), (4, 'Me urge 💀')
    ], coerce=int)
    is_complete = BooleanField('Complete')
    image = FileField('Attach Image')


