#! /usr/bin/env python
#-*- coding: utf-8 -*-
import time
import itertools
import ctypes
from ctypes.wintypes import BOOL, UINT, LONG, LPCWSTR, HWND, WPARAM, LPARAM, RECT, HGLOBAL, LPVOID, HANDLE

INTERVAL = 0.07

class _ENUM(object):
    def __init__(self, default=0, increment=None):
        self.current = default
        self.increment = increment if increment else lambda x: x+1
    
    def next(self, value=None, increment=None):
        if value is not None:
            self.current = value 
        if increment:
            self.increment = increment
        
        cur = self.current
        self.current = self.increment(self.current)
        return cur


KEYUP = 2
LEFT, MIDDLE, RIGHT = range(3)

# defined windows.h
SM_CXSCREEN = 0
SM_CYSCREEN = 1
GW_CHILD = 5
GW_ENABLEPOPUP = 6

XMAX = ctypes.windll.user32.GetSystemMetrics(SM_CXSCREEN)
YMAX = ctypes.windll.user32.GetSystemMetrics(SM_CYSCREEN)

class DisplayCoefficient:
    X = 0xFFFF / (XMAX * 1.0)
    Y = 0xFFFF / (YMAX * 1.0)
    
    @classmethod
    def convert_x(cls, val):
        return int(val * cls.X)

    @classmethod
    def convert_y(cls, val):
        return int(val * cls.Y)


_ME = _ENUM(0x0001, lambda x: x<<1).next
class MouseEvent:
    MOVE = _ME(0x0001)
    LEFTDOWN = _ME()
    LEFTUP = _ME()
    RIGHTDOWN = _ME()
    RIGHTUP = _ME()
    MIDDLEDOWN = _ME()
    MIDDLEUP = _ME()
    WHEEL = _ME(0x0800)
    ABSOLUTE = _ME(0x8000)

