#-*- coding: utf-8 -*-
import ctypes
from . import api

class Display:
    XMAX = api.GetSystemMetrics(api.SM_CXSCREEN)
    YMAX = api.GetSystemMetrics(api.SM_CYSCREEN)
    
class Normarize:
    COEF_X = 0xFFFF/float(Display.XMAX)
    COEF_Y = 0xFFFF/float(Display.YMAX)
    
    @classmethod
    def xx(cls, value):
        return int(value * cls.COEF_X)

    @classmethod
    def yy(cls, value):
        return int(value * cls.COEF_Y)

    @classmethod
    def rect(cls, rect):
        rect.left = cls.xx(rect.left)
        rect.right = cls.xx(rect.right)
        rect.top = cls.yy(rect.top)
        rect.bottom = cls.yy(rect.bottom)
        return rect
        
def get_window_handle(cname=None, wname=None, timeout=10, interval=1):
    func, args = None, None
    if cname == wname == None:
        func = api.GetForegroundWindow
        args = []
    else:
        func = api.FindWindowEx
        args = [None, None, str(cname), str(wname)]
    
    for ii in range(timeout/interval):
        try:
            hwnd = func(*args)
            if hwnd:
                return hwnd
        except Windowserror, err:
            pass
        time.sleep(interval)
    raise TimeoutError()

def get_window_rect(hwnd, absolute=True):
    rect = api.RECT()
    lprect = ctypes.pointer(rect)
    api.GetWindowRect(hwnd, lprect)
    if absolute:
        rect = Normarize.rect(rect)
    return rect

