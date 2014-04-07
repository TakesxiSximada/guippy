#! /usr/bin/env python
#-*- coding: utf-8 -*-
try:
    import startup
except ImportError:
    pass

import guippy

import unittest
import time
import itertools

class DemoDialogTest(unittest.TestCase):
    INIT_RADIO = 'test1'
    RADIOS = {'test1': (40, 67),
              'test2': (97, 67),
              'test3': (160, 67),
              }
    CHECKS = {'test1': (40, 93),
              'test2': (97, 93),
              'test3': (160, 93),
              }

    APPLY = 19, 40
    RADIO_ENTRY = 200, 67
    CHECK_ENTRY = 200, 93

    SLEEP = 0.2

    def __init__(self, *args, **kwds):
        unittest.TestCase.__init__(self, *args, **kwds)
        gp = guippy.Guippy()
        gp.catch('TkTopLevel', 'guippy')
        gp.restore()
        gp.active()
        self.gp = gp

    def sleep(self):
        time.sleep(self.SLEEP)

    def apply(self):
        xx, yy = self.APPLY
        self.gp.chase(xx, yy, click=True)

    def get_radio_value(self):
        xx, yy = self.RADIO_ENTRY
        self.gp.chase(xx, yy, click=True)# check entry
        line =  self.gp.get_line()
        return line.strip()

    def get_check_values(self):
        xx, yy = self.CHECK_ENTRY
        self.gp.chase(xx, yy, click=True)# check entry
        line = self.gp.get_line()
        for name in map(lambda line: line.strip(), line.split(',')):
            if name != '':
                yield name

    def setUp(self):
        self.apply()
        if self.get_radio_value() != '':
            xx, yy = self.RADIOS[self.INIT_RADIO]
            self.gp.chase(xx, yy, click=True)

        for name in self.get_check_values():
            xx, yy = self.CHECKS[name]
            self.gp.chase(xx, yy, click=True)

    def test_all_pattern(self):

        check_patterns = [ptn for ii in range(1, len(self.CHECKS))
                          for ptn in itertools.combinations(sorted(self.CHECKS.items()), ii)]

        for radio_name, radio_coord in sorted(self.RADIOS.items()):
            xx, yy = radio_coord
            self.gp.chase(xx, yy, click=True)

            for ptn in check_patterns:
                check_names = sorted([name for name, _tmp in ptn])
                for check_name, check_coord in ptn:
                    xx, yy = check_coord
                    self.gp.chase(xx, yy, click=True)

                self.sleep()
                self.apply()
                self.sleep()
                self.assertEqual(radio_name, self.get_radio_value())
                now_check_names = [name for name in self.get_check_values()]
                self.assertEqual(check_names, now_check_names)

                for check_name, check_coord in ptn:
                    xx, yy = check_coord
                    self.gp.chase(xx, yy, click=True)

if __name__ == '__main__':
    unittest.main()
