from logger import logging

def add(a, b):
    logging.debug(f"Addtion is taking place")
    return a + b

logging.debug("The addition function is callled")
add(10,15)