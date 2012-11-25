#-*- coding: utf-8 -*-
import Tkinter as tkinter
import time

try:
    import startup
except ImportError:
    pass

import guippy

def main():
    root = tkinter.Tk()
    xx_yy = tkinter.StringVar()
    tkinter.Entry(root, textvariable=xx_yy).pack()

    def get_coord():
        coord = guippy.Mouse.now(normalize=False)
        xx_yy.set(str(coord))
        root.after(100, get_coord)
    get_coord()
    root.mainloop()
if __name__ == '__main__':
    main()
