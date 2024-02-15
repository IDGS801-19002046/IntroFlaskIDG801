from wtforms import Form
from wtforms import StringField, TelField, IntegerField

from wtforms import EmailField
from wtforms.validators import DataRequired, Email

class UserForm(Form):
    nombre = StringField('nombre', [
        validators.DataRequired(message='El campo es obligatorio'),
        validators.Length(min=4, max=10, message='Ingresa un nombre válido')
    ])
    email = StringField('email', [
        validators.DataRequired(message='El campo es obligatorio'),
        validators.Email(message='Ingresa un email válido')
    ])
    apaterno = StringField('apaterno', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=4, max=30, message='Ingresa un apellido válido')
    ])
    amaterno = StringField('amaterno', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=4, max=10, message='Ingresa un apellido válido')
    ])
    edad = IntegerField('edad', [
        validators.DataRequired(message='El campo es requerido'),
        validators.NumberRange(min=1, max=5, message='Ingresa una edad válida')
    ])