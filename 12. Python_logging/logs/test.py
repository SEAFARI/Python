from logger import logging

def add(a,b):
    logging.debug("Adding operation is taking place")
    return a+b

logging.debug("Adding operation is called")
add(2,3)