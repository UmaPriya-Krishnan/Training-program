import sqlite3
import estab_conn
from lg import lgg 

class DbConnect():
    
    def __init__(self,connection,cr):
        try:
            self.connection = connection
            self.cursor = connection.cursor() 
            #return self.connection, self.cursor
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
            create_query = "CREATE TABLE IF NOT EXISTS DEPT (dep_id text primary key, dep_name text, dep_manager text)"
            self.cursor.execute(create_query)
            #self.cursor.execute('delete from dept')
            msg = lgg.logger()
            msg.info('Tables are created as expected')
            #connection.commit()
        except sqlite3.Error as error:
            log_info = lgg.logger()
            log_info.info(error)
            

    def data_entry(self):
        try:        
            filename = 'C:\\Users\\mohan\\Desktop\\Virtual training\\rand\\dept.csv'
            with open(filename,'r') as fr:
                for line in fr.readlines():
                    col_value = line.replace('\n','').split(',')
                    insert_query = "INSERT INTO DEPT (dep_id, dep_name, dep_manager) VALUES('{}','{}','{}')" .format(col_value[0],col_value[1],col_value[2])
                    self.cursor.execute(insert_query)
            connection.commit()
            msg = lgg.logger()
            msg.info('Values are inserted ')
        except sqlite3.Error as error:
            log_info = lgg.logger()
            log_info.info(error)
    
    def display(self):
        try:
            result = ''
            value = self.cursor.execute("SELECT * FROM dept")
            for i in value:
#if values in the table are of int, use [str(i) for i in value and then join the values with comma delimiter
                sep = ','.join(i)
                result = result+sep +'\n'
            return result
            msg = lgg.logger()
            msg.info('Selected Values are fetched')
            self.cursor.close        
        except sqlite3.Error as error:
            log_info = lgg.logger()
            log_info.info(error)   

            
connection, cursor = estab_conn.cn()
sql = DbConnect(connection, cursor)
sql.create_table()
sql.data_entry()
sql.display()
sql.connect()