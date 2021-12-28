"""
Xog.py
"""
import logging
import inspect 
import sys

# lazy for testing import
from Xolor import Xolor

# Source: https://newbedev.com/how-to-add-a-custom-loglevel-to-python-s-logging-facility
def addLoggingLevel(level_str: str, level_int: int, method_str: str = None):
    if not method_str:
        method_str = level_str.lower()

    if hasattr(logging, level_str):
        raise AttributeError(f'{level_str} already defined in logging module')
    if hasattr(logging, method_str):
        raise AttributeError(f'{method_str} already defined in logging module')
    if hasattr(logging.getLoggerClass(), method_str):
        raise AttributeError(f'{method_str} already defined in logger class')
        
    def logForLevel(self, message, *args, **kwargs):
        if self.isEnabledFor(level_int):
            self._log(level_int, message, args, **kwargs)
    def logToRoot(message, *args, **kwargs):
        logging.log(level_int, message, *args, **kwargs)

    logging.addLevelName(level_int, level_str)
    setattr(logging, level_str, level_int)
    setattr(logging.getLoggerClass(), method_str, logForLevel)
    setattr(logging, method_str, logToRoot)

class XogFormat(logging.Formatter):
    """
    XogFormat:
        A log formatter class, used buy Xog to add Xolor spice based on log level.
    """
    xolor = Xolor()

    def __init__(self, verbose_level: int = 5, print_level: int = 35):
        super().__init__(fmt="%(asctime)s| %(funcName)s: %(lineno)d| %(message).640s")
        # Add two print levels, verbose for LOTS of message, print for anything
        try:
            addLoggingLevel("VERBOSE", verbose_level)
        except AttributeError:
            pass

        try:
            addLoggingLevel("PRINT", print_level)
        except AttributeError:
            pass

    def format(self, record):
        color = {
            logging.CRITICAL: self.xolor.CRIT,
            logging.ERROR: self.xolor.ERROR,
            logging.PRINT: "",
            logging.WARN: self.xolor.WARN,
            logging.INFO: self.xolor.INFO,
            logging.DEBUG: self.xolor.DEBUG,
            logging.VERBOSE: self.xolor.VERBOSE
        }.get(record.levelno, self.xolor.WEIRD)
        if record.levelno == logging.PRINT:
            self._style._fmt = f"%(message)s{self.xolor.END}"
        elif record.levelno == logging.VERBOSE:
            self._style._fmt = f"{color} %(asctime)s| %(message)s{self.xolor.END}"
        else:
            self._style._fmt = f"{color} %(asctime)s| %(filename)s-%(funcName)s:%(lineno)d| %(message)s{self.xolor.END}"
        return super().format(record)

class Xog():
    """
    Xog:
        A log decorator for doing log things!
    """
    log_level = 5

    def __init__(self, log_name: str = __name__, log_level: int = 5, stream = sys.stdout):
        self.log_name = log_name
        self.log_level = log_level

        self.logger = logging.getLogger(log_name)

        self.changeLevel(log_level)
        self.addStreamHandler(stream, self.log_level)

    def changeLevel(self, log_level: int = 5):
        self.logger.setLevel(log_level)
        for hdlr in self.logger.handlers:
            hdlr.setLevel(log_level)
        
    def addStreamHandler(self, stream, log_level: int = 5):
        ch = logging.StreamHandler(stream) # console handler, logging default sys.stderr, func default sys.stdout
        ch.setLevel(log_level)
        ch.setFormatter(XogFormat())
        self.logger.addHandler(ch)
        return ch

    def changeHandlerLevel(self, hdlr, log_level: int = 5):
        hdlr.setLevel(log_level)

    def removeHandler(self, hdlr):
        self.logger.handlers.remove(hdlr)

    def clearHandlers(self):
        self.logger.handlers.clear()

    def getLogger(self):
        return self.logger

    def log(self, func = None):
        def log_wrapper(*args, **kwargs):
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            params = ", ".join(args_repr + kwargs_repr)
            self.logger.verbose(f'{func.__name__} called with{"out" if not params else ""} args {params}')
            try:
                result = func(*args, **kwargs)
                self.logger.verbose(f'{func.__name__} returned {result}')
                return result
            except Exception as e:
                self.logger.exception(f"{type(e).__name__}: {e}")
                raise e
        return log_wrapper