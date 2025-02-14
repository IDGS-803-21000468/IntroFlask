from wtforms import Form, StringField, validators
from flask import Flask,redirect,url_for,render_template,request
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError
from wtforms import Form, StringField, validators, IntegerField, SubmitField,BooleanField, SelectField, TextAreaField, EmailField

class UseForm(Form):
    matricula = StringField('Matricula', validators=[DataRequired()])
    edad = IntegerField("Edad")
    name = StringField('Name', validators=[DataRequired()])
    apellidos = StringField('Apellidos', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')