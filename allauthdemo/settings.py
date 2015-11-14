""" you could copy the settings_generated.py file over this file. """
import sys
# import os
import allauthdemo.utils

try:
    from allauthdemo.settings_secret import *
except ImportError:
    sys.stderr.write("ERROR: No secret settings found. \n\n")
    sys.exit(1)


try:
    from allauthdemo.settings_generated_max import *
except ImportError:
    sys.stderr.write("ERROR: No generated settings found. Please run 'make configure' first.\n\n")
    sys.exit(1)


try:
    from allauthdemo.settings_email import *
except ImportError:
    sys.stderr.write("ERROR: No email settings found. \n\n")
    sys.exit(1)


try:
    from allauthdemo.settings_verification import *
except ImportError:
    sys.stderr.write("ERROR: No verification settings found.\n\n")
    sys.exit(1)


try:
    from allauthdemo.settings_cryptoblog import *
except ImportError:
    sys.stderr.write("ERROR: No cryptoblog settings found. \n\n")
    sys.exit(1)


try:
    from allauthdemo.settings_local import *
except ImportError:
    sys.stderr.write("WARNING: No local settings found.\n\n")
    pass

print(allauthdemo.utils.module_path(), 'line', allauthdemo.utils.lineno(), 'DEBUG =', DEBUG)
