from wtforms import Form
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms import validators 

class Formulario(Form):
	cedula= IntegerField('cedula')
	nombre= StringField('nombre')
	apellido= StringField('apellido')
	telefono= StringField('telefono')
	direccion= TextAreaField('direccion')
	submit= SubmitField("Enviar")

class Login(Form):
	nombre= StringField('nombre')
	cedula= IntegerField('cedula')
	submit= SubmitField("enviar")

	
