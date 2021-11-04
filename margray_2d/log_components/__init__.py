from . import clr_win32 
import sys 

if sys.platform in ["win32", "cygwin"]:
    clr_win32.init()

class Props():
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GREYBG = '\033[100m'
    REDBG = '\033[101m'
    GREENBG = '\033[102m'
    YELLOWBG = '\033[103m'
    BLUEBG = '\033[104m'
    PINKBG = '\033[105m'
    CYANBG = '\033[106m' 

class Log():
    def __init__(self):
        self.props = Props()
    def cprint(self, text, color):
        print(color+text+'\033[0m')
    def colored(self, text, color):
        return color+text+'\033[0m'
    def warning(self, warning):
        self.cprint(warning,self.props.WARNING)
    def error(self, error):
        self.cprint(error,self.props.FAIL)                           