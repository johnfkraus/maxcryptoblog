# allauthdemo/utils.py
import os
import inspect
import sys
from inspect import getsourcefile
from os.path import abspath


"""Handy utils for config"""


def contents(*names):
    """Return string contents from first matching named environment variable
    or file.

    Each name in names is checked first against an environment variable then
    a file. An Exception is raised if nothing matches.
    """
    for name in names:
        if name in os.environ:
            return os.environ[name]

        else:
            name = os.path.expanduser(name)
            if os.path.isfile(name):
                with open(name) as src:
                    return src.read().strip()

    raise Exception("Unresolved content: " + ', '.join(names))


def lineno():
    """ Returns the current line number in the program.
    Danny Yoo (dyoo@hkn.eecs.berkeley.edu).
    Requires import inspect.
    """
    return inspect.currentframe().f_back.f_lineno


def we_are_frozen():
    # All of the modules are built-in to the interpreter, e.g., by py2exe
    return hasattr(sys, "frozen")


def module_path():
    # encoding = sys.getfilesystemencoding()
    if we_are_frozen():
        return os.path.dirname(sys.executable)
    return os.path.dirname(__file__)


def get_source_file():
    abspath(getsourcefile(lambda: 0))
