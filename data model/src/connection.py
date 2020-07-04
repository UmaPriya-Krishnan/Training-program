import mysql.connector
import sys
sys.path.append(r'C:\Users\mohan\Desktop\py_sql\config\config.properties')
import configdetails


def con():
    host, user, pwd, db = configdetails.conpar()
    mydb = mysql.connector.connect(host=host, user=user, password=pwd, database=db)
    #print(mydb.is_connected())
    return mydb
#con()