_VK = _ENUM().next
class VK:
    LBUTTON = _VK(0x01) # mouse left
    RBUTTON = _VK() # mouse right
    CANCEL = _VK()
    MBUTTON = _VK() # mouse middle
    XBUTTON1 = _VK()
    XBUTTON2 = _VK()
    RESV_7 = _VK()
    BACK = _VK() # back space
    TAB = _VK() # \t
    RESV_10 = _VK()
    RESV_11 = _VK()
    CLEAR = _VK()
    RETURN = _VK() # \n
    RESV_14 = _VK()
    RESV_15 = _VK()
    SHIFT = _VK() # shift
    CONTROL = _VK() # ctrl
    MENU = _VK() # alt (GRAPH)
    PAUSE = _VK() # pause
    CAPITAL = _VK() # caps lock
    KANA = HANGUL = _VK() # kana
    RESV_22 = _VK()
    JUNJA = _VK()
    FINAL = _VK()
    HANJA = KANJI = _VK() # kanji
    RESV_26 = _VK()
    ESCAPE = _VK() # escape
    CONVERT = _VK() # henkan
    NONCONVERT = _VK() # muhenkan
    ACCEPT = _VK()
    MODECHANGE = _VK()
    SPACE = _VK() # space
    PRIOR = _VK() # page up
    NEXT = _VK() # page down
    END = _VK() # end
    HOME = _VK() # home
    LEFT = _VK() # arrow
    UP = _VK() # arrow
    RIGHT = _VK() # arrow
    DOWN = _VK() # arrow
    SELECT = _VK()
    PRINT = _VK()
    EXECUTE = _VK()
    SNAPSHOT = _VK() # print screen
    INSERT = _VK() # insert
    DELETE = _VK() # delete
    HELP = _VK()
    N0 = _VK() # 0
    N1 = _VK() # 1
    N2 = _VK() # 2
    N3 = _VK() # 3
    N4 = _VK() # 4
    N5 = _VK() # 5
    N6 = _VK() # 6
    N7 = _VK() # 7
    N8 = _VK() # 8
    N9 = _VK() # 9
    # reserve
    A = _VK(0x41) # alphabet
    B = _VK() # alphabet
    C = _VK() # alphabet
    D = _VK() # alphabet
    E = _VK() # alphabet
    F = _VK() # alphabet
    G = _VK() # alphabet
    H = _VK() # alphabet
    I = _VK() # alphabet
    J = _VK() # alphabet
    K = _VK() # alphabet
    L = _VK() # alphabet
    M = _VK() # alphabet
    N = _VK() # alphabet
    O = _VK() # alphabet
    P = _VK() # alphabet
    Q = _VK() # alphabet
    R = _VK() # alphabet
    S = _VK() # alphabet
    T = _VK() # alphabet
    U = _VK() # alphabet
    V = _VK() # alphabet
    W = _VK() # alphabet
    X = _VK() # alphabet
    Y = _VK() # alphabet
    Z = _VK() # alphabet
    LWIN = _VK() # windows key left
    RWIN = _VK() # windows key right
    APPS = _VK() # application key
    RESV_94 = _VK()
    SLEEP = _VK()
    NUMPAD0 = _VK() # Num 0
    NUMPAD1 = _VK() # Num 1
    NUMPAD2 = _VK() # Num 2
    NUMPAD3 = _VK() # Num 3
    NUMPAD4 = _VK() # Num 4
    NUMPAD5 = _VK() # Num 5
    NUMPAD6 = _VK() # Num 6
    NUMPAD7 = _VK() # Num 7
    NUMPAD8 = _VK() # Num 8
    NUMPAD9 = _VK() # Num 9
    MULTIPLY = _VK() # Num *
    ADD = _VK() # Num +
    SEPARATOR = _VK() # Num ,
    SUBTRACT = _VK() # Num -
    DECIMAL = _VK() # Num .
    DIVIDE = _VK() # Num /
    F1 = _VK() # function key
    F2 = _VK() # function key
    F3 = _VK() # function key
    F4 = _VK() # function key
    F5 = _VK() # function key
    F6 = _VK() # function key
    F7 = _VK() # function key
    F8 = _VK() # function key
    F9 = _VK() # function key
    F10 = _VK() # function key
    F11 = _VK() # function key
    F12 = _VK() # function key
    F13 = _VK() # function key
    F14 = _VK() # function key
    F15 = _VK() # function key
    F16 = _VK() # function key
    F17 = _VK() # function key
    F18 = _VK() # function key
    F19 = _VK() # function key
    F20 = _VK() # function key
    F21 = _VK() # function key
    F22 = _VK() # function key
    F23 = _VK() # function key
    F24 = _VK() # function key
    # reserve
    NUMLOCK = _VK(0X90) # NumLock
    SCROLL = _VK() # ScrollLock
    EQUAL = _VK() # Num =
    # RESERV
    LSHIFT = _VK(0xa0) # shift left
    RSHIFT = _VK() # shift right
    LCONTROL = _VK() # ctrl left
    RCONTROL = _VK() # ctrl right
    LMENU = ALT_L = _VK() # alt left
    RMENU = ALT_R = _VK() # alt right
    BROWSER_BACK = _VK()
    BROWSER_FORWARD = _VK()
    BROWSER_REFRESH = _VK()
    BROWSER_STOP = _VK()
    BROWSER_SEARCH = _VK()
    BROWSER_FAVORITES = _VK()
    BROWSER_HOME = _VK()
    VOLUME_MUTE = _VK()
    VOLUME_DOWN = _VK()
    VOLUME_UP = _VK()
    MEDIA_NEXT_TRACK = _VK()
    MEDIA_PREV_TRACK = _VK()
    MEDIA_STOP = _VK()
    MEDIA_PLAY_PAUSE = _VK()
    LAUNCH_MAIL = _VK()
    LAUNCH_MEDIA_SELECT = _VK()
    LAUNCH_APP1 = _VK()
    LAUNCH_APP2 = _VK()
    RESV_184 = _VK()
    RESV_185 = _VK()
    OEM_1 = COLON = _VK() # :
    OEM_PLUS = SEMICOLON = _VK() # ;
    OEM_COMMA = COMMA = _VK() # ,
    OEM_MINUS = MINUS = _VK() # -
    OEM_PERIOD = DOT = _VK() # .
    OEM_2 = SLASH = _VK() # /
    OEM_3 = AT = _VK() # @
    # reserve
    OEM_4 = BOX_O = _VK(0xdb) # [
    OEM_5 = BACKSLASH = _VK() # \
    OEM_6 = BOX_C = _VK() # ]
    OEM_7 = CARET = _VK() # ^
    OEM_8 =  _VK() # _
    RESV_224 = _VK()
    OEM_AX = _VK()
    OEM_102 = UNDERLINE = _VK() # _
    ICO_HELP = _VK()
    ICO_00 = _VK()
    PROCESSKEY = _VK()
    PACKET = _VK()
    RESV_232 = _VK()
    OEM_RESET = _VK()
    OEM_JUMP = _VK()
    OEM_PA1 = _VK()
    OEM_PA2 = _VK()
    OEM_PA3 = _VK()
    OEM_WSCTRL = _VK()
    OEM_CUSEL = _VK()
    OEM_ATTN = _VK()
    OEM_FINISH = _VK()
    OEM_COPY = _VK()
    OEM_AUTO = _VK()
    OEM_ENLW = _VK()
    OEM_BACKTAB = _VK()
    ATTN = _VK()
    CRSEL = _VK()
    EXSEL= _VK()
    EREOF = _VK()
    PLAY = _VK()
    ZOOM = _VK()
    NONAME = _VK()
    PA1 = _VK()
    OEM_CLEAR = _VK()

