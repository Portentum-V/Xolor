"""
Xog.py
"""
import logging
import inspect 
import sys

from Xolor.Xolor import Xolor

class Xog_Format(logging.Formatter):
    """
    Xog_Format:
        A log formatter class, used buy Xog to add Xolor spice based on log level.
    """
    xolor = Xolor()

    def __init__(self):
        super().__init__(fmt="%(asctime)s| %(funcName)s: %(lineno)d| %(message)s")
        logger = logging.getLogger(log_name)

    def format(self, record):
        color = {
            logging.CRITICAL: self.xolor.CRIT,
            logging.ERROR: self.xolor.ERROR,
            logging.WARN: self.xolor.WARN,
            logging.INFO: self.xolor.INFO,
            logging.DEBUG: self.xolor.DEBUG,
        }.get(record.levelno, self.xolor.WEIRD)
        self._style._fmt = f"{color} %(asctime)s| %(funcName)s: %(lineno)d| %(message)s{self.xolor.END}"
        return super().format(record)

class Xog():
    """
    Xog:
        A log decorator for doing log things!
    """
    xolor = Xolor()
    log_level = 10

    def __init__(self, log_name: str = __name__, log_level: int = 10, stream = sys.stdout):
        self.log_name = log_name
        self.log_level = log_level

        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(log_level)

        self.add_handler(stream)
        
    def get_logger():
        return self.logger

    def change_level(log_level: int = 10):
        self.logger.setLevel(log_level)
        for hdlr in logger.handlers:
            hdlr.setLevel(log_level)
        
    def add_handler(log_level: int = 10, stream):
        ch = logging.StreamHandler(stream) # console handler, logging default sys.stderr, func default sys.stdout
        ch.setLevel(log_level)
        ch.setFormatter(Xog_Format())
        self.logger.addHandler(ch)
        return ch

    def remove_handler(hdlr):
        self.logger.handlers.remove(hdlr)

    def cleanup_logger():
        try:
            self.logger.handlers.clear()
        except Exception as e:
            print(f"{Xolor.ERROR}{type(e).__name__} occured while clearing logger:{Xolor.END} {e}")
        return

    def log(func = None):
        def wrapper(*args, **kwargs):
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            params = ", ".join(args_repr + kwargs_repr)
            self.logger.debug(f"{func.__name__} called with args {params}")
            try:
                result = func(*args, **kwargs)
                self.logger.debug(f"{func.__name__} returned with {result}")
                return result
            except Exception as e:
                self.logger.exception(f"{type(e).__name__}: {e}")
                raise e
        return wrapper

def log_tester(level:int = 1):
    xog = Xog(log_level = level)
    logger = xog.get_logger()
    print("Logger Critical:")
    logger.critical("CRIT HIT!")
    print("Logger Error:")
    logger.error("ERROR ERROR ERROR")
    print("Logger Exception:")
    logger.exception("An exception occured")
    print("Logger Warning:")
    logger.warning("Warning message here")
    print("Logger Info:")
    logger.info("Mad information status!")
    print("Logger Debug:")
    logger.debug("Very specific detail! Nice nice nice")
    return