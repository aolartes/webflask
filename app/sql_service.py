import pyodbc


class Connection:
    def connection():
        s = 'aolartes.database.windows.net'
        d = 'DB_AOS'
        u = 'aolartes'
        p = '123456aA!'
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

    print (get_users)