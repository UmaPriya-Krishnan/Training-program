import logging  

class lgg():
    def logger():
        logging.basicConfig(filename="db_log.txt", filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)  
        return logging
