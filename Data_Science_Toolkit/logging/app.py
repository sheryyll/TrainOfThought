import logging

# logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers = [
        logging.FileHandler("app1.log"), 
        logging.StreamHandler()
    ],
    force=True
)

logger = logging.getLogger("ArithmeticApp")

def add(a,b):
    result = a + b
    logger.debug(f"Adding {a} and {b} to get {result}")
    return result

def subtract(a,b):
    result = a - b
    logger.debug(f"Subtracting {a} and {b} to get {result}")
    return result

def multiply(a,b):
    result = a * b
    logger.debug(f"Multiplying {a} and {b} to get {result}")
    return result

def divide(a,b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} and {b} to get {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
add(10, 15)
subtract(20, 19)
multiply(10, 20)
divide(100, 50)
