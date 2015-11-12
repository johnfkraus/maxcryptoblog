"""All settings in this demo are written to settings_generated.py

In a real project, you could start by copying the settings_generated.py file
over this file.
"""
import sys
import os

try:
    from allauthdemo.settings_generated import *
except ImportError:
    sys.stderr.write("ERROR: No generated settings found. Please run 'make configure' first.\n\n")
    sys.exit(1)


try:
    from allauthdemo.settings_email import *
except ImportError:
    sys.stderr.write("ERROR: No email settings found. Please run 'make configure' first.\n\n")
    sys.exit(1)


try:
    from allauthdemo.settings_verification import *
except ImportError:
    sys.stderr.write("ERROR: No verification settings found. Please run 'make configure' first.\n\n")
    sys.exit(1)


try:
    from allauthdemo.settings_cryptoblog import *
except ImportError:
    sys.stderr.write("ERROR: No cryptoblog settings found. Please run 'make configure' first.\n\n")
    sys.exit(1)
