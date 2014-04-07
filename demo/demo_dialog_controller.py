#! /usr/bin/env python
#-*- coding: utf-8 -*-
try:
    import startup
except ImportError:
    pass

import guippy

import time
import itertools

def sleep():
    time.sleep(0.2)

def main():
    gp = guippy.Guippy()
    gp.catch('TkTopLevel', 'guippy')
    gp.active()
    gp.restore()


    def apply():
        gp.chase(19, 40, click=True)

    radios = {'test1': (40, 67),
              'test2': (97, 67),
              'test3': (160, 67),
              }
    checks = {'test1': (40, 93),
              'test2': (97, 93),
              'test3': (160, 93),
              }

    def setUp():
        init_radio = 'test1'
        apply()

        gp.chase(200, 67, click=True)# radio entry
        if gp.get_line() != init_radio:
            xx, yy = radios[init_radio]
            gp.chase(xx, yy, click=True)


        gp.chase(200, 93, click=True)# check entry
        check_line = gp.get_line()
        checks = map(lambda line: line.strip(), check_line.split(','))
        print checks
        for check_name in checks:
            if check_name == '':
                continue
            xx, yy = checks[check_name]
            gp.chase(xx, yy, click=True)

    checks_patterns = [nn for ii in range(1,4)
                       for nn in itertools.combinations(sorted(checks.items()), ii)]

    setUp()
    for radio_name, radio_coord in sorted(radios.items()):
        xx, yy = radio_coord
        sleep()
        gp.chase(xx, yy, click=True)

        for pattern in checks_patterns:
            for check_name, check_coord in pattern:
                xx, yy = check_coord
                sleep()
                gp.chase(xx, yy, click=True)

            apply()
            sleep()
            gp.chase(200, 67, click=True)# radio entry
            print gp.get_line()
            gp.chase(200, 93, click=True)# check entry
            print gp.get_line()
            sleep()

            for check_name, check_coord in pattern:
                xx, yy = check_coord
                sleep()
                gp.chase(xx, yy, click=True)




if __name__ == '__main__':
    main()
