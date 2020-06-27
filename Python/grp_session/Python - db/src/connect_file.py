import sqlite3
import config_file
from log_file import lgg

def cn():
    try:
        env = 'dev'
        db_conn = sqlite3.connect(config_file.connet(env))
        cr = db_conn.cursor
        msg = lgg.logger()
        msg.info("Connection established to Sqlite3 successfully")
        return db_conn, cr
    except sqlite3.Error as error:
        lg = lgg.logger()
        lg.info(error)