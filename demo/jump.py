#! /usr/bin/env python
#-*- coding: utf-8 -*-
import startup
import guippy

import time

def main():
    for ii in range(1000):
        guippy.Mouse.jump(ii, ii, False, True)
        time.sleep(0.1)

if __name__ == '__main__':
    main()
