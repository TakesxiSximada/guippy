#! /usr/bin/env python
#-*- coding: utf-8 -*-
try:
    import startup
except ImportError:
    pass

import guippy
def main():
    kbd = guippy.Keyboard()
    kbd.windows('d')

if __name__ == '__main__':
    main()
