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
        gp = guippy.Guippy()
        gp.catch()
        rect = gp.get_rect()
        xx, yy = guippy.Mouse.now(normalize=False)
        xx = rect.left - xx
        yy = rect.top - yy
        coord = xx, yy
        xx_yy.set(str(coord))
        root.after(100, get_coord)
    get_coord()
    root.mainloop()
if __name__ == '__main__':
    main()
