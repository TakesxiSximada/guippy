#! /usr/bin/env python
#-*- coding: utf-8 -*-
import time
import math
import optparse
import itertools

try:
    import startup
except ImportError:
    pass

import guippy

def circle(xx, yy, speed=0xFFF):
    def _harf_circle(last_quarter=True):
        degree_list = range(180)
        unity = 1
        if not last_quarter:
            degree_list.reverse()
            unity = -unity
        
        _get_xx = lambda rad: int(math.cos(rad) * speed) + xx
        _get_yy = lambda rad: int(math.sin(rad) * speed * unity) + yy
        
        for deg in degree_list:
            rad = math.radians(deg)
            _xx = _get_xx(rad)
            _yy = _get_yy(rad)
            yield _xx, _yy

    for quarter in (True, False):
        for _xx, _yy in _harf_circle(last_quarter=quarter):
            yield _xx, _yy

def main():
    parser = optparse.OptionParser()
    parser.add_option('--eternal', default=False, action='store_true')
    opts, args = parser.parse_args()
    
    count = 3
    try:
        count = args[0]
    except IndexError:
        pass

    counter = range
    if opts.eternal:
        counter = lambda *args, **kwds: itertools.count()
    
    for ii in counter(count):
        for xx, yy in circle(0x5FFF, 0x5FFF, 0x2FFF):
            guippy.Mouse.jump(xx, yy)
            time.sleep(0.001)

if __name__ == '__main__':
    main()
