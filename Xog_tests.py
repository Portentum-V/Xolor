"""
Xog_tests.py
"""
from Xog import Xog

test_xog = Xog(log_level = 5)
@test_xog.log
def dec():
    logger = test_xog.getLogger()
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

def raw():
    logger = test_xog.getLogger()
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

def lvl():
    for level in range(0,50):
        print(logging.getLevelName(level))