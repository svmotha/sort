import os
import os.path
from os import listdir
from os.path import isfile, join
# -*- coding: utf8 -*-
'''
NB: Not part of the code, just used to model sorting as practice

Test module for sorting an item just once in a list even if it
occurs more than once. This will help with:
    Making sure we know which artist name occursmore than once
    in the list of artists.
'''
# l = [1, 2, 3, 4, 5, 6, 1, 6, 1, 2]
# lis_o = []
#
# for i in range(len(l)):
#     a = [x for x, val in enumerate(l) if val == l[i]]
#     if len(a) > 1:
#         if l[i] in lis_o:
#             pass
#         else:
#             lis_o.append(l[i])
#
#     elif len(a) == 1:
#         lis_o.append(l[i])

'''
fixing os.walk filename capturing for files that contain ' and " in the file names.
'''

def replace_special_chars_files(temp):
    reserved_chars = ['"',"'"]
    for i in range(len(reserved_chars)):
        if reserved_chars[i] in temp:
            temp = temp.replace(reserved_chars[i],' ')
    return temp

root = 'C:\\Users\\User\\Music\\test folder'
path = os.path.join(root, "targetdirectory")
all_files_in_dir = []
all_files_dir = []

for path, subdirs, files in os.walk(unicode(root, 'utf-8')):
    print files
    for name in files:
        if isinstance(name, str) == True:
            all_files_in_dir.append(replace_special_chars_files(name))
#            print name
            all_files_dir.append(path)


