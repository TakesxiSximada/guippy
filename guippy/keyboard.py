#-*- coding: utf-8 -*-
"""To emulate keyboard.

"""

class KeyboardCore(object):
    def push(self):
        """Push the key.
        """
        pass
    
    def release(self):
        """Release the key.
        """
        pass

    def put(self):
        """Input a character.
        """
        pass

    def punch(self):
        """Input messages.
        """
        pass

class KeyboardElement(KeyboardCore):
    def F(self, num):
        """Type the function key.
         Avariable num is integer. It is processing after convert integer.
        If can not convert integer then will raise TypeError.
        """
        pass

    def cltr(self):
        """Type the control key."""
        pass

    def alt(self):
        """Type the alt key."""
        pass

    def fn(self):
        """Type the fn key."""
        pass

    def shift(self):
        """Type the shift key."""
        pass

    def capslock(self):
        """Type the caps lock key."""
        pass

    def tab(self):
        """Type the tab key."""
        pass

    def lang(self):
        """Tpe a language key.
         Use to switch between input languages. Change language is depends on a
        respectively system.
        """
        pass

    def space(self):
        pass

    def windows(self):
        pass

    def mac(self):
        pass

    def up(self):
        pass

    def up(self):
        pass

    def down(self):
        pass

    def right(self):
        pass

    def left(self):
        pass

    def enter(self):
        pass

    def backspace(self):
        pass
    
    def insert(self):
        pass
    
    def delete(self):
        pass

    def menu(self):
        pass

    def printscreen(self):
        pass

    def numlock(self):
        pass

    def pause(self):
        pass

    def home(self):
        pass

    def end(self):
        pass

    def page_up(self):
        pass

    def page_down(self):
        pass

    def escape(self):
        pass

    def convert(self):
        pass

    def nonconvert(self):
        pass

    def kana(self):
        pass


class Keyboard(KeyboardElement):
    def comb(self):
        pass

    def mark_line(self):
        pass

    def mark_all(self):
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
