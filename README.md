# Xolor!

A quick and dirty class for adding color to the commandline.

+ The `Xolor` class provides select graphic renditions which are supported by most terminals.
+ The `Xog` class provides a decorator for logging functions.

*I make no guarantees that this will work for you*

### Example
```
from Xolor.Xog import Xog

xog = Xog()

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
```
