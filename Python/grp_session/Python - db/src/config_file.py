import configparser
from log_file import lgg

config = configparser.ConfigParser()
config.read('C:\\Users\\mohan\\Desktop\\db_base\\config\\config.ini')

def connet(env):
    try:
        db = config.get(env, 'db')
        lg = lgg.logger()
        lg.info('Configuration done successfully')
        return db 
    except Exception as error:
        lg = lgg.logger()
        lg.info(error)
