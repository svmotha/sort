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
def collect_audio(target):
    all_files_in_dir = os.listdir(target)
    audio_files = []
                            # Extracted Audio file details 
    # 1. Artist
    # 2. Title (song name)
    # 3. Album title
    # 4. Path on local storage
    # 5. Track number
    # 6. Total number of tracks on specific album
    # 7. Tracking id generation 
    audio_file_deets = [[],[],[],[],[],[],[]]
    files_not_parsed = []
    count = 0
    for i in range(len(all_files_in_dir)):
        if all_files_in_dir[i].endswith(('.mp3', '.wav', '.MP3', '.wma')) == True:
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
                audio_file_deets[6].append(count)
                count = count + 1
                audio_files.append(all_files_in_dir[i])
            if current_audiofile == None:
                files_not_parsed.append(temp)
    return audio_file_deets, files_not_parsed, all_files_in_dir

#------------------------------------------------------------------------------
'''
Making a list of all known artist names to use later when creating song
storage folders.
'''

def music_handling(audio_file_deets):
    artist_names = []
    # Create artist name folders: os.mkdir(’mydir’)
    for i in range(len(audio_file_deets[0])):
        '''
                            NB: Attention!!!!!!!!!!!
        Unicode testin function must enter here once completed:
        isinstance(a, unicode)
        '''
        if audio_file_deets[0][i] != None:
            artist_names.append(str(audio_file_deets[0][i].strip()
                                    .encode('utf-8')))
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

    return artist_names, folder_titles, unknown_songs

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

def making_arranged_dir(target, folder_titles):
    moveto = os.path.join(target, 'Arranged files')
    os.mkdir(os.path.join(target, 'Arranged files'))
    new_dirs = []

    for i in range(len(folder_titles)):
        os.mkdir(os.path.join(moveto , folder_titles[i]))
        new_dirs.append(os.path.join(moveto , folder_titles[i]))
    unknown_dir = os.path.join(moveto, 'Unknown artists').strip()
    os.mkdir(os.path.join(moveto , 'Unknown artists'))
    return moveto, new_dirs, unknown_dir

#------------------------------------------------------------------------------
'''
Move files to respective folders
'''


#------------------------------------------------------------------------------
'''
Delete files while testing
'''
def delete_files(moveto):
    user_input = raw_input('''would you like to delete newly created
                           files: [y/n]\n''')
    if user_input.strip() == 'y':
        shutil.rmtree(moveto)


#------------------------------------------------------------------------------
'''
copy all files to right places
'''
def copy_to_arranged(new_dirs, song_locations, folder_titles,
                     artist_names, unknown_dir):
    for i in range(len(artist_names)):
        for j in range(len(folder_titles)):
            str_test = isinstance(artist_names[i], str)
            if (artist_names[i] == folder_titles[j]) and (str_test == True):
                shutil.copy(song_locations[i].strip(),new_dirs[j].strip())

#------------------------------------------------------------------------------
'''
Copy all files that need meta data identification, to a new repository.
Allowing the audio fingerprinting process to be simplified and centrallised,
'''

def copy_all_unknowns():
    pass
##            if str_test == False :
##                shutil.copy(song_locations[i].strip(),unknown_dir)
                
        
#------------------------------------------------------------------------------
'''
Rename files: If tags i.e. meta data doesn't match visible file name on pc
it can be difficult for the user to know what song they are looking at.
'''
def rename_files():
    pass

#------------------------------------------------------------------------------
'''
File tracking id module
'''
def create_tracking_id():
    pass

#------------------------------------------------------------------------------
                        #------ MAIN CODE ------#
#------------------------------------------------------------------------------
'''
MAIN CODE AND MAIN FUNCTION
'''
if __name__ == "__main__":
    target = "C:\\Users\\User\\Music\\test folder"
    audio_details = collect_audio(target)
    handle_files = music_handling(audio_details[0])
    create_folders = making_arranged_dir(target, handle_files[1])
    copying_songs = copy_to_arranged(create_folders[1], audio_details[0][3],
                                     handle_files[1], handle_files[0],
                                     create_folders[2])



##    delete_arrangement = delete_files(create_folders[0]) #Delete demo files


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------



    
