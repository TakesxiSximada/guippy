#! /usr/bin/env python
#-*- coding: utf-8 -*-
import unittest
import guippy




class Test(unittest.TestCase):
    def test_test(self):
        pass

class ImportTest(Test):
    def test_imports(self):
        import guippy
        import guippy.api
        import guippy.clipboard
        import guippy.decorator
        import guippy.error
        import guippy.keyboard
        import guippy.mouse
        import guippy.operator
        import guippy.shortcut
        import guippy.util
        import guippy.window

class KeyboardTest(Test):
    def test_test(self):
        import guippy.keyboard
        keyboard = guippy.keyboard.Keyboard()


class ClipboardTest(Test):
    def test_clipboard(self):
        import guippy.clipboard
        guippy.clipboard.Clipboard.get()

if __name__ == '__main__':
    unittest.main()
