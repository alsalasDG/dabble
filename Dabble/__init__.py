""" Builds membrane protein systems """

__version__ = '2.7.7'
__author__ = 'Robin Betz'

import sys
import inspect

#=========================================================================

class DabbleError(Exception):
    """
    An error message aimed at users, without a really long traceback.
    """

    def __init__(self, msg):
        try:
            ln = sys.exc_info()[-1].tb_lineno
        except AttributeError:
            ln = inspect.currentframe().f_back.f_lineno

        print("\n\n\n{0.__name__} (line {1}): {2}\n".format(type(self), ln, msg))
        #self.args = "\n\n\n{0.__name__} (line {1}): {2}\n".format(type(self),
        #                                                          ln, msg)

#=========================================================================

from Dabble.builder import DabbleBuilder
from Dabble.fileutils import *
from Dabble.vmdsilencer import VmdSilencer

