import logging.config

logging.config.fileConfig("Logger.conf")


def debug(message):
    logging.debug(message)


def warning(message):
    logging.warning(message)
    

def info(message):
    logging.warning(message)
    
    
