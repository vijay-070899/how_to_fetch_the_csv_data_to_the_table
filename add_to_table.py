import pandas as pd
import mysql.connector
from mysql.connector import Error
empdata = pd.read_csv('vijay.csv', index_col=False, delimiter = ',')
empdata.head()
try:

    con_obj=mysql.connector.connect(host='localhost',user='root',password='root')
    cur_obj=con_obj.cursor()
    cur_obj.execute('create table vijay.freinds(name varchar(20),country varchar(20),age int,gender varchar(20))')
    print('table is crated')
    for i,row in empdata.iterrows():
        sql="insert into vijay.freinds values (%s,%s,%s,%s)"
        cur_obj.execute(sql,tuple(row))
        print('record inserted')
        con_obj.commit()
except Error as e:
    print("Error while connecting to MySQL", e)

