import os
import sys

root = "C:\\Users\\User\\Music\\test folder"
path = os.path.join(root, "targetdirectory")

songs = []
song_location = []
for path, subdirs, files in os.walk(root):
    for name in files:
        songs.append(name)
        song_location.append(path)

##print songs

##print "\n\n\n\n ---- new stuff ----- \n\n\n\n"
##a = os.listdir(root)
##print a
