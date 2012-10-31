#-*- coding: utf-8 -*-
import time
from . import util, api, shortcut
from .decorator import interval
from .shortcut import get_window_rect, Normarize

class Window(object):
    def __init__(self, cname=None, wname=None, catch=False, interval=0.07):
        self.cname = cname
        self.wname = wname
        self.hwnd = None # window handle
        self.interval = interval

    def catch(self, cname=None, wname=None, *args, **kwds):
        if cname is not None:
            self.cname = cname
        if wname is not None:
            self.wname = wname
        self.hwnd = shortcut.get_window_handle(self.cname, self.wname, 
                                               *args, **kwds)
    def get_rect(self, *args, **kwds):
        return get_window_rect(self.hwnd, *args, **kwds)

    def set_rect(self, *args, **kwds):
        assert False, 'not support'
    
    @interval
    def active(self):
        api.SetForegroundWindow(self.hwnd)
        
    def get_child(self):
        assert False, 'not support'

    def get_popup(self):
        assert False, 'not support'
