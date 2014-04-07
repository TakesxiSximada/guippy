#! /usr/bin/env python
#-*- coding: utf-8 -*-
import time

try:
    import startup
except ImportError:
    pass

import guippy
from guippy.application import Notepad

def main():
    gp = guippy.PedigreeGuippy()
    gp.kbd.windows('r')
    gp.kbd.enter('notepad')
    names = Notepad.names()
    for ii in range(3):
        try:
            gp.win.catch(*names)
        except guippy.error.Timeout:
            continue
        else:
            break
    else:
        raise guippy.error.Timeout

    gp.win.active()
    gp.win.minimize()
    gp.win.maximize()
    gp.chase(50, 50)
    gp.win.restore()
    gp.chase(50, 50)
    gp.win.active()
    gp.kbd.punch('hello world!' * 30)

if __name__ == '__main__':
    main()
