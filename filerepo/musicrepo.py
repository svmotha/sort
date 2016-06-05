'''
Identify mp3, wav, etc. files and arange them accordingly
in desired local storage folder
'''

import eyed3
import os
import os.path
from os import listdir
from os.path import isfile, join
import shutil

target = "C:\\Users\\User\\Music\\rAY"
'''
for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames
                     if f.lower().endswith((".mp3", ".wav"))]:
        print os.path.join(dirpath, filename)
'''


all_files_in_dir = os.listdir(target)
audio_files = []
audio_file_deets = [[],[],[],[],[],[]] # 6 details for now
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
        if current_audiofile == None:
            files_not_parsed.append(temp)

indexes = []
for i in range(len(audio_file_deets[0])):
    if audio_file_deets[i] != None:
        pass
    if audio_file_deets[i] != None:
        indexes.append([])
        for j in range(len(audio_file_deets[0])):
            if audio_file_deets[i] == audio_file_deets[j]:
                pass
