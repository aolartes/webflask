from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators =[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Login')

class TodoForm (FlaskForm):
    description = StringField('Descripcion',validators=[DataRequired()])
    submit = SubmitField('crear')

class DeleteTodoForm(FlaskForm):
    submit = SubmitField('Borrar')

class UpdateTodoForm(FlaskForm):
    submit = SubmitField('Actualizar')

class MyForm(FlaskForm):
    checkbox = BooleanField('Seleccionar elementos')
    submit = SubmitField('Eliminar')