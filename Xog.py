"""
Xog.py
"""
import logging
import inspect 

from Xolor.Xolor import Xolor

class Xog:
    """
    Xog:
        A log formatter for the logging module
    """
    xolor = Xolor()

    def __init__(self):
        super().__init__()

    def format(self, record):
        if record.levelno == logging.DEBUG:
            self._style._fmt = f"{self.xolor.DEBUG}%(module)s %(lineno)d: %(message)s {self.xolor.END}"
        else:
            color = {
                logging.CRITICAL: self.xolor.CRIT,
                logging.ERROR: self.xolor.ERROR,
                logging.WARN: self.xolor.WARN,
                logging.INFO: self.xolor.INFO
            }.get(record.levelno, 0)
            self._style._fmt = f"{color}%(message)s{self.xolor.END}"
        return super().format(record)

def configure_logger(log_level: int):
    name = inspect.stack()[1][3] # Get str name of caller
    
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    ch.setFormatter(Xog())

    logger.addHandler(ch)

    return logger

def log_tester(log_level:int = 1):
    logger = configure_logger(log_level)
    print("Logger Critical:")
    logger.critical("CRIT HIT!")
    print("Logger Error:")
    logger.error("ERROR ERROR ERROR")
    print("Logger Warning:")
    logger.warning("Warning message here")
    print("Logger Info:")
    logger.info("Mad information status!")
    print("Logger Debug:")
    logger.debug("Very specific detail! Nice nice nice")
    return