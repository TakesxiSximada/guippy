#-*- coding: utf-8 -*-
from .decorator import interval
from .window import Window

class Operator(object):
    def __init__(self, *args, **kwds):
        assert False, 'not support'

    @interval
    def chase(self, xx=0, yy=0):
        assert False, 'not support'        
        
