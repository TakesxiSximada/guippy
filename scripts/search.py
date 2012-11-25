#-*- coding: utf-8 -*-
import os
import re

CLASS_OR_DEF = re.compile('^\s*(class|def)\s.*')
for root, dirs, files in os.walk(os.getcwd()):
    for filename in files:
        print '{0}'.format(filename)
        print '='*len(filename)
        with open(filename, 'rb') as ff:
            for line in ff:
                if CLASS_OR_DEF.match(line):
                    print line,
