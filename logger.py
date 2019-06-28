import logging 
def log():
    FORMAT = '%(asctime)-15s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(filename='log/otomeshon.log', format=FORMAT,
        level=logging.INFO, datefmt='%Y-%m-%dT%H:%M:%S')
    return logging.getLogger('Otomeshon')

