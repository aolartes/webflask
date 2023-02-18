import pyodbc 



s = 'localhost'
d = 'DB_AOS'
u = 'sa'
p = '123456aA!'
cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+s+';DATABASE='+d+';UID='+u+';PWD='+ p
conn = pyodbc.connect(cstr)

cursor = conn.cursor()

cursor.execute('SELECT * FROM dbo.client')


for fila in cursor.fetchall():
  print(fila.user_name)