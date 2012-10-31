#-*- coding: utf-8 -*-
import ctypes
from .api import HWND, GlobalLock, OpenClipboard, GlobalUnlock, CloseClipboard, GetClipboardData, CF_UNICODETEXT

class Clipboard(object):
    @staticmethod
    def get(hwnd=None):
        if hwnd is None:
            hwnd = HWND(0)
            
        org_restype = GlobalLock.restype

        OpenClipboard(hwnd)
        try:
            hmem = GetClipboardData(CF_UNICODETEXT)
            GlobalLock.restype = ctypes.c_wchar_p
            try: 
                return GlobalLock(ctypes.c_int(hmem)) # return unicode text
            finally:
                GlobalUnlock(hmem)
        finally:
            GlobalLock.restype = org_restype 
            CloseClipboard()

    def set():
        assert False, 'not support.'

