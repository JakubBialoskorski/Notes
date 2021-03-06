from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SubmitField, SelectMultipleField, HiddenField
from flask_pagedown.fields import PageDownField
from wtforms import validators

class LoginForm(FlaskForm):
    username = TextField('Username*', [validators.Required("Please enter your name.")])
    password = PasswordField('Password*', [validators.Required("Please enter your password.")])
    submit = SubmitField('Login')

class SignUpForm(FlaskForm):
    username = TextField('Username*', [validators.Required("Please enter your username")])
    email = TextField('Email*', [validators.Required("Please enter your email"), validators.Email('Email format incorrect')])
    password = PasswordField('Password*', [validators.Required("Please enter your password"), validators.EqualTo('confirm_password', message='Passwords must match'), validators.Length(min=8, max=32, message='Password must contain 8 digits minimum, with 32 being maximum')])
    confirm_password = PasswordField('Confirm your password*', [validators.Required("Confirm your password")])
    submit = SubmitField('Signup')

class AddNoteForm(FlaskForm):
    note_id = HiddenField("Note ID:")
    note_title = TextField('Note Title:', [validators.Required("Please enter a note title.")])
    note = PageDownField('Your Note:')
    tags = SelectMultipleField('Note Tags:')
    submit = SubmitField('Add Note')

class AddTagForm(FlaskForm):
    tag = TextField('Enter tag:', [validators.Required("Please enter the tag")])
    submit = SubmitField('Add Tag')

class ChangeEmailForm(FlaskForm):
    email = TextField('Email*', [validators.Required("Please enter our email"), validators.Email('Email format incorrect')])
    submit = SubmitField('Update Email')

class ChangePasswordForm(FlaskForm):
    password = PasswordField('Set new password*', [validators.Required("Please enter your password"), validators.EqualTo('confirm_password', message='Passwords must match'), validators.Length(min=8, max=32, message='Password must contain 8 digits minimum, with 32 being maximum')])
    confirm_password = PasswordField('Confirm new password*', [validators.Required("Confirm your password")])
    submit = SubmitField('Update Password')