del _VK

_ = VK


class Keycode(object):
    FUNC_CODE = {1: _.F1,
                 2: _.F2,
                 3: _.F3,
                 4: _.F4,
                 5: _.F5,
                 6: _.F6,
                 7: _.F7,
                 8: _.F8,
                 9: _.F9,
                 10: _.F10,
                 11: _.F11,
                 12: _.F12,
                 13: _.F13,
                 14: _.F14,
                 15: _.F15,
                 16: _.F16,
                 17: _.F17,
                 18: _.F18,
                 19: _.F19,
                 20: _.F20,
                 21: _.F21,
                 22: _.F22,
                 23: _.F23,
                 24: _.F24,
                 }

    CHAR_CODE = {'\t': _.TAB,
                 '\n': _.RETURN,
                 ' ': _.SPACE,
                 '-': _.MINUS,
                 '^': _.CARET,
                 '\\': _.BACKSLASH,
                 '@': _.AT,
                 '[': _.BOX_O,
                 ';': _.SEMICOLON,
                 ':': _.COLON,
                 ']': _.BOX_C,
                 ',': _.COMMA,
                 '.': _.DOT,
                 '/': _.SLASH,
                 _.UNDERLINE: _.UNDERLINE, # -
                 }

    SHIFTCHAR_CHAR = {'!': '1',
                      '"': '2',
                      '#': '3',
                      '$': '4',
                      '%': '5',
                      '&': '6',
                      "'": '7',
                      '(': '8',
                      ')': '9',
                      '=': '-',
                      '~': '^',
                      '|': '\\',
                      '`': '@',
                      '{': '[',
                      '+': ';',
                      '*': ':',
                      '}': ']',
                      '<': ',',
                      '>': '.',
                      '?': '/',
                      '_': _.UNDERLINE,
                      }
    
    @classmethod
    def char2codes(cls, char):
        SHIFT = VK.SHIFT
        shift_on = False
        
        try:
            if char.isalpha() and char.upper():
                raise KeyError # on shift
            else:
                target_char = cls.SHIFTCHAR_CHAR[char]
        except KeyError, err:
            target_char = char
        else:
            yield SHIFT, True, False
            shift_on = True
        
        try:
            yield cls.CHAR_CODE[target_char], True, True
        except KeyError, err:
            yield ord(char.upper()), True, True
            #assert False, 'Not support char: {0}'.format(char)
        
        # shift off
        if shift_on:
            yield SHIFT, False, True
    
    def func2codes(self, num):
        try:
            code = cls.FUNC_CODE[num]
        except KeyError, err:
            assert False, 'Not support char: {0}'.format(num)
        else:
            yield code, True, True

LPCTSTR = LPCWSTR
USER32 = ctypes.windll.LoadLibrary('user32.dll')

def _errcheck_null(result, func, args):
    if result is None:
        raise ctypes.WinError()
    return args

