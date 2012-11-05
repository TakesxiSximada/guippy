#! /usr/bin/env python
#-*- coding: utf-8 -*-
try:
    import startup
except ImportError:
    pass

import guippy
def main():
    kbd = guippy.Keyboard
    kbd.windows('r')
    kbd.punch('cmd')
    kbd.enter()

if __name__ == '__main__':
    main()
