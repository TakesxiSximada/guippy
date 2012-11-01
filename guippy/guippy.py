#-*- coding: utf-8 -*-
from .mouse import Mouse
from .window import Window
from .keyboard import Keyboard
from .clipboard import Clipboard

class PedigreeGuippy(object):
    def __init__(self):
        self.ms = Mouse()
        self.cb = Clipboard()
        self.kbd = Keyboard()
        self.win = Window()

    def chase(self):
        pass

    def get_area(self):
        pass

    def get_line(self):
        pass

    def poweroff(self):
        pass

class HybridGuippy(PedigreeGuippy, Mouse, Keyboard, Window, Clipboard):
    def __init__(self):
        self.ms = self
        self.cb = self
        self.kbd = self
        self.win = self

Guippy = HybridGuippy
