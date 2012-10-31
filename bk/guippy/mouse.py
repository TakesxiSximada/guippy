#-*- coding: utf-8 -*-
from . import api
from .decorator import interval

LEFT, MIDDLE, RIGHT = range(3)
class Mouse(object):
    
    @classmethod
    @interval
    def mouse(cls, code, xx=0, yy=0, wheel=0):
        api.mouse_event(code, xx, yy, wheel, 0)

    @classmethod
    @interval
    def event(cls, code, xx=0, yy=0, wheel=0):
        api.mouse_event(code, xx, yy, wheel, 0)
        
    def move(self):
        pass

    def drag(self):
        pass

    def drop(self):
        pass

    def click(self):
        pass

    def wclick(self):
        pass

    def wheel(self):
        pass


    def click_l(self):
        pass

    def click_r(self):
        pass

    def click_m(self):
        pass

    def wclick_l(self):
        pass

    def wclick_r(self):
        pass

    def wclick_m(self):
        pass

