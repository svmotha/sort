'''
|--------------------------------------------------------------------------
|
| Jam arrange: GUI linked to arrangement algorithm
| Author: Victor Motha
| Copyright 2016
| Objective: Sort through audio files and sort them according to artist names.
| Current stable version: 0.0.4
|
'''

'''
|--------------------------------------------------------------------------
| Importing built-in and External packages:
|--------------------------------------------------------------------------
|
| This is where we import all our built-in python packages, such as os,
| and shutil to allow for access to OS dir and file manipulation. We
| also import the TinyTag external package to access file meta-data.
|
'''
import os
import os.path
# from os import listdir
from os.path import join  # isfile
import shutil
from tinytag import TinyTag

'''
|--------------------------------------------------------------------------
| Arranging algorithm:
|--------------------------------------------------------------------------
|
| This is where we call all functions linked to arranging algorithm 
| through the - Arranger - class.
|
'''
class Arranger(object):
    """Arranging algorithm for jamarrange."""

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    '''
    |--------------------------------------------------------------------------
    | Repalcing special characters: Dir names
    |--------------------------------------------------------------------------
    |
    | This is where we replace all special characters when reading dir names
    | to ensure python can evaluate through these files as strings and 
    | escape these characters.
    |
    '''
    def replace_special_chars_files(self, temp):
        reserved_chars = ['"',"'"]
        for i in range(len(reserved_chars)):
            if reserved_chars[i] in temp:
                temp = temp.replace(reserved_chars[i],' ')
        return temp

    '''
    |--------------------------------------------------------------------------
    | Repalcing special characters: File names
    |--------------------------------------------------------------------------
    |
    | This is where we replace all special characters when reading file names
    | to ensure python can evaluate through these files as strings and  
    | escape these characters. This is also to ensure we conform to 
    | OS directory naming conventions as is highlighted in the 
    | - directory_handling - tutorial.
    |
    '''
    def replace_special_chars(self, temp):
        reserved_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']  # see tutorial for explanation
        if temp is not None:
            for i in range(len(reserved_chars)):
                if reserved_chars[i] in temp:
                    temp = temp.replace(reserved_chars[i], ' ')
        else:
            pass
        return temp

    '''
    |--------------------------------------------------------------------------
    | Meta-data collection:
    |--------------------------------------------------------------------------
    |
    | This is where we collect all audio file details in user selected 
    | directory.
    |
    '''
    def collect_audio(self, target):
        '''
        |--------------------------------------------------------------------------
        | Find all files:
        |--------------------------------------------------------------------------
        |
        | This is where we find all files in dir and subdirs.
        |
        '''
        root = target
        path = os.path.join(root, "targetdirectory")
        all_files_in_dir = []
        all_files_dir = []
        for path, subdirs, files in os.walk(root):
            for name in files:
                all_files_in_dir.append(self.replace_special_chars(str(name)))
                all_files_dir.append(path)
        audio_files = []
        '''
        |--------------------------------------------------------------------------
        | Extracted Audio file details:
        |--------------------------------------------------------------------------
        |
        | This is the data we collect in order as listed below:
        | 1. Artist
        | 2. Title (song name)
        | 3. Album title
        | 4. Path on local storage
        | 5. Track number
        | 6. Total number of tracks on specific album
        | 7. Tracking id generation
        |
        '''
        audio_file_deets = [[], [], [], [], [], [], []]
        files_not_parsed = []
        total_files_parsed = 0 # Keeping track of total number of media files in dir
        count = 0
        for i in range(len(all_files_in_dir)):
            if all_files_in_dir[i].endswith(('.mp3', '.wav', '.MP3', '.wma', '.WMA', '.WAV', '.mp4', '.MP4')) == True:
                total_files_parsed += 1 # counting each find media file
                temp = os.path.join(all_files_dir[i],str(all_files_in_dir[i]))
                current_audiofile = TinyTag.get(temp)
                if current_audiofile is not None:
                    curr_artist = self.replace_special_chars(current_audiofile.artist)
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
        return audio_file_deets, files_not_parsed, all_files_in_dir, all_files_dir, total_files_parsed

    '''
    |--------------------------------------------------------------------------
    | Meta-data sorting:
    |--------------------------------------------------------------------------
    |
    | This is where we make a list of all known meta-data, for later use 
    | when creating song storage folders.
    |
    '''
    def music_handling(self, audio_file_deets):
        artist_names = []
        for i in range(len(audio_file_deets[0])):
            '''
            |--------------------------------------------------------------------------
            | Potential Bug: Unicode Testing Required
            |--------------------------------------------------------------------------
            |
            | Unicode testing function must enter here once completed, e.g: 
            | isinstance(a, unicode)
            |
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
    |--------------------------------------------------------------------------
    | Make Artist Directories:
    |--------------------------------------------------------------------------
    |
    | This is where we make folders for all songs with known artist meta data.
    |
    '''
    def making_arranged_dir(self, target, folder_titles):
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
    |--------------------------------------------------------------------------
    | Move Files To Respective Directories:
    |--------------------------------------------------------------------------
    |
    | This is where we move files to respective folders.
    |
    | Note: This function is currently NOT created and a copying function is  
    | preferrd, as there isn't an undo function, for buggy moves.
    |
    '''
    def movefiles(self):
        pass

    '''
    |--------------------------------------------------------------------------
    | Delete Unknown Folder:
    |--------------------------------------------------------------------------
    |
    | This is where we delete unknown folder if no unknown songs found.
    |
    '''
    def clean_unknown_folder(self, unknown_songs, unknown_dir):
        if unknown_songs == [[],[]]:
            shutil.rmtree(unknown_dir)
        else:
            pass

    '''
    |--------------------------------------------------------------------------
    | Delete Testing Folders:
    |--------------------------------------------------------------------------
    |
    | This is where we delete files while testing.
    |
    | Note: This function works through the python console, and can be deleted
    | before packaging.
    |
    '''
    def delete_files(self, moveto):
        user_input = raw_input('''would you like to delete newly created
                               files: [y/n]\n''')
        if user_input.strip() == 'y':
            shutil.rmtree(moveto)

    '''
    |--------------------------------------------------------------------------
    | Copy Files To Directories:
    |--------------------------------------------------------------------------
    |
    | This is where we copy all files to corresponding artist folders.
    |
    '''
    def copy_to_arranged(self, new_dirs, song_locations, folder_titles, artist_names, unknown_dir):
        for i in range(len(artist_names)):
            for j in range(len(folder_titles)):
                str_test = isinstance(artist_names[i], str)
                if (artist_names[i] == folder_titles[j]) and (str_test == True):
                    shutil.copy(song_locations[i].strip(), new_dirs[j].strip())

    '''
    |--------------------------------------------------------------------------
    | Copy Unkown Files To Directories:
    |--------------------------------------------------------------------------
    |
    | This is where we copy all files that need meta data identification, to 
    | a new repository. This wil allow the audio fingerprinting process 
    | to be simplified and directory targeted.
    |
    '''
    def copy_all_unknowns(self, unknown_songs, unknown_dir):
        for i in range(len(unknown_songs[1])):
            shutil.copy(unknown_songs[1][i], unknown_dir)

    '''
    |--------------------------------------------------------------------------
    | Rename Audio Fingerprinted Files:
    |--------------------------------------------------------------------------
    |
    | This is where we rename files: If tags i.e. meta data doesn't match 
    | visible file name on pc. It can be difficult for the user to know 
    | what song they are looking at.
    |
    | Note: This function will be built once audio fingerprinting has been 
    | added into Jam arrange.
    |
    '''
    def rename_files(self):
        pass
