from django.shortcuts import render
from django.db import connection
#from embl.models import Embl
import psycopg2

# try:
connection = psycopg2.connect(user="postgres",password="12345",host="localhost",port="5432",database="embl")
print("Database opened successfully")

cur = connection.cursor()
# connection.commit()
# cur.execute('SELECT count(*) from "MyData" WHERE neighborhood = 57') 
# cur.execute('SELECT count(*) from "MyData" WHERE protein1 like %ENSP00000222008 ''') 
# cur.execute("""SELECT count(*) FROM "MyData" where protein2 like '%ENSP00000222008'""")
# cur.execute('SELECT count(*) FROM "MyData" where protein2 LIKE %(ENSP00000222008)s')
cur.execute('SELECT * FROM "MyData" WHERE protein2 = "%9606.ENSP00000222008%"')



    # WHERE protein1 like '%ENSP00000222008%'")
record = cur.fetchall()
print(record, "data")

connection.close()