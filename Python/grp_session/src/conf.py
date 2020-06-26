import configparser

config = configparser.ConfigParser()
config.read('C:\\Users\\mohan\\Desktop\\db_base\\config\\co.ini')

def connet(env):
    db = config.get(env, 'db')
    return db 
    
if __name__ == '__main__':
    connet('dev')
    
    
   # sqlite3.connect('SQLite_Pyt.db')