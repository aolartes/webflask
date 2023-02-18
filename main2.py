from app.models import UserData,UserModel
from app.sql_service2 import Connection
from werkzeug.security import generate_password_hash
import os
from dotenv import load_dotenv
load_dotenv()


def get_todos(connection=Connection.connection,user_id = 'colartes'):
    todos=[]
    idtodos=[]     
    query = connection().execute(f"select * from  todos t inner join client c on c.idclient = t.idclient where [user_name] = '{user_id}';")
    for row in query.fetchall():
        #return(str(row.idclient))
        todos.append({  "idtodos"   : str(row[0]),
                        "idclient"  : str(row[1]),
                        "todos"     : str(row[2]),
                        "done"      : row[3]
                        })
        # for todo in todos:
        #     valor = todo.get("todos")
        #     if valor:
        #         idtodos.append(valor)
    return todos
print(get_todos())
for result in get_todos():
    print(result['todos'],result['done'])

valor = True
print (not valor)

def signup():
    username = 'aolartes1'
    password = 'Skr4v3n4$!'
    user_doc = Connection.get_userc(connection=Connection.connection,user_id=username)#Connection.get_userc(connection=Connection.connection,user_id='username')
    if user_doc is None:
        password_hash = generate_password_hash(password)
        user_data = UserData(username,password_hash)
        print(user_data.username)
        print(user_data.password)
        #Connection.user_put(user_data,Connection.connection)
    else:
        password_hash = generate_password_hash('metal123')#generate_password_hash((user_doc[0])['password'])
        user_data = UserData(username,password_hash)
        print('Existe')
        #print(user_data.password)

signup()


valor = Connection.get_todos(Connection.connection,user_id='aolartes')

print (valor)

#Connection.update_todo(Connection.connection,todo_id=163,done=1)

data_base = os.getenv('data_base')

print(data_base)


# def pruebita():
#     conn=Connection.connection()
#     lista=[]
#     consulta = "select top 2 * from todos;"
#     result = conn.execute(consulta)
#     for row in result.fetchall():
#         lista.append(
#             {
#                 "idtodos"   : row[0],
#                 "idclient"  : row[1],
#                 "todos"     : row[2],
#                 "done"      : row[3],
#             }
#         )

#     return lista
#     # for dictio in lista:
#     #     devuelve = (dictio)
#     #     return (devuelve)

# print(pruebita())
# for result in pruebita():
#     print(result['todos'])


# def get_todos(connection=Connection.connection,user_id = 'colartes'):
#     todos=[]
#     idtodos=[]     
#     query = connection().execute(f"select * from  todos t inner join client c on c.idclient = t.idclient where [user_name] = '{user_id}';")
#     for row in query.fetchall():
#         #return(str(row.idclient))
#         todos.append({  "idtodos"   : str(row[0]),
#                         "idclient"  : str(row[1]),
#                         "todos"     : str(row[2]),
#                         "done"      : row[3]
#                         })
#     for todo in todos:
#         valor = todo.get("todos")
#         if valor:
#             idtodos.append(valor)
#     return idtodos

#print(get_todos())




# print('😈')
# print('alvaro olarte'.title())










# print (consulta)
# consult=[]
# query = conn.execute("SELECT  * FROM dbo.pruebas")
# for row in query:
#     consult.append({
#                     "campo1": str(row[0]),
#                     "campo2": str(row[1])
#                     })
# print (consult)


# conn.commit()
#conn.close()





    # query = connection().execute("select * from  todos")
    # for row in query.fetchall():
    #         print(row)
    



# def retorno_tupla():
#     tupla = ('aols','15263d')
#     print(tupla.)


# retorno_tupla()


# user = ''

# if (users[0]) == None:
#     user = None
# else:
#     for item in users:
#         user = (item['user_name'])
# print (user)





#print (users[0]['password'])
#print(((users[0])['user_name']))


#print((users[0])['password'])

# password = users[0].get('password',None)
# print (password)




#password = users.get('password')
#password=users.to_dict()['password']
# print (password)