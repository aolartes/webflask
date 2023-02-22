from app import create_app
import unittest
from flask import request,make_response,redirect, render_template,session,url_for,flash
from flask_login import login_required,current_user
#from app.sql_service import Connection
from app.sql_service2 import Connection
from app.forms import TodoForm, DeleteTodoForm,UpdateTodoForm

app = create_app()


#todos = Connection.get_todos(connection=Connection.connection,user_id='usernme')


# class PrintSql:
#     def __init__(self):
#         self.objeto_a = Connection()
#     def usar_valor(self):
#         val=self.objeto_a.obten_valor()      
#         valores = []
#         llave_buscar = "todos"
#         for diccionario in val:
#             valor = diccionario.get(llave_buscar)
#             if valor:
#                 valores.append(valor)
#         return valores

# b = PrintSql()
# todos = b.usar_valor()

#todos = ['Comprar Café','Enviar solicitud de Compra','Entregar video al productor']



@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)




@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',error=error)

@app.errorhandler(500)
def not_found(error):
    return render_template('500.html',error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session ['user_ip'] = user_ip
    #response.set_cookie('user_ip',user_ip)
    
    return response
    

@app.route('/hello', methods=['GET','POST'])
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.id #session.get('username')
    todo_form=TodoForm()
    delete_form=DeleteTodoForm()
    update_form = UpdateTodoForm()    
    todos=Connection.get_todos(connection=Connection.connection,user_id=username)
    context={
        'user_ip': user_ip,
        'todos': Connection.get_todos(connection=Connection.connection,user_id=username),
        #'dones': Connection.get_done(connection=Connection.connection,user_id=username),
        'username':username,
        'todo_form':todo_form,
        'delete_form':delete_form,
        'update_form': update_form,        
    }

    if todo_form.validate_on_submit():
        Connection.put_todo(user_id =username,description=todo_form.description.data,connection=Connection.connection)
        flash('Tu tarea se creo con éxito')
        
        return redirect(url_for('hello'))


    return render_template('hello.html',**context)

@app.route('/todos/delete/<todo_id>',methods=['POST'])
def delete(todo_id):
    user_id = current_user.id
    Connection.delete_todo(connection=Connection.connection,todo_id=todo_id)
    flash('Tu tarea se elimino con éxito')
    return redirect(url_for('hello'))

@app.route('/todos/update/<todo_id>/<int:done>',methods=['POST'])
def update(todo_id,done):
    user_id = current_user.id
    Connection.update_todo(Connection.connection,todo_id=todo_id)
    flash('Tu tarea se ha actualizado con éxito')
    return redirect(url_for('hello'))



"""iniciar con video 34: Editar tareas"""