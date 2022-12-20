mobs = [ 'anupam', 'sutapa', 'riya', 'sanju', 'rosni', 'sonali', 'susmita', 'rahul', 'mohasin', 'moha', 'jonaki', 'juliet', 'raaj','priya', 'harimahan', ' haridas', 'haripal', 'suman', 'joya', 'prantik', 'kartik', 'nayra', 'arif', 'souvik', 'ripon', 'puspa', 'allu arjun', 'ram', 'xukai', 'sunni', 'nobita', 'sunio', 'sinchain', 'gyan', 'arman', 'oggy', 'jack', 'paplu', 'dhaplu', 'jhaplu', 'sizuka', 'priti', 'ruhi', 'kenichi', 'ninja hattori', 'sisumanu', 'shinzo', 'bob', ]

fav_mobs = ['haripal', 'suman', 'joya', 'prantik', 'kartik', 'nayra', 'arif', 'souvik', 'ripon', 'Zebronics']

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
X = '\033[0;30m'
RED = '\033[0;31m'
# """ ANSI color codes """
    # BLACK = "\033[0;30m"
    # RED = "\033[0;31m"
    # GREEN = "\033[0;32m"
    # BROWN = "\033[0;33m"
    # BLUE = "\033[0;34m"
    # PURPLE = "\033[0;35m"
    # CYAN = "\033[0;36m"
    # LIGHT_GRAY = "\033[0;37m"
    # DARK_GRAY = "\033[1;30m"
    # LIGHT_RED = "\033[1;31m"
    # LIGHT_GREEN = "\033[1;32m"
    # YELLOW = "\033[1;33m"
    # LIGHT_BLUE = "\033[1;34m"
    # LIGHT_PURPLE = "\033[1;35m"
    # LIGHT_CYAN = "\033[1;36m"
    # LIGHT_WHITE = "\033[1;37m"
    # BOLD = "\033[1m"
    # FAINT = "\033[2m"
    # ITALIC = "\033[3m"
    # UNDERLINE = "\033[4m"
    # BLINK = "\033[5m"
    # NEGATIVE = "\033[7m"
    # CROSSED = "\033[9m"
    # END = "\033[0m"



print(fav_mobs)
for f in fav_mobs:
    if f in mobs:
        for i,each in enumerate(mobs,start=1):
            print("{} => {}".format(i,each))

    else:
        print(X+"mob : "+ f +" <= is not available")

