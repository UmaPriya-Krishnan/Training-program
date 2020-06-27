import sqlite3
import connect_file
from log_file import lgg 

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
            create_query = "CREATE TABLE IF NOT EXISTS STUDENT (Roll_No Bigint primary key, Dep_id varchar(9), \
                            S_Name Char(20), Sex char(9), city char(20), p_no bignint, Stud_type Varchar(20), Credits int, year int)";
            self.cursor.execute(create_query)
            self.cursor.execute('delete from student')
            msg = lgg.logger()
            msg.info('Student table has been created successfully')
        except sqlite3.Error as error:
            log_info = lgg.logger()
            log_info.info(error)
            
    def data_entry(self):
        try:        
            filename = 'C:\\Users\\mohan\\Desktop\\db_base\\src\\student.csv'
            with open(filename,'r') as fr:
                for line in fr.readlines():
                    col_value = line.replace('\n','').split(',')
                    insert_query = "INSERT INTO STUDENT (Roll_No , Dep_id, S_Name, Sex, City, p_no, Stud_type, Credits, year )\
                    VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')" .format(col_value[0],col_value[1],col_value[2],col_value[3],col_value[4],col_value[5], col_value[6],col_value[7],col_value[8])
                    self.cursor.execute(insert_query)
            connection.commit()
            msg = lgg.logger()
            msg.info('Values are inserted into student table successfully')
        except sqlite3.Error as error:
            log_info = lgg.logger()
            log_info.info(error)
            print(error)

    def display(self):
        try:
            result = ''
            value = self.cursor.execute("SELECT * FROM STUDENT")
            for row in value:
                p = [str(i) for i in row]
                sep = ','.join(p)
                result = result+sep+'\n'
            msg = lgg.logger()
            msg.info('Selected Values are fetched')
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