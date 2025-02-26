from wtforms import Form, StringField, IntegerField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email

class UseForm(Form):
    matricula = StringField('Matricula', validators=[DataRequired()])
    edad = IntegerField("Edad")
    name = StringField('Nombre', validators=[DataRequired()])
    apellidos = StringField('Apellidos', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Enviar')
