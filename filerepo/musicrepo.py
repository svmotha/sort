'''
Jam arrange: Arrangement algorithm
Author: Numstack (Pty) Ltd
Copyright 2016
Objective: Identify mp3, wav, etc. files and arange them accordingly in desired local storage folder.
'''

'''
Importing all necessary libraries
'''
import os
import os.path
from os import listdir
from os.path import isfile, join
import shutil
from tinytag import TinyTag

'''
Repalcing special characters in file name
'''

def replace_special_chars_files(temp):
    reserved_chars = ['"',"'"]
    for i in range(len(reserved_chars)):
        if reserved_chars[i] in temp:
            temp = temp.replace(reserved_chars[i],' ')
    return temp

'''
Repalcing special characters in a dir name
'''

def replace_special_chars(temp):
    reserved_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']  # see tutorial for explanation
    if temp is not None:
        for i in range(len(reserved_chars)):
            if reserved_chars[i] in temp:
                temp = temp.replace(reserved_chars[i], ' ')
    else:
        pass
    return temp

'''
Collect audio files' details in chosen directory
'''

def collect_audio(target):
    '''
    finding all files in dir and subdir
    '''
    root = target
    path = os.path.join(root, "targetdirectory")
    all_files_in_dir = []
    all_files_dir = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            all_files_in_dir.append(replace_special_chars(str(name)))
            all_files_dir.append(path)
    audio_files = []
    '''
                            Extracted Audio file details
    1. Artist
    2. Title (song name)
    3. Album title
    4. Path on local storage
    5. Track number
    6. Total number of tracks on specific album
    7. Tracking id generation
    '''
    audio_file_deets = [[], [], [], [], [], [], []]
    files_not_parsed = []
    count = 0
    for i in range(len(all_files_in_dir)):
        if all_files_in_dir[i].endswith(('.mp3', '.wav', '.MP3', '.wma', '.WMA', '.WAV', '.mp4', '.MP4')) == True:
            temp = os.path.join(all_files_dir[i],str(all_files_in_dir[i]))
            current_audiofile = TinyTag.get(temp)
            if current_audiofile is not None:
                curr_artist = replace_special_chars(current_audiofile.artist)
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
    return audio_file_deets, files_not_parsed, all_files_in_dir, all_files_dir


'''
Making a list of all known artist names to use later when creating song
storage folders.
'''

def music_handling(audio_file_deets):
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
    unknown_songs = [[],[]]

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

    return artist_names, folder_titles, unknown_songs



'''
Make folders for all songs with known artist meta data.
'''

def making_arranged_dir(target, folder_titles):
    moveto = os.path.join(target, 'Arranged files')
    os.mkdir(os.path.join(target, 'Arranged files'))
    new_dirs = []
    for i in range(len(folder_titles)):
        temp = os.path.join(moveto, folder_titles[i])
        if temp.strip().lower() not in new_dirs:
            os.mkdir(temp)
            new_dirs.append(temp.strip())
    unknown_dir = os.path.join(moveto, 'Unknown artists').strip()
    os.mkdir(os.path.join(moveto, 'Unknown artists'))
    return moveto, new_dirs, unknown_dir

'''
Move files to respective folders
'''

def movefiles():
    pass

'''
Delete unknown folder if no unknown songs found
'''
def clean_unknown_folder(unknown_songs, unknown_dir):
    if unknown_songs == [[],[]]:
        shutil.rmtree(unknown_dir)
    else:
        pass

'''
Delete files while testing
'''

def delete_files(moveto):
    user_input = raw_input('''would you like to delete newly created
                           files: [y/n]\n''')
    if user_input.strip() == 'y':
        shutil.rmtree(moveto)

'''
copy all files to right places
'''

def copy_to_arranged(new_dirs, song_locations, folder_titles, artist_names, unknown_dir):
    for i in range(len(artist_names)):
        for j in range(len(folder_titles)):
            str_test = isinstance(artist_names[i], str)
            if (artist_names[i] == folder_titles[j]) and (str_test == True):
                shutil.copy(song_locations[i].strip(), new_dirs[j].strip())

'''
Copy all files that need meta data identification, to a new repository.
Allowing the audio fingerprinting process to be simplified and centrallised,
'''

def copy_all_unknowns(unknown_songs, unknown_dir):
    for i in range(len(unknown_songs[1])):
        shutil.copy(unknown_songs[1][i], unknown_dir)
        
'''
Rename files: If tags i.e. meta data doesn't match visible file name on pc
it can be difficult for the user to know what song they are looking at.
'''

def rename_files():
    pass

'''
MAIN CODE AND MAIN FUNCTION
'''

if __name__ == "__main__":
    target = "/Users/victor/Music/test"
    audio_details = collect_audio(target)
    handle_files = music_handling(audio_details[0])
    create_folders = making_arranged_dir(target, handle_files[1])
    copy_to_arranged(create_folders[1], audio_details[0][3], handle_files[1], handle_files[0], create_folders[2])
    copy_all_unknowns(handle_files[2], create_folders[2])
    clean_arranged_folder = clean_unknown_folder(handle_files[2], create_folders[2])

##    delete_arrangement = delete_files(create_folders[0]) #Delete demo files
