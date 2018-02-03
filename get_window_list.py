import subprocess
import re


def get_window_list():
    """
    A function that returns a list of open windows and
    their attributes.
    Each window in the list has a list of attributes in the following order:
    <window ID> <desktop ID> <X>,<Y>,<W>,<H> <client machine> <window title>
    """
    proc = subprocess.run(['wmctrl', '-lG'], encoding='utf-8', stdout=subprocess.PIPE)
    windstr = proc.stdout
    windstr = re.sub(' +', " ", windstr)
    windlist = windstr.split('\n')
    if windlist[-1] == '':
        windlist = windlist[:-1]
    windowlist = []
    for line in range(len(windlist)):
        win = windlist[line].split(" ", 7)
        windowlist.append(win)
    return windowlist


if __name__ == "__main__":
    print(*get_window_list(), sep='\n')
