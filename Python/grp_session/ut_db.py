import unittest
import sqlite3
import db_connect

class MyTest(unittest.TestCase):
    def test_check(self):
        r = open("dept.csv",'r')
        lines = r.read()
        print("lines:\n", lines)
        conn = sqlite3.connect('C:\\Users\\mohan\\Desktop\\Virtual training\\upqk1.db')
        c = conn.cursor()
        op = db_connect.display()
        print("op:\n", op)
        self.assertEqual(lines,op)
        
if __name__ == '__main__':
    unittest.main()