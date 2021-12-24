"""
Xolor.py
"""

class Xolor:
    """
    Xolor:
        A quick and dirty class for adding color to print statements
        Should work on most linux distros and Windows 10+
        
    Old Windows Req?
    if os.name == "nt": # Do this to get colors to work on Windows 10+
        import subprocess
        subprocess.call('', shell=True)

    Notes:
        Select graphic rendtions BOLD, FRAME, and CIRCLE did not work on Windows 10.
        Additionally, SLOW and FAST blink were at the same speed
    """
    # Bright Foreground Colors
    GRAY    = '\033[90m'
    RED     = '\033[91m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[93m'
    BLUE    = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN    = '\033[96m'
    WHITE   = '\033[97m'
    # Bright Background Colors
    BG_GRAY    = '\033[100m'
    BG_RED     = '\033[101m'
    BG_GREEN   = '\033[102m'
    BG_YELLOW  = '\033[103m'
    BG_BLUE    = '\033[104m'
    BG_MAGENTA = '\033[105m'
    BG_CYAN    = '\033[106m'
    BG_WHITE   = '\033[107m'

    # Select Graphic Renditions
    END     = '\033[0m' # Reset/Normal; default attributes
    BOLD    = '\033[1m'
    FAINT   = '\033[2m'
    ITALIC  = '\033[3m'
    UNDER   = '\033[4m'
    SLOW    = '\033[5m' # Blink Slow
    FAST    = '\033[6m' # Blink Fast
    INVERT  = '\033[7m' # Swap foreground and background color
    HIDE    = '\033[8m'
    CROSS   = '\033[9m'
    FRAME   = '\033[51m'
    CIRCLE  = '\033[52m'
    OVER    = '\033[53m'

    # Disable specific SGR
    NO_BOLD_OR_FAINT    = '\033[22m'
    NO_ITALIC           = '\033[23m'
    NO_UNDER            = '\033[24m'
    NO_BLNK             = '\033[25m'
    NO_INVERT           = '\033[27m'
    NO_CROSS            = '\033[29m'
    NO_FG               = '\033[39m' # Default foreground
    NO_BG               = '\033[49m' # Default background
    NO_FRAME_OR_CIRCLE  = '\033[54m'
    NO_OVER             = '\033[55m'

    # Normal FG ints; +10 for BG, +70 for Bright, +80 for BG Bright
    black   = 30
    red     = 31
    green   = 32
    yellow  = 33
    blue    = 34
    magenta = 35
    cyan    = 36
    white   = 37

    # Formating
    CRIT  = MAGENTA + SLOW + '[*]'
    ERROR = RED            + '[!]'
    WARN  = YELLOW         + '[?]'
    INFO  = WHITE + FAINT  + '[~]'
    DEBUG = GRAY           + '[-]'
    SUCC  = CYAN           + '[+]'
    NICE  = GREEN          + '[$]'
    WEIRD = BLUE           + '[ ]'

    # Lazy function
    def color_str(self, c: str, s: str):
        return(f"{c}{s}{self.END}")