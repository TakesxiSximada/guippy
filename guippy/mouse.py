#-*- coding: utf-8 -*-
from .api import mouse_event
from .decorator import interval

LEFT, MIDDLE, RIGHT - range(3)

class Button(object):

    @classmethod
    @interval
    def _mouse_event(cls, code, xx=0, yy=0, wheel=0):
        mouse_event(code, xx, yy, wheel, 0)

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

class Position(object):
    def jump(self):
        pass

    def coord(self):
        pass

    def now(self):
        pass

class Mouse(Button, Position):
    def point(self):
        pass

