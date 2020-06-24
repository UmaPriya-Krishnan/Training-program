import sqlite3

def connect():
    try:
        connection = sqlite3.connect('SQLi.db')
        cursor = connection.cursor()
        return connection,cursor        
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def create_table(): 
    connection,cursor = connect()    
    create_query = "CREATE TABLE IF NOT EXISTS DEPT (dep_id varchar(10) primary key, dep_name varchar(20), dep_manager varchar(20))"
    cursor.execute(create_query)
    cursor.execute('delete from dept')
    print("Table created successfully")
    connection.commit()

def data_entry():
    connection,cursor = connect()
    filename = 'C:\\Users\\mohan\\Desktop\\Virtual training\\dept.csv'
    with open(filename,'r') as fr:
        for line in fr.readlines():
            col_value = line.replace('\n','').split(',')
            insert_query = "INSERT INTO DEPT (dep_id, dep_name, dep_manager) VALUES('{}','{}','{}')" .format(col_value[0],col_value[1],col_value[2])
            cursor.execute(insert_query)
    connection.commit()
    print("Values entered successfully")

def display():
    connection,cursor = connect()
    result = ''
    value = cursor.execute("SELECT * FROM dept")
    for i in value:
        sep = ','.join(i)
        result = result+sep +'\n'
    return result
    cursor.close
    
connect()
create_table()
data_entry()
display()