# prototype
FindWindow = ctypes.WINFUNCTYPE(HWND, LPCTSTR, LPCTSTR)(
    ('FindWindowW', USER32),
    ((1, 'lpClassName'), (1, 'lpWindowName'))
    )
FindWindow.errcheck = _errcheck_null

FindWindowEx = ctypes.WINFUNCTYPE(HWND, HWND, HWND, LPCTSTR, LPCTSTR)(
    ('FindWindowExW', USER32),
    ((1, 'hwndParent'),
     (1, 'hwndChildAfter'),
     (1, 'lpClassName'),
     (1, 'lpWindowName'),
     ))
FindWindowEx.errcheck = _errcheck_null

#SetActiveWindow = ctypes.WINFUNCTYPE(HWND, HWND)(
#    ('SetActiveWindow', USER32),
#    ((1, 'hWnd')))
#SetActiveWindow.errcheck = _errcheck_null

# defined in winbase.h
GMEM_MOVEABLE = 0x0002
GMEM_ZEROINIT = 0x0040
GHND = GMEM_MOVEABLE | GMEM_ZEROINIT

# defined in winuser.h
CF_TEXT = 1
CF_UNICODETEXT = 13

# private utilities
def _fptr_from_windll(dllname, funcname, restype=None, errcheck=None):
    dll = getattr(ctypes.windll, dllname)
    fptr = getattr(dll, funcname)
    if restype is not None:
        fptr.restype = restype
    if errcheck is not None:
        fptr.errcheck = errcheck
    return fptr

def _api_user32(*args, **kwds):
    return _fptr_from_windll('user32', *args, **kwds)

def _api_kernel32(*args, **kwds):
    return _fptr_from_windll('kernel32', *args, **kwds)

# Windows API
_e = _errcheck_null
GlobalAlloc      = _api_kernel32('GlobalAlloc', HGLOBAL, _e)
GlobalFree       = _api_kernel32('GlobalFree', HGLOBAL, _e)
GlobalLock       = _api_kernel32('GlobalLock', LPVOID, _e)
GlobalUnlock     = _api_kernel32('GlobalUnlock', BOOL, _e)
OpenClipboard    = _api_user32('OpenClipboard', BOOL, _e)
CloseClipboard   = _api_user32('CloseClipboard', BOOL, _e)
GetClipboardData = _api_user32('GetClipboardData', HANDLE, _e)



