import acoustid
import os.path
from os import listdir
from os.path import isfile, join

API_key = 'AxIwHZrcAz'
root = "home/victor/music/test folder"
path = os.path.join(root, "targetdirectory")
all_files_in_dir = []
all_files_dir = []
for path, subdirs, files in os.walk(root):
        for name in files:
            all_files_in_dir.append(name)
            all_files_dir.append(path)

aud_files = []
for i in range(len(all_files_in_dir)):
    if all_files_in_dir[i].endswith(('.mp3', '.wav', '.MP3', '.wma',
                                     '.WMA', '.WAV', '.mp4', '.MP4')) == True:
        # aud_files.append(all_files_dir[i] + "\\" + str(all_files_in_dir[i]))
        aud_files.apend(os.path.join(all_files_dir[i],str(all_files_in_dir[i])))
'''
data inaud_data array below:
0. path
1. artist
2. title
3. Acoustid recording_id
4. score
'''
aud_data = [[],[],[],[],[]]
for i in range(len(aud_files)):
    print aud_files[i]
    for score, recording_id, title, artist in acoustid.match(API_key,
                                                             aud_files[i]):
        aud_data[0].append(aud_files[i])
        aud_data[1].append(artist)
        aud_data[2].append(title)
        aud_data[3].append(recording_id)
        aud_data[4].append(score)
