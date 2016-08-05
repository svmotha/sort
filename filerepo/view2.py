'''
Jam arrange: GUI linked to arrangement algorithm
Author: Numstack (Pty) Ltd
Copyright 2016
Objective: Through the use of a simple GUI, identify mp3, wav, etc. files and arrange them accordingly in desired local storage folder.
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
import wx

class MyFileDropTarget(wx.FileDropTarget):
    """
    Drag and drop file in field
    """
    def __init__(self, window):
        """Constructor"""
        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, filenames):
        """
        When files are dropped, write where they were dropped and then
        the file paths themselves
        """
        self.window.SetInsertionPointEnd()
        self.window.updateText("\n%d file(s) dropped at %d,%d:\n" %
                              (len(filenames), x, y))
        for filepath in filenames:
            self.window.updateText(filepath + '\n')

'''
Main window for operation
'''

class WelcomeWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400,175))
        # wx.Frame.__init__(self, parent, title=title, style=wx.RAISED_BORDER)  no outside access
        self.SetBackgroundColour('white')
##        self.CreateStatusBar()
        self.create_begin()

        # Setting up the menu bars and their various buttons
        filemenu= wx.Menu()
        menuarrange = filemenu.Append(wx.ID_ANY, "&Arrange", "Select a folder with your songs to arrange.")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", "Learn more about Jam arrange")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit","Leave the program :( ")

        helpmenu = wx.Menu()
        menuhelp = helpmenu.Append(wx.ID_HELP, "&Help", "How to use Jam arrange.")

        # viewmenu = wx.Menu()
        # menufullscreen = viewmenu.Append(wx.ID_ANY,"&Full screen"," Full screen")
        # menufullscreenexit = viewmenu.Append(wx.ID_ANY,"&Exit full screen"," Exit Full screen")

        # Creating the menu bar
        # Adding the "file menu" to the MenuBar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File")
        menuBar.Append(helpmenu, "&Help")
        # menuBar.Append(viewmenu, "&View")


        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content
        
        # Set events.
        self.Bind(wx.EVT_MENU, self.onDir, menuarrange)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Bind(wx.EVT_MENU, self.onHelp, menuhelp)

        # self.Bind(wx.EVT_MENU, self.Onfullscreen, menufullscreen)
        # self.Bind(wx.EVT_MENU, self.Onfullscreenexit, menufullscreenexit)

        self.Centre()
        self.Show(True)
#        self.Maximize(True)

    # Create and center begin button : arrange
    def create_begin(self):
        # panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetFont(wx.Font(25,
                             wx.FONTFAMILY_MODERN,
                             wx.FONTSTYLE_NORMAL,
                             wx.FONTWEIGHT_BOLD,
                             faceName="Roboto"))
        begin_button = wx.Button(self,id=-1,label="Arrange",size=(200,55),style=wx.RAISED_BORDER)
        begin_button.SetForegroundColour(wx.Colour(255, 255, 255))
        begin_button.SetBackgroundColour('#5f9ad8')
        # begin_button.SetBackgroundColour('#5f9ad8')

        # imageFile = "/home/victor/development/jamarrange.io/filerepo/notclicked.png"
        # image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        # begin_button = wx.BitmapButton(self,id=-1,bitmap=image1,
        #                                size=(220,60),
        #                                style=wx.RAISED_BORDER)
        begin_button.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
        begin_button.SetWindowStyleFlag(wx.RAISED_BORDER)
        
        main_sizer.AddStretchSpacer()
        main_sizer.Add(begin_button, 0, wx.CENTER)
        main_sizer.AddStretchSpacer()
        self.SetSizer(main_sizer)

        self.Bind(wx.EVT_BUTTON, self.onDir, begin_button)

    '''
    Open operating system directory and select a folder that contains the
    songs you'd like to arrange.
    '''

    def onDir(self, event):
        '''
        message box to test if found file dir is one chosen
        '''
        def Onbegin(self, message):
            dlg = wx.MessageDialog( self,
                                    message,
                                    "Arrangement successful", wx.OK)
            dlg.ShowModal()
            dlg.Destroy()
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
                os.mkdir(os.path.join(moveto, folder_titles[i]))
                new_dirs.append(os.path.join(moveto, folder_titles[i]))
            unknown_dir = os.path.join(moveto, 'Unknown artists').strip()
            os.mkdir(os.path.join(moveto, 'Unknown artists'))
            return moveto, new_dirs, unknown_dir

        '''
        Move files to respective folders
        '''

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
            for i in range(len(unknown_songs)):
                shutil.copy(unknown_songs[1][i], unknown_dir)

        '''
        Rename files: If tags i.e. meta data doesn't match visible file name on pc
        it can be difficult for the user to know what song they are looking at.
        '''
        def rename_files():
            pass

        """
        Show the DirDialog and print the user's choice to stdout
        """
        dlg = wx.DirDialog(self, "Choose a folder to arrange",
                           style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )
        if dlg.ShowModal() == wx.ID_OK:

            target = str(dlg.GetPath())
            # Executing arranging algorithm
            audio_details = collect_audio(target)
            handle_files = music_handling(audio_details[0])
            create_folders = making_arranged_dir(target, handle_files[1])
            copy_to_arranged(create_folders[1], audio_details[0][3], handle_files[1], handle_files[0],create_folders[2])
            copy_all_unknowns(handle_files[2], create_folders[2])

        #    delete_arrangement = delete_files(create_folders[0]) #Delete demo files
            message = "Your songs have been ARRANGED!!!"
            Onbegin(self,message)
        dlg.Destroy()

    def Onfullscreen(self,e):
        self.Maximize(True)
    
    def Onfullscreenexit(self,e):
        self.Maximize(False)

    def OnAbout(self,e):
        dlg = wx.MessageDialog( self,
                                "Arranging your music has never been this simple",
                                "About Jam arrange", wx.OK)
        dlg.ShowModal() # Show its
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self,e):
        self.Close(True)  # Close the frame.

    def onHelp(self, e):
        pass

if __name__ == "__main__":
    app = wx.App(False)
    frame = WelcomeWindow(None, "Jam arrange v1.0.1")
    app.MainLoop()
