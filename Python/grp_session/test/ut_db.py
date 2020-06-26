import unittest
import sqlite3
import sys
sys.path.append("C:\\Users\\mohan\\Desktop\\db_base\\src")
import estab_conn
import db_connect
from db_connect import DbConnect
#sys.path.append("C:\\Users\\mohan\\Desktop\\db_base\\src")

class MyTest(unittest.TestCase):
    def test_check(self):
        
        cr = connection.cursor
        with open("C:\\Users\\mohan\\Desktop\\Virtual training\\class-db\\dept.csv",'r') as e:
            lines = e.read()
        
        op = s.display()
        self.assertEqual(lines,op)
    def test_connection(self):
        conn = s.connect()
        self.assertNotEqual((conn,conn),("False,False"))
if __name__ == '__main__':
    connection, cursor = estab_conn.cn()
    s = DbConnect(connection,cursor)
    unittest.main()
    