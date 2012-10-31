#-*- coding: utf-8 -*-
from . import api
from .decorator import interval, specialkey

class Keyboard(object):

    @staticmethod
    @interval
    def push(code):
        api.keybd_event(code, 0, 0, 0)

    @staticmethod
    @interval
    def pull(code):
        api.keybd_event(code, 0, api.KEYUP, 0)

    @classmethod
    def key(cls, code, push=True, pull=True):
        if push:
            cls.push(code)
        if pull:
            cls.pull(code)
        
    @classmethod
    def punch(cls, message):
        for char in list(message):
            for code, push, pull in Keycode.char2codes(char):
                cls.key(code, push, pull)

    def windows(self, message):
        self.key(api.VK_LWIN, True, False)
        #self.punch(message)
        self.key(api.VK_LWIN, False, True)

    @classmethod
    @specialkey
    def backspace(cls):
        return api.BACK

    @classmethod
    @specialkey
    def delete(cls):
        assert False, 'not supported'

    @classmethod
    @specialkey
    def alt(cls):
        return api.VK_ALT_L

    @classmethod
    @specialkey
    def ctrl(cls):
        return api.VK_LCONTROL

    @classmethod
    @specialkey
    def shift(self):
        return api.VK_LSHIFT

    def enter(self):
        pass

    def escape(self):
        pass

    def home(self):
        pass

    def end(self):
        pass
    
    def F(self):
        pass

    def Fn(self):
        pass

    def space(self):
        pass

class Keycode(object):
    FUNC_CODE = {1: api.VK_F1,
                 2: api.VK_F2,
                 3: api.VK_F3,
                 4: api.VK_F4,
                 5: api.VK_F5,
                 6: api.VK_F6,
                 7: api.VK_F7,
                 8: api.VK_F8,
                 9: api.VK_F9,
                 10: api.VK_F10,
                 11: api.VK_F11,
                 12: api.VK_F12,
                 13: api.VK_F13,
                 14: api.VK_F14,
                 15: api.VK_F15,
                 16: api.VK_F16,
                 17: api.VK_F17,
                 18: api.VK_F18,
                 19: api.VK_F19,
                 20: api.VK_F20,
                 21: api.VK_F21,
                 22: api.VK_F22,
                 23: api.VK_F23,
                 24: api.VK_F24,
                 }

    CHAR_CODE = {'\t': api.VK_TAB,
                 '\n': api.VK_RETURN,
                 ' ': api.VK_SPACE,
                 '-': api.VK_MINUS,
                 '^': api.VK_CARET,
                 '\\': api.VK_BACKSLASH,
                 '@': api.VK_AT,
                 '[': api.VK_BOX_O,
                 ';': api.VK_SEMICOLON,
                 ':': api.VK_COLON,
                 ']': api.VK_BOX_C,
                 ',': api.VK_COMMA,
                 '.': api.VK_DOT,
                 '/': api.VK_SLASH,
                 api.VK_UNDERLINE: api.VK_UNDERLINE, # -
                 }

    SHIFT_CHAR = {'!': '1',
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
                  '_': api.VK_UNDERLINE,
                  }
    
    @classmethod
    def char2codes(cls, char):
        char = str(char)
        shift_on = False
        
        try:
            if char.isalpha() and char.upper():
                pass # on shift
            else:
                char = cls.SHIFT_CHAR[char]
        except KeyError:
            pass
        else: # on shift procedure
            yield api.VK_LSHIFT, True, False
            shift_on = True
        
        code = None
        try:
            code = cls.CHAR_CODE[char]
        except KeyError:
            code = ord(char.upper())
        assert code, 'not support char: {0}'.format(char)
        yield code, True, True
        
        # shift procedure
        if shift_on:
            yield api.VK_LSHIFT, False, True

    def func2codes(cls, num):
        try:
            code = cls.FUNC_CODE[num]
        except KeyError, err:
            assert False, 'Not support char: {0}'.format(num)
        else:
            yield code, True, True
