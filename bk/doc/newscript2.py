#! /usr/bin/env python
#-*- coding: utf-8 -*-
#{#
"""Generate python script template file.
"""
#}#
"""
"""
__license__ = 'GNU General Public License Version 3'
__status__ = 'Production'
__author__ = 'TakEsxima'
__email__ = 'tak.esxima@gmail.com'
__credits__ = (__author__,)
__maintainer__ = '{0}<{1}>'.format(__author__, __email__)

#{#
__copyright__ = 'Copyright (C) 2012 - NOW, {0}'.format(__author__)
#}#

#{#
import time
"""
#}#
__copyright__ = 'Copyright (C) {{ year }} - NOW, {0}'.format(__author__)
#{#
"""
#}#

import os
import sys
import optparse

__DEBUG__ = False
try:
    __DEBUG__ = os.environ['DEBUG'].upper() == 'TRUE'
except KeyError:
    pass

ERRORCODE = 255

#{#
import os
import jinja2 as jinja

def mkdir_p(path):
    try:
        os.makedirs(path)
    except:
        pass

def write_new_scripts(paths, force=False):
    self_path = os.path.abspath(__file__)
    template_file = os.path.basename(self_path) 
    template_dir = os.path.dirname(self_path)

    loader = jinja.FileSystemLoader(template_dir)
    env = jinja.Environment(loader=loader)
    tmpl = env.get_template(template_file)    
    buf = tmpl.render(year=time.strftime('%Y'))
    
    for path in paths:
        if not force:
            if os.path.exists(path):
                ans = raw_input('{0}? (yes or no):'.format(path))
                if ans != 'yes':
                    print '  -> pass'
                    continue
        path = os.path.abspath(path)
        dirname = os.path.dirname(path)
        mkdir_p(dirname)
        with open(path, 'w+b') as ff:
            ff.write(buf)
            
_entry_point = write_new_scripts
#}# special code

#_entry_point = # setting callable object

# test code


def parse_args(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    parser = optparse.OptionParser()
    parser.add_option('--unittest', default=False, action='store_true')
    parser.add_option('--doctest',  default=False, action='store_true')
    parser.add_option('--test',     default=False, action='store_true')
    #{#
    parser.add_option('-f', '--force', default=False, action='store_true')
    #}#
    opts, args = parser.parse_args(argv)

    rargs = []
    kwds = {}
    unittest_ = opts.unittest
    doctest_ = opts.doctest

    #{#
    try:
        path = args
    except IndexError:
        parser.error('input a new file path.')
    else:
        rargs.append(path)
    
    kwds['force'] = opts.force
    #}#
    return rargs, kwds, unittest_, doctest_,

def main():
    args, kwds, unittest_, doctest_ = parse_args()

    # test code
    if doctest_ or unittest_:
        if doctest_:
            exc_doctest()        
        if unittest_:
            exc_unittest()
        sys.exit(0)
    
    # main code
    try:
        rc = _entry_point(*args, **kwds)
        sys.exit(rc)
    except BaseException, err:
        if __DEBUG__:
            raise
        else:
            print err
            sys.exit(ERRORCODE)

def exc_unittest():
    import unittest
    tests = []
    
    # add tests
    
    suite = unittest.TestSuite()
    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)
    return 0

def exc_doctest():
    import doctest
    doctest.testmod()
    return 0

if __name__ == '__main__':
    main()