class Window(object):
    def __init__(self, cname=None, wname=None, catch=True, hwnd=None):
        self.hwnd = None
        self.cname = cname
        self.wname = wname
        
        if catch:
            self.catch()
    
    def catch(self):
        self.hwnd = self.get_window(self.cname, self.wname)
        
    @staticmethod
    def get_window(cname=None, wname=None):
        func = None
        args = None
        if cname == wname == None:
            func = ctypes.windll.user32.GetForegroundWindow
            args = []
        else:
            func = FindWindowEx
            args = [None, None, cname, wname]
        
        for ii in itertools.count():
            try:
                #hwnd = func(*args) # (-o-;)!?
                hwnd = FindWindowEx(None, None, cname, wname)
                if hwnd:
                    return hwnd
            except WindowsError, err:
                print err
        assert False

    def get_child(self):
        child_hw = ctypes.windll.user32.GetWindow(self.hwnd, GW_CHILD)
        return Window(hwnd=child_hw)
    
    def get_popup(self):
        child_hw = ctypes.windll.user32.GetWindow(self.hwnd, GW_ENABLEDPOPUP)
        return Window(hwnd=child_hw)


    def active(self):
        ctypes.windll.user32.SetForegroundWindow(self.hwnd)
        time.sleep(INTERVAL)

    def get_window_rect(self, absolute=True):
        rect = RECT()
        lprect = ctypes.pointer(rect)
        ctypes.windll.user32.GetWindowRect(self.hwnd, lprect)
        if absolute:
            rect.left = DisplayCoefficient.convert_x(rect.left)
            rect.top  = DisplayCoefficient.convert_y(rect.top)
        return rect

    def chase(self, xx=0, yy=0):
        rect = self.get_window_rect()
        xx = DisplayCoefficient.convert_x(xx) + rect.left
        yy = DisplayCoefficient.convert_y(yy) + rect.top
        self.point(xx, yy)
        
    def punch(self, message):
        for char in list(message):
            for code, down, up in Keycode.char2codes(char):
                self.keyboard(code, down, up)

    def click(self, *args, **kwds):
        self.drag(*args, **kwds)
        self.drop(*args, **kwds)

    def escape(self, message=''):
        code = VK.ESCAPE
        self.keyboard(code, down=True, up=False)
        self.punch(message)
        self.keyboard(code, down=False, up=True)

    def home(self, on=True, off=True):
        code = VK.HOME
        if on:
            self.keyboard(code, down=True, up=False)
        if off:
            self.keyboard(code, down=False, up=True)

    def end(self, on=True, off=True):
        code = VK.END
        if on:
            self.keyboard(code, down=True, up=False)
        if off:
            self.keyboard(code, down=False, up=True)

    def F(self, num):
        for code, down, up in Keycode.func2codes(num):
            self.keyboard(code, down, up)
            
    def enter(self):
        self.punch('\n')

    def shift(self, message='', on=True, off=True):
        code = VK.SHIFT
        if on:
            self.keyboard(code, down=True, up=False)
        self.punch(message)
        if off:
            self.keyboard(code, down=False, up=True)

    def ctrl(self, message='', on=True, off=True):
        code = VK.LCONTROL
        if on:
            self.keyboard(code, down=True, up=False)
        self.punch(message)
        if off:
            self.keyboard(code, down=False, up=True)

    def alt(self, message='', on=True, off=True):
        code = VK.ALT_L
        if on:
            self.keyboard(code, down=True, up=False)
        self.punch(message)
        if off:
            self.keyboard(code, down=False, up=True)
    
    def backspace(self, message='', on=True, off=True):
        code = VK.BACK
        if on:
            self.keyboard(code, down=True, up=False)
        self.punch(message)
        if off:
            self.keyboard(code, down=False, up=True)
    
    def keyboard(self, code, down=True, up=True):
        if down:
            self.key_down(code)
        if up:
            self.key_up(code)
    
    @property
    def user32(self):
        return ctypes.windll.user32

    # I/F to OS
    def key_down(self, code):
        self.user32.keybd_event(code, 0, 0, 0)
        time.sleep(INTERVAL)
        
    def key_up(self, code):
        self.user32.keybd_event(code, 0, KEYUP, 0)
        time.sleep(INTERVAL)
    
    # mouse 
    def click(self, *args, **kwds):
        self.drag(*args, **kwds)
        self.drop(*args, **kwds)

    def wclick(self, target=LEFT):
        self.click(target)
        self.click(target)


    def drag(self, target=LEFT):
        _target_code = {LEFT: MouseEvent.LEFTDOWN,
                        MIDDLE: MouseEvent.MIDDLEDOWN,
                        RIGHT: MouseEvent.RIGHTDOWN,
                        }
        code = _target_code[target]
        return self.mouse(code)

    def drop(self, target=LEFT):
        _target_code = {LEFT: MouseEvent.LEFTUP,
                        MIDDLE: MouseEvent.MIDDLEUP,
                        RIGHT: MouseEvent.RIGHTUP,
                        }
        code = _target_code[target]
        return self.mouse(code)
    
    def point(self, xx, yy, absolute=True):
        code = MouseEvent.MOVE
        if absolute:
            code |= MouseEvent.ABSOLUTE
        return self.mouse(code, xx, yy)

    def mouse(self, code, xx=0, yy=0, wheel=0):
        self.user32.mouse_event(code, xx, yy, wheel, 0)
        time.sleep(INTERVAL)
    
    def mark_line_all(self):
        self.home()
        self.shift(on=True, off=False)
        self.end()
        self.shift(on=False, off=True)
        
    def copy(self):
        self.ctrl('c')
        
    def clipboard(self, hwnd=None):
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

def main():
    win = Window(cname='Emacs', wname='emacs@HOSTNAME')
    win.active()
    win.chase()
    for ii in range(200):
        win.chase(ii, ii)

if __name__ == '__main__':
    main()
