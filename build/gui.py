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
| Importing resources and WX GUI package:
|--------------------------------------------------------------------------
|
| This is where we import all our built python resources and the WX 
| GUI building package.
|
'''
from fileSort import Arranger
from jamTests import timer
import wx
from wx.lib.buttons import GenButton

'''
|--------------------------------------------------------------------------
| Main GUI operation window:
|--------------------------------------------------------------------------
|
| This is where we build the Jam arrange GUI, and call all sorting \
| functionality into the application.
|
'''
class WelcomeWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400,175))
        self.SetBackgroundColour('white')
        self.create_begin()

        filemenu= wx.Menu()  # Menu button
        menuarrange = filemenu.Append(wx.ID_ANY, "&Arrange", "Select a folder with your songs to arrange.")
        menuDelete = filemenu.Append(wx.ID_ANY, "&Delete", "Delete folders you no longer need.")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", "Learn more about Jam arrange")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit","Leave the program :( ")
        helpmenu = wx.Menu()
        menuhelp = helpmenu.Append(wx.ID_HELP, "&Help", "How to use Jam arrange.")
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File")
        menuBar.Append(helpmenu, "&Help")
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content

        '''
        |--------------------------------------------------------------------------
        | Setting events:
        |--------------------------------------------------------------------------
        |
        | This is where we link all user clicks, hovers, etc. to events, thus 
        | making the interface responsive as expected.
        |
        '''
        self.Bind(wx.EVT_MENU, self.onDir, menuarrange)
        self.Bind(wx.EVT_MENU, self.onDelete, menuDelete)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.onHelp, menuhelp)

        self.Centre()
        self.Show(True)

    '''
    |--------------------------------------------------------------------------
    | Launch basic GUI:
    |--------------------------------------------------------------------------
    |
    | This is where we build the basic GUI, which runs on application launch.
    |
    '''
    def create_begin(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetFont(wx.Font(25,
                             wx.FONTFAMILY_MODERN,
                             wx.FONTSTYLE_NORMAL,
                             wx.FONTWEIGHT_BOLD,
                             faceName="Roboto"))
        begin_button = GenButton(self,id=-1,label="Arrange",size=(200,55),style=wx.BORDER_SIMPLE)
        begin_button.SetForegroundColour(wx.Colour(255, 255, 255))
        begin_button.SetBezelWidth(1)
        begin_button.SetBackgroundColour('#5f9ad8')
        begin_button.SetCursor(wx.Cursor(wx.CURSOR_HAND)) #StockCursor deprecated
        begin_button.SetWindowStyleFlag(wx.RAISED_BORDER)
        main_sizer.AddStretchSpacer()
        main_sizer.Add(begin_button, 0, wx.CENTER)
        main_sizer.AddStretchSpacer()
        self.SetSizer(main_sizer)
        self.Bind(wx.EVT_BUTTON, self.onDir, begin_button)

    '''
    |--------------------------------------------------------------------------
    | Deleting any files user selects:
    |--------------------------------------------------------------------------
    |
    | This is where we user file selection to directory deleting functions.
    |
    '''
    def onDelete(self, event):
        dlg = wx.DirDialog(self, "Choose a folder to delete",
                           style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )
        if dlg.ShowModal() == wx.ID_OK:
            target = str(dlg.GetPath())
            shutil.rmtree(target)
            message = "Your files have been deleted :("
            Onbegin(self,message)
        dlg.Destroy()

    '''
    |--------------------------------------------------------------------------
    | Selecting and arranging user files:
    |--------------------------------------------------------------------------
    |
    | This is where we open an operating system directory to allow the user 
    | to select a folder that contains the songs they'd like to arrange.
    |
    '''
    def onDir(self, event):
        '''
        |--------------------------------------------------------------------------
        | Display selected dir message box:
        |--------------------------------------------------------------------------
        |
        | This is where we display a message box to test if found file dir 
        | is one selected by user.
        |
        '''
        def Onbegin(self, message):
            dlg = wx.MessageDialog( self,
                                    message,
                                    "Arrangement successful", wx.OK)
            dlg.ShowModal()
            dlg.Destroy()

        '''
        |--------------------------------------------------------------------------
        | Display selected dir message box:
        |--------------------------------------------------------------------------
        |
        | This is where we show the DirDialog and print the user's choice to 
        | stdout.
        |
        '''
        dlg = wx.DirDialog(self, "Choose a folder to arrange",
                           style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )
        if dlg.ShowModal() == wx.ID_OK:

            target = str(dlg.GetPath())
            '''
            |--------------------------------------------------------------------------
            | Arranging sorting and timing:
            |--------------------------------------------------------------------------
            |
            | This is where we execute the arranging function and timing test.
            | We also sort the audio file sthrough various functions. The
            | application displays the time it took to arrange the files, 
            | which should be less than a song a second on average.
            |
            '''
            Sort = Arranger.Arranger(target_path=target)
            test_time = timer.TimeKeeper().stopWatch() # Timing process
            audio_details = Sort.collect_audio(Sort.target_path)
            handle_files = Sort.music_handling(audio_details[0])
            create_folders = Sort.making_arranged_dir(Sort.target_path, handle_files[1])
            Sort.copy_to_arranged(create_folders[1], audio_details[0][3], handle_files[1], handle_files[0],create_folders[2])
            Sort.copy_all_unknowns(handle_files[2], create_folders[2])
            Sort.clean_unknown_folder(handle_files[2], create_folders[2])
            time_taken = round((timer.TimeKeeper().stopWatch() - test_time), 2)
            message = "Jam arrange took: " + str(time_taken) + "s, to arrange your songs."

            Onbegin(self,message)
        dlg.Destroy()

    '''
    |--------------------------------------------------------------------------
    | Maximise & Minimise window:
    |--------------------------------------------------------------------------
    |
    | This is where we allow user to view GUI in fullscreen mode. We 
    | also allow user to exit fullscreen mode as they desire.
    |
    '''
    def Onfullscreen(self,e):
        self.Maximize(True)

    def Onfullscreenexit(self,e):
        self.Maximize(False)

    '''
    |--------------------------------------------------------------------------
    | About window:
    |--------------------------------------------------------------------------
    |
    | This is where we allow user to view a message dialog, about the 
    | application.
    |
    '''
    def OnAbout(self,e):
        dlg = wx.MessageDialog( self,
                                "Arranging your music has never been this simple",
                                "About Jam arrange", wx.OK)
        dlg.ShowModal() # Show its
        dlg.Destroy() # finally destroy it when finished.

    '''
    |--------------------------------------------------------------------------
    | Exit application:
    |--------------------------------------------------------------------------
    |
    | This is where we allow user to exit the application.
    |
    '''
    def OnExit(self,e):
        self.Close(True)  # Close the frame.

    '''
    |--------------------------------------------------------------------------
    | Application support:
    |--------------------------------------------------------------------------
    |
    | This is where we give the user any help they would require when using
    | Jam arrange.
    |
    | Note: This functionality is currently unavailable.
    |
    '''
    def onHelp(self, e):
        pass

'''
|--------------------------------------------------------------------------
| Executing application:
|--------------------------------------------------------------------------
|
| This is where we execute the application on launch.
|
'''
if __name__ == "__main__":
    app = wx.App(False)
    frame = WelcomeWindow(None, "Jam arrange v0.0.4")
    app.MainLoop()
