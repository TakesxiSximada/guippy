#! /usr/bin/env python
#-*- coding: utf-8 -*-
import startup
import guippy
from guippy.error import Timeout

import time
import string
import random
import unittest
from unittest import TestCase

import six

# test
area = lambda target, base, width=10: (base-width) <= target <= (base+width)

LOOP_MAX = 0xFFF
ASCII_CHARS = string.ascii_letters + string.digits + string.punctuation

class GuippyTest(TestCase):
    NOTEPAD = u'Notepad', u'無題 - メモ帳'

    def active_notepad(self):
        try:
            win = guippy.Window()
            win.catch(*self.NOTEPAD)
            win.active()
        except Timeout:
            kbd = guippy.Keyboard()
            kbd.windows('r')
            kbd.enter('notepad')
            time.sleep(1)

class NormalizeTest(GuippyTest):
    def test_normalize_denormalize(self):
        from guippy.shortcut import Normalizer, Denormalizer

        def _func(normalize, denormalize, num):
            normal = normalize(num)
            ans = denormalize(normal)
            self.assert_(area(ans, num, 1),
                         '{0} -> {1} -> {2}'.format(num, normal, ans))

        for ii in range(LOOP_MAX):
            _func(Normalizer.xx, Denormalizer.xx, ii)
            _func(Normalizer.yy, Denormalizer.yy, ii)

class WindowTest(GuippyTest):
    def setUp(self):
        self.win = guippy.Window()

    def test_get_window(self):
        self.active_notepad()
        hwnd_aa = self.win.get_window()
        guippy.Keyboard.windows('d')
        hwnd_bb = self.win.get_window(*self.NOTEPAD)
        self.assertEqual(hwnd_aa, hwnd_bb)
        guippy.Keyboard.windows('d')

    def test_catch(self):
        self.active_notepad()
        self.win.catch()
        hwnd_aa = self.win.hwnd
        guippy.Keyboard.windows('d')
        self.win.catch(*self.NOTEPAD)
        hwnd_bb = self.win.hwnd
        self.assertEqual(hwnd_aa, hwnd_bb)
        guippy.Keyboard.windows('d')

    def _test_active(self):
        self.active_notepad()
        self.win.active()
        self.win.catch()
        hwnd_aa = self.win.hwnd
        guippy.Keyboard.windows('d')

        hwnd_bb = self.win.get_window()
        self.assertEqual(hwnd_aa, hwnd_bb)
        guippy.Keyboard.windows('d')

    def test_rect(self):
        self.win.get_rect(True)
        self.win.get_rect(False)

    def test_get_popup(self):
        self.win.get_popup()

    def test_get_child(self):
        self.win.get_child()

    def test_cname_wname(self):
        win = guippy.Window()
        win.catch()
        now_hwnd = win.hwnd
        cname = win.get_cname()
        wname = win.get_wname()
        new_hwnd = guippy.Window.get_window(cname, wname)
        self.assertEqual(now_hwnd, new_hwnd)

class WindowSizeTest(GuippyTest):
    MARGIN = 19
    SIZE_PATTERN = (ii for ii in range(100, 200))
    MESSAGE = 'now = {0}, before = {1}'

    def check(self, now, before):
        _inf = before - self.MARGIN
        _sup = before + self.MARGIN
        self.assert_(_inf < now < _sup, self.MESSAGE.format(now, before))

    def _test_width(self):
        win = guippy.Window()
        win.catch()
        org = win.width
        for ii in self.SIZE_PATTERN:
            win.width = ii
            self.check(win.width, ii)
        win.width = org

    def _test_height(self):
        win = guippy.Window()
        win.catch()
        org = win.height
        for ii in self.SIZE_PATTERN:
            win.height = ii
            self.check(win.height, ii)
        win.height = org

class WindowMoveTest(GuippyTest):
    def setUp(self):
        mouse = guippy.Mouse()
        mouse.jump(1, 1)

    def test_move(self):
        self.active_notepad()
        win = guippy.Window()
        win.catch()
        org = win.get_rect(normalize=False)
        for ii in range(10, 100):
            top = ii
            left = int(top * 1.5)

            win.move(left, top)
            now = win.get_rect(normalize=False)

            self.assertEqual(left, now.left)
            self.assertEqual(top, now.top)

        win.move(org.left, org.top)
        win.close()

class KeyboardTest(GuippyTest):
    def _test_punch(self):
        guippy.Keyboard.punch('#' + string.printable)

    def test_alt(self):
        guippy.Keyboard.alt()

class KeycodeTest(GuippyTest):
    def test_char2codes(self):
        gen = guippy.keyboard.Keycode.char2codes('C')
        self.assertEqual((160, True, False), six.next(gen)) # push shift
        self.assertEqual((67, True, True), six.next(gen))   # push and release 'C'
        self.assertEqual((160, False, True), six.next(gen)) # release shift

        gen = guippy.keyboard.Keycode.char2codes('c')
        self.assertEqual((67, True, True), six.next(gen))   # push and release 'C'
        try:
            codes = six.next(gen)
        except StopIteration:
            pass # OK
        else:
            self.fail(codes)

    def test_func2codes(self):
        gen = guippy.keyboard.Keycode.func2codes(1)
        self.assertEqual((112, True, True), six.next(gen))

class ClipboardTest(GuippyTest):
    def test_test(self):
        data = ASCII_CHARS
        guippy.Clipboard.set(data)
        buf = guippy.Clipboard.get()
        self.assertEqual(data, buf)


class MouseTest(GuippyTest):
    def test_now(self):
        ms = guippy.Mouse()
        for ii in range(LOOP_MAX):
            self.assertEqual(ms.now(), ms.now())
            self.assertEqual(ms.now(True), ms.now(True))
            self.assertEqual(ms.now(False), ms.now(False))

    def jumping(self, ms, normalize, absolute,
                      jump_coord, prediction_coord, now_coord, width):
        fmt = 'now={0}, prediction={1}'
        for ii in range(LOOP_MAX):
            xx, yy = jump_coord()
            ans_xx, ans_yy = prediction_coord(xx, yy)
            ms.jump(xx, yy, normalize, absolute)
            now_xx, now_yy = now_coord(xx, yy)
            #self.assert_(area(now_xx, ans_xx, width),
            #                 fmt.format(now_xx, ans_xx))
            #self.assert_(area(now_yy, ans_yy, width),
            #                 fmt.format(now_yy, ans_yy))

    def test_jump_normalize_absolute(self):
        ms = guippy.Mouse()
        normalize = True
        absolute = True

        def jump_coord():
            return random.randint(1, 300), random.randint(1, 300)

        def prediction_coord(xx, yy):
            return xx, yy

        def now_coord(xx, yy):
            return ms.now()

        width = 100
        self.jumping(ms, normalize, absolute,
                     jump_coord, prediction_coord, now_coord, width)

    def test_jump_unnormalize_unabsolute(self):
        from guippy.shortcut import Display
        ms = guippy.Mouse()
        normalize = False
        absolute = False

        def jump_coord():
            _ = lambda n: random.randint(-n, n)
            return _(Display.XMAX), _(Display.YMAX)

        def prediction_coord(xx, yy):
            now_xx, now_yy = ms.now(normalize)
            return now_xx + xx, now_yy + yy

        def now_coord(*args, **kwds):
            return ms.now(normalize)
        width = 10
        self.jumping(ms, normalize, absolute,
                     jump_coord, prediction_coord, now_coord, width)


    def test_point(self):
        mouse = guippy.Mouse()
        mouse.jump(23, 45)
        mouse.point(34,63)

if __name__ == '__main__':
    unittest.main()
