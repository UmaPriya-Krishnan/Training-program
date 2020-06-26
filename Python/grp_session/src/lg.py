import logging  

class lgg():
    def logger():
        logging.basicConfig(filename="db_log0626.txt", filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)  
        return logging
