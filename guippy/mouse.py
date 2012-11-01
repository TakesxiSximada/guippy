#-*- coding: utf-8 -*-
"""This and that in order to control the mouses.
"""
from .api import mouse_event, GetCursorPos, ME_MOVE, ME_ABSOLUTE, ME_WHEEL, \
    ME_LEFTDOWN, ME_LEFTUP, ME_MIDDLEDOWN, ME_MIDDLEUP, ME_RIGHTDOWN, ME_RIGHTUP   
from .decorator import interval

import ctypes
from ctypes.wintypes import POINTgxs

LEFT, MIDDLE, RIGHT = range(3)
BUTTONDOWN_EVENT = {LEFT: ME_LEFTDOWN,
                    MIDDLE: ME_MIDDLEDOWN,
                    RIGHT: ME_RIGHTDOWN,
                    }

BUTTONUP_EVENT = {LEFT: ME_LEFTUP,
                  MIDDLE: ME_MIDDLEUP,
                  RIGHT: ME_RIGHTUP,
                  }

DEFAULT_ABSOLUTE = True
DEFAULT_NORMARIZE = True

def _mouse_event(code, xx=0. yy=0, wheel=0, flag=0):
    """I/F with mouse_event().
    
    It created for setting default value.
    """
    return mouse_event(code, xx, yy, wheel, flag)

def call_mouse_event(func):
    """A decorator to call the mouse_event().

    このデコレータによってデコレーションされたメソッドは、
    その戻り値を引数としてmouse_event()をcallします。

    デコレーションされるメソッドの戻り値の型によって、
    mouse_event()への引数の渡し方が変化します。

    辞書型であればキーワード付き可変長引数として、
    リストかタプルであればキーワードなし可変長引数として、
    その他であれば単なる引数として、
    mouse_event()に渡します。

    この挙動で問題となるケースはmouse_event()の引数として、
    辞書型かリストかタプルを渡したいときです。その場合デコレーションされる
    メソッドの戻り値は、更にリストかタプルでラッピングしなければなりません。
    とはいえこのような引数はmouse_event()自身が受け付けないのでエラーになるでしょう。
    """

    def _wrap(obj, *args, **kwds):
        call_args = func(obj, *args, **kwds)
        typ = type(call_args)
        if typ == dict:
            return _mouse_event(**call_args)
        elif typ in (list, tuple):
            return _mouse_event(*call_args)
        else:
            return _mouse_event(call_args)
    return _wrap

class Button(object):
    @classmethod
    @call_mouse_event
    def drag(cls, button=None):
        """Drag on the button of mouse.

         A variable button is id of mouse button. Be input object with
        LEFT or MIDDLE or RIGHT. If not exist id then raise KeyError.
        """
        button = LEFT if button is None else button
        return BUTTONDOWN_EVENT[button] # raise KeyError
    
    @classmethod
    @call_mouse_event
    def drop(cls, button=None):
        """Drop off the button of mouse.
        
         A variable button is id of mouse button. See drag().
        """
        button = LEFT if button is None else button
        return BUTTONUP_EVENT[button] # raise KeyError

    @classmethod
    def click(cls, button=None):
        """Click the mouse.
        
         A variable button is id of mouse button. See drag().
        """
        cls.drag(button)
        cls.drop(button)
    
    @classmethod
    def wclick(cls, button=None):
        """Double click the mouse.

         A variable button is id of mouse button. See drag().
        """
        for ii in range(2):
            cls.click(button)
        
    @classmethod
    def wheel(cls, num=1):
        """Wheel the mouse.
        
         A variable num is wheel count. The num greater than 0, TEMAE.
        The num less than 0, MUKOU.
        """
        return ME_WHEEL|ME_MOVE, 0, 0, num

class Position(object):
    """Control position of mouse pointer.
    """

    @classmethod
    @call_mouse_event
    def jump(cls, xx, yy,
             normarize=DEFAULT_NORMARIZE, absolute=DEFAULT_ABSOLUTE):
        """Moving mouse pointer.

         The xx and yy is coord. The normarize is coord normarize switch.
        The absolute is switch of to using absolute coord.
        """
        code = ME_MOVE
        if normarize:
            code |= ME_ABSOLUTE

        if normarize and not absolute:
            nowx, nowy = cls.now(normarize)
            xx += nowx
            yy += nowy
        elif not normarize and absolute:
            nowx, nowy = cls.now(normarize)
            xx -= nowx
            yy -= nowy
        return code, xx, yy

    @staticmethod
    def now(normarize=DEFAULT_NORMARIZE):
        """Getting now coord of mouse pointer.
        
         The normarize is switch of to using mormarize coord.
        """
        point = POINT()
        lppoint = ctypes.pointer(point)
        GetCursorPos(lppoint)
        if normarize:
            point = Normarizer.point(point)
        return point.x, point.y

class Mouse(Button, Position):
    """Combination button and position of mouse emulate.
    """
    
    @classmethod
    def point(cls, *args, **kwds):
        """Click after move the mouse pointer.
        """
        cls.jump(*args, **kwds)
        cls.click()

