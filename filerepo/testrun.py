'''
Importing all necessary libraries
'''
import os
import os.path
from os import listdir
from os.path import isfile, join
import shutil
from tinytag import TinyTag


target = "/home/victor/Music"
'''
finding all files in dir and subdir
'''
root = target
path = os.path.join(root, "targetdirectory")
all_files_in_dir = []
all_files_dir = []
for path, subdirs, files in os.walk(root):
    for name in files:
        all_files_in_dir.append(str(name))
        all_files_dir.append(path)

audio_files = []
audio_file_deets = [[], [], [], [], [], [], []]
files_not_parsed = []
count = 0
for i in range(len(all_files_in_dir)):
    if all_files_in_dir[i].endswith(('.mp3', '.wav', '.MP3', '.wma', '.WMA', '.WAV', '.mp4', '.MP4')) == True:
        temp = all_files_dir[i] + "/" + str(all_files_in_dir[i])
        current_audiofile = TinyTag.get(temp)
        if current_audiofile is not None:
            curr_artist = current_audiofile.artist
            if curr_artist == '':
                curr_artist = None
                audio_file_deets[0].append(curr_artist)
            else:
                audio_file_deets[0].append(curr_artist)
            audio_file_deets[1].append(current_audiofile.title)
            audio_file_deets[2].append(current_audiofile.album)
            audio_file_deets[3].append(temp)
            audio_file_deets[4].append(current_audiofile.track)
            audio_file_deets[5].append(current_audiofile.track_total)
            audio_file_deets[6].append(count)
            count = count + 1
            audio_files.append(all_files_in_dir[i])
        if current_audiofile == None:
            files_not_parsed.append(temp)
    # return audio_file_deets, files_not_parsed, all_files_in_dir, all_files_dir

audio_details = [audio_file_deets,files_not_parsed,all_files_in_dir,all_files_dir]

# ---------------------------------------------------------------------------------------------------

artist_names = []
for i in range(len(audio_file_deets[0])):
    '''
                        NB: Attention!!!!!!!!!!!
    Unicode testing function must enter here once completed:
    isinstance(a, unicode)
    '''
    if audio_file_deets[0][i] is not None:
        artist_names.append(str(audio_file_deets[0][i].strip()
                                .encode('utf-8')))
    if audio_file_deets[0][i] is None:
        artist_names.append(i)

folder_titles = []
unknown_songs = [[], []]

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
            unknown_songs[0].append(artist_names[i])
            unknown_songs[1].append(audio_file_deets[3][i])

handle_files = [artist_names, folder_titles, unknown_songs]
