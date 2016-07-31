'''
Jam arrange: create executable version of current Jam arrange version
Author: Numstack (Pty) Ltd
Copyright 2016
Objective: Through the use of a simple GUI, identify mp3, wav, etc. files and arrange them accordingly in desired local storage folder.
'''

'''
Importing all necessary libraries
'''

from distutils.core import setup
import py2exe
import os
import os.path
from os import listdir
from os.path import isfile, join
import shutil
from tinytag import TinyTag
import wx

setup(
    options={
        "py2exe": {"dll_excludes": ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"]}},
    console=['JamarrangeGUI.py'])

'''
setup(console=['JamarrangeGUI.py'],
      options = {
          'py2exe': {
              'packages': ['os', 'os.path', 'listdir',
                           'isfile', 'join','shutil','wx','tinytag','TinyTag']
          }
      })
'''