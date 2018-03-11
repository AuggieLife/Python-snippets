from Xlib import display
from collections import namedtuple
import tkinter as tk


def position_label(label, geo):
    def get_mouse_pos():
        data = display.Display().screen().root.query_pointer()._data
        Mouseposition = namedtuple('Mouseposition', ['x', 'y'])
        mouseposition = Mouseposition(data["root_x"], data["root_y"])
        if geo == "x":
            label.config(text=str(mouseposition.x))
        else:
            label.config(text=str(mouseposition.y))
        label.after(100, get_mouse_pos)
    get_mouse_pos()


root = tk.Tk()
root.geometry("170x65+10+10")
root.title("Mouse Position")

x_label = tk.Label(root,
                   justify=tk.RIGHT,
                   bg="red",
                   text="X POS:")
x_label.place(x=10,
              y=5,
              width=40,
              height=25)

x_pos = tk.Label(root,
                 justify=tk.LEFT,
                 bg="yellow",
                 fg="red")
x_pos.place(x=50,
            y=5,
            width=40,
            height=25)
position_label(x_pos, "x")

y_label = tk.Label(root,
                   justify=tk.RIGHT,
                   bg="red",
                   text='Y POS:')
y_label.place(x=90,
              y=5,
              width=40,
              height=25)

y_pos = tk.Label(root,
                 justify=tk.LEFT,
                 bg="yellow",
                 fg="red")
y_pos.place(x=130,
            y=5,
            width=40,
            height=25)
position_label(y_pos, "y")

button = tk.Button(root,
                   text='Stop',
                   command=root.destroy)
button.place(x=25,
             y=35,
             width=120,
             height=25)

root.mainloop()
