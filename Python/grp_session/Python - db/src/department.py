import sqlite3
import connect_file
from log_file import lgg 

class DbConnect():
    
    def __init__(self,connection,cr):
        try:
            self.connection = connection
            self.cursor = connection.cursor() 
        except sqlite3.Error as errror:
            log_info = lgg.logger()
            log_info.info(error)
    def connect(self):
        try:
            return connection, cursor
        except sqlite3.Error as error:
            log_info = lgg.logger()
            log_info.info(error)
            return False, False
            
    def create_table(self):  
        try: 
            create_query = "CREATE TABLE IF NOT EXISTS DEPARTMENT (Dep_id VARCHAR(9) PRIMARY KEY, Dep_name CHAR(30))"
            self.cursor.execute(create_query)
            self.cursor.execute('delete from department')
            msg = lgg.logger()
            msg.info('Department table has been created successfully')
        except sqlite3.Error as error:
            log_info = lgg.logger()
            log_info.info(error)
            
    def data_entry(self):
        try:        
            filename = 'C:\\Users\\mohan\\Desktop\\db_base\\src\\department.csv'
            with open(filename,'r') as fr:
                for line in fr.readlines():
                    col_value = line.replace('\n','').split(',')
                    insert_query = "INSERT INTO DEPARTMENT (Dep_id, Dep_name)VALUES('{}', '{}')" .format(col_value[0],col_value[1])
                    self.cursor.execute(insert_query)
            connection.commit()
            msg = lgg.logger()
            msg.info('Values are inserted into department table successfully')
        except sqlite3.Error as error:
            log_info = lgg.logger()
            log_info.info(error)
            print(error)

    def display(self):
        try:
            result = ''
            value = self.cursor.execute("SELECT * FROM DEPARTMENT")
            for row in value:
                p = [str(i) for i in row]
                sep = ','.join(p)
                result = result+sep+'\n'
            msg = lgg.logger()
            msg.info('Selected Values are fetched from the department table')
            return result
            self.cursor.close        
        except sqlite3.Error as error:
            log_info = lgg.logger()
            log_info.info(error)
            print(error)

            
connection, cursor = connect_file.cn()
sql = DbConnect(connection, cursor)
sql.create_table()
sql.data_entry()
sql.display()
sql.connect()