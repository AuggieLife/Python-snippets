from Xlib import display
from collections import namedtuple


def get_mouse_pos():
    data = display.Display().screen().root.query_pointer()._data
    Mouseposition = namedtuple('Mouseposition', ['x', 'y'])
    mouseposition = Mouseposition(data["root_x"], data["root_y"])
    return mouseposition


if __name__ == '__main__':
    m = get_mouse_pos()
    print(m.x)
