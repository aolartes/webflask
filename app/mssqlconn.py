from sqlalchemy import create_engine
import pandas as pd

server = 'localhost'
database = 'DB_AOS'
driver = 'DBC Driver 17 for SQL Server'
database_con=f'mssql://@{server}/{database}?driver={driver}'

engine = create_engine(database_con)
con = engine.connect()

df = pd.read_sql_query("SELECT  * FROM dbo.todos order by todos",con)
print (df)

