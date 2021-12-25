"""
Xog.py
"""
import logging
import inspect 
import sys

# lazy for testing import
try:
    from Xolor.Xolor import Xolor
except ModuleNotFoundError:
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

    def __init__(self):
        super().__init__(fmt="%(asctime)s| %(funcName)s: %(lineno)d| %(message)s")
        try:
            addLoggingLevel("VERBOSE", 5)
        except AttributeError:
            pass

    def format(self, record):
        color = {
            logging.CRITICAL: self.xolor.CRIT,
            logging.ERROR: self.xolor.ERROR,
            logging.WARN: self.xolor.WARN,
            logging.INFO: self.xolor.INFO,
            logging.DEBUG: self.xolor.DEBUG,
            logging.VERBOSE: self.xolor.VERBOSE
        }.get(record.levelno, self.xolor.WEIRD)
        self._style._fmt = f"{color} %(asctime)s| %(funcName)s: %(lineno)d| %(message)s{self.xolor.END}"
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
        self.addHandler(stream, self.log_level)

    def changeLevel(self, log_level: int = 5):
        self.logger.setLevel(log_level)
        for hdlr in self.logger.handlers:
            hdlr.setLevel(log_level)
        
    def addHandler(self, stream, log_level: int = 5):
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
                self.logger.verbose(f'{func.__name__} returned {result:.32s if result else "None"}')
                return result
            except Exception as e:
                self.logger.exception(f"{type(e).__name__}: {e}")
                raise e
        return log_wrapper

xog = Xog(log_level = 5)
@xog.log
def dec_log_tester():
    logger = xog.getLogger()
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
    print("Logger Verbose:")
    logger.verbose("OH GOD TO MUCH")
    return

def raw_log_tester(level:int = 1):
    logger = xog.getLogger()
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
    print("Logger Verbose:")
    logger.verbose("OH GOD TO MUCH")
    return

def level_tester():
    for level in range(0,50):
        print(logging.getLevelName(level))