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
    cname = tkinter.StringVar()
    wname = tkinter.StringVar()

    tkinter.Entry(root, textvariable=cname).pack()
    tkinter.Entry(root, textvariable=wname).pack()

    def get_name():
        win = guippy.Window()
        win.catch()
        
        _cname = win.get_cname()
        _wname = win.get_wname()

        cname.set(_cname)
        wname.set(_wname)
        root.after(100, get_name)
    get_name()
    root.mainloop()

if __name__ == '__main__':
    main()
