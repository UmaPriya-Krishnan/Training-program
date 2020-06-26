import sqlite3
import conf

def cn():
    env = 'dev'
    db_conn = sqlite3.connect(conf.connet(env))
    cr = db_conn.cursor
    return db_conn, cr
    
if __name__ == '__main__':
    cn()
