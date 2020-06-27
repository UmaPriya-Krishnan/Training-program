import unittest
import sqlite3
import sys
sys.path.append("C:\\Users\\mohan\\Desktop\\db_base\\src")
import connect_file
import student_table
from student_table import DbConnect

class MyTest(unittest.TestCase):
    def test_check(self):
        
        cr = connection.cursor
        with open('C:\\Users\\mohan\\Desktop\\db_base\\src\\student.csv','r') as e:
            lines = e.read()
        op = s.display()
        self.assertEqual(lines,op)
    def test_connection(self):
        conn = s.connect()
        self.assertNotEqual((conn,conn),("False,False"))
if __name__ == '__main__':
    connection, cursor = connect_file.cn()
    s = DbConnect(connection,cursor)
    unittest.main()
    