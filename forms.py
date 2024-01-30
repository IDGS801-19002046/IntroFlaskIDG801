from wtforms import  Form 
from wtforms import StringField,IntegerField

from wtforms.validators import DataRequired, Email



class UserForm(Form):
    nombre=StringField('nombre')
    email=StringField('email')
    apaterno=StringField('apaterno')
    amaterno=StringField('amaterno')
    edad=IntegerField('edad')
    
    