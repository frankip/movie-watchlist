from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, BooleanField, ValidationError, validators
from wtforms.validators import Required,Email,EqualTo
from wtforms.fields.html5 import EmailField

from ..models import User


class RegistrationForm(FlaskForm):
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    username = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')


    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')
    
    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            user  = User.query.all()
            print('all users',user)
            uname = User.query.filter_by(username = data_field.data)
            print('request',uname)
            raise ValidationError('That username is taken')


class LoginForm(FlaskForm):
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')