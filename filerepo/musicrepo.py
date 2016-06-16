'''
Jam arrange - Official Api
                            Objective:
-----------------------------------------------------------------------------
Identify mp3, wav, etc. files and arange them accordingly
in desired local storage folder
-----------------------------------------------------------------------------
'''
#------------------------------------------------------------------------------
'''
Importing all necessary libraries
'''

import eyed3
import os
import os.path
from os import listdir
from os.path import isfile, join
import shutil

#------------------------------------------------------------------------------
'''
Collect audio files' details in chosen directory
'''

target = "C:\\Users\\User\\Music\\rAY"
all_files_in_dir = os.listdir(target)
audio_files = []
                        # Extracted Audio file details 
# 1. Artist
# 2. Title (song name)
# 3. Album title
# 4. Path on local storage
# 5. Track number
# 6. Total number of tracks on specific album
audio_file_deets = [[],[],[],[],[],[]]
files_not_parsed = []
for i in range(len(all_files_in_dir)):
    if all_files_in_dir[i].endswith(('.mp3', '.wav')) == True:
        temp = target + '\\' + all_files_in_dir[i]
        current_audiofile = eyed3.load(temp)
        if current_audiofile != None:
            audio_file_deets[0].append(current_audiofile.tag.artist)
            audio_file_deets[1].append(current_audiofile.tag.title)
            audio_file_deets[2].append(current_audiofile.tag.album)
            audio_file_deets[3].append(temp)
            temp = current_audiofile.tag.track_num
            audio_file_deets[4].append(temp[0])
            audio_file_deets[5].append(temp[1])
            audio_files.append(all_files_in_dir[i])
        if current_audiofile == None:
            files_not_parsed.append(temp)

#------------------------------------------------------------------------------
'''
Making a list of all known artist names to use later when creating song
storage folders.
'''


artist_names = []

# Create artist name folders: os.mkdir(’mydir’)
for i in range(len(audio_file_deets[0])):
    if audio_file_deets[0][i] != None:
        artist_names.append(str(audio_file_deets[0][i].strip()))
    if audio_file_deets[0][i] == None:
        artist_names.append(i)

folder_titles = []
unknown_songs = []

for i in range(len(artist_names)):
    temp = [x for x, val in enumerate(artist_names)
            if val == artist_names[i]]
    if len(temp) > 1:
        if artist_names[i] in folder_titles:
            pass
        else:
            folder_titles.append(artist_names[i])
    elif len(temp) == 1:
        temp2 = isinstance(artist_names[i], str)
        if temp2 == True:
            folder_titles.append(artist_names[i])
        else:
            unknown_songs.append(artist_names[i])
##            unknown_songs.append(audio_files[i])

#------------------------------------------------------------------------------
'''
NB: Not part of the code, just used to model sorting as practice

Test module for sorting an item just once in a list even if it
occurs more than once. This will help with:
    Making sure we know which artist name occursmore than once
    in the list of artists.
'''
l = [1,2,3,4,5,6,1,6,1,2]
lis_o = []

for i in range(len(l)):
    a = [x for x, val in enumerate(l) if val == l[i]]
    if len(a) > 1:
        if l[i] in lis_o:
            pass
        else:
            lis_o.append(l[i])
        
    elif len(a) == 1:
        lis_o.append(l[i])

#------------------------------------------------------------------------------
'''
Make folders for all songs with known artist meta data.
'''
moveto = os.path.join(target, 'Arranged files')
os.mkdir(os.path.join(target, 'Arranged files'))

for i in range(len(folder_titles)):
    os.mkdir(os.path.join(moveto , folder_titles[i]))



#------------------------------------------------------------------------------
