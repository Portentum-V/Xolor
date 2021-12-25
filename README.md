# Xolor!

A quick and dirty class for adding color to the commandline.

+ The `Xolor` class provides select graphic renditions which are supported by most terminals.
+ The `Xog` class provides a decorator for logging functions.

*I make no guarantees that this will work for you*

### Example
```
from Xolor.Xog import Xog

xog = Xog()

@xog.log
def my_func(one, two, three):
    logger = xog.getLogger()
    logger.critical("something reallllly bad just happened")
    logger.info("information!")
    return [two]
    
def example():
    my_func(1, "Whatever", None)
    xog.changeLevel(15)
    my_func({}, 62, "Like")
    xog.changeLevel(45)
    my_func("jeez", [], 4.5)
    
>>> example()
[v] 2021-12-25 00:39:52,673| my_func called with args 1, 'Whatever', None
[*] 2021-12-25 00:39:52,673| core.py-my_func:59| something reallllly bad just happened
[~] 2021-12-25 00:39:52,673| core.py-my_func:60| information!
[v] 2021-12-25 00:39:52,673| my_func returned ['Whatever']
[*] 2021-12-25 00:39:52,673| core.py-my_func:59| something reallllly bad just happened
[~] 2021-12-25 00:39:52,673| core.py-my_func:60| information!
[*] 2021-12-25 00:39:52,674| core.py-my_func:59| something reallllly bad just happened
```
