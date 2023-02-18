import pyodbc
import os
from dotenv import load_dotenv
load_dotenv()



class Connection:
    def connection():
        s = os.getenv('s')
        d = os.getenv('d')
        u = os.getenv('u')
        p = os.getenv('p')
        cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+s+';DATABASE='+d+';UID='+u+';PWD='+ p
        conn = pyodbc.connect(cstr)
        cursor = conn.cursor()
        return cursor
    


    
    def get_usersc(connection):
        user_name=[]
        iduser=[]     
        query = connection().execute("SELECT  user_name FROM dbo.client")
        for row in query.fetchall():
            #return(str(row.idclient))
            user_name.append({  "idclient"   : str(row[0])
                            })
        for idclient in user_name:
            valor = idclient.get("idclient")
            if valor:
                iduser.append(valor)
        return iduser
    
    get_users = get_usersc(connection)

    def get_userc(connection,user_id):
        user=[]
        iduser=[]     
        query = connection().execute(f"select c.user_name,p.password from client c inner join passwd p on p.idclient = c.idclient where c.[user_name] = '{user_id}';")
        for row in query.fetchall():
            #return(str(row.idclient))
            user.append({  "user_name"   : str(row[0]),
                            "password"  : str(row[1])
                            })
        #return user
        if not user:#(user[0]) == None:
            users = None
        else:
            for item in user:
                users =user
        return users        

        # if not user:
        #     value = [None]
        # else:
        #     value = user
        # return value

    def user_put(user_data,connection):
        conn = connection()
        username = (user_data.username)
        password = (user_data.password)
        querycli = f"insert into client ([user_name]) VALUES ('{username}');"
        querypass = f"insert into passwd ([password],idclient) values ('{password}',(select max(idclient) from client));"
        conn.execute(querycli)
        conn.execute(querypass)
        conn.commit()
    

    def get_todos(connection,user_id):
        todos=[]
        #idtodos=[]     
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
        #return idtodos
        return todos

    # def get_done(connection,user_id):
    #     done=[]
    #     iddone=[]     
    #     query = connection().execute(f"select * from  todos t inner join client c on c.idclient = t.idclient where [user_name] = '{user_id}';")
    #     for row in query.fetchall():
    #         #return(str(row.idclient))
    #         done.append({  "idtodos"   : str(row[0]),
    #                         "idclient"  : str(row[1]),
    #                         "todos"     : str(row[2]),
    #                         "done"      : str(row[3]),
    #                         })
    #     for todo in done:
    #         valor = todo.get("done")
    #         if valor:
    #             iddone.append(valor)
    #     return iddone

    def put_todo(user_id,description,connection):
        conn = connection()
        username = user_id
        description = description.replace("'","''")
        querytodo = f"insert into todos (idclient,todos,done) values ((select idclient from client where user_name = '{username}'),N'{description}',0);"
        conn.execute(querytodo)
        conn.commit()

    def delete_todo(connection,todo_id):
        conn = connection()
        querydelete = f"delete from todos where idtodos in ({todo_id});"
        conn.execute(querydelete)
        conn.commit()
    
    def update_todo(connection,todo_id):
        conn = connection()
        query_update = f"update todos set done = CASE WHEN done = 1 THEN 0 ELSE 1 END  where idtodos = {todo_id};"
        conn.execute(query_update)
        conn.commit()
    

    def _get_todo_ref(connection,user_id,todo_id):
        conn = connection()
        query = f"select * from client c inner join todos t on t.idclient = c.idclient where c.user_name = {user_id} and t.idtodos =167"




    def _get_todo_ref(connection,user_id,todo_id):
        conn = connection()
        query_todo_ref=f"select idtodos from todos where "
    
                


    

    
    
    #for user in get_users(connection):
    #    print(user)
        
    



        


    # consulta = connection().execute('SELECT * FROM dbo.client')


    # for fila in consulta.fetchall():
    #     print(fila.user_name)
    
    
    
    
    

    

    

