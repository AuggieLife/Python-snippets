from collections import namedtuple
import subprocess


def get_window_list():
    """
    A function that returns a list of open windows and
    their attributes.
    Each window in the list has a list of attributes in the following order:
    <window ID> <desktop ID> <X>,<Y>,<W>,<H> <client machine> <window title>
    """
    Window = namedtuple('Window', ['id', 'desktop',
                                   'x', 'y', 'w', 'h',
                                   'client', 'title'])
    proc = subprocess.run(['wmctrl', '-lG'], encoding='utf-8', stdout=subprocess.PIPE)
    windstr = proc.stdout.split('\n')[:-1]
    windows = [Window(*line.split(maxsplit=7)) for line in windstr]
    return windows


if __name__ == "__main__":
    x = get_window_list()
    for item in x:
        print("Window id = {}\nWindow Title = {}\n\n".format(item.id, item.title))
