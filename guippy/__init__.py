#-*- coding: utf-8 -*-
"""Graphical User Interfaces Procedures for PYthon.

 Guippy emulate various operations of computer users. It provides the ability for
emulate keyboards, mouses, window system, and clipboards. By using this, you can
run your computer automatically.

 This is a Pyhon 3rd party library. Written in pure Python. You need to Python
programming, but it is very easy to use. And you can easily and safely install.

example.

   >>> import guippy
   >>> gp = guippy.Guippy()
   >>> gp.catch()
   >>> gp.punch()
   >>> gp.close()

Let's get started.
"""

__version__ = '$Revision$'
__author__ = 'tak.esxima'
__maintainer__ = __author__
__email__ = '{0}@gmail.com'.format(__author__)
__credits__ = (__author__, )
__copyright__ = 'Copyright (c) 2012 {0}'.format(__author__)
__license__ = 'GNU General Public License Version 3'
__status__ = 'Development'

import mouse
import keyboard
import window
import clipboard
import api
from .guippy import *  # import all objects in guippy.
from .mouse import Mouse
from .keyboard import Keyboard
from .window import Window
from .clipboard import Clipboard

__all__ = (
    # in guippy module
    'Guippy',
    # in other modules
    'mouse', 'keyboard', 'window', 'clipboard',
    'Mouse', 'Keyboard', 'Window', 'Clipboard',
    'api'
    )

