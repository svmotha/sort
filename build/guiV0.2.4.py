'''
Jam arrange: GUI linked to arrangement algorithm
Author: Numstack (Pty) Ltd
Copyright 2016
Objective: Through the use of a simple GUI, identify mp3, wav, etc. files and arrange them accordingly in desired local storage folder.
Current stable version: 0.2.4
'''

'''
Importing all necessary libraries
'''
from fileSort import Arranger
from jamTests import timer
import time
import wx
from wx.lib.buttons import GenButton

'''
Main window for operation
'''

class WelcomeWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400,175))
        self.SetBackgroundColour('white')
        self.create_begin()

        # Menu button
        filemenu= wx.Menu()
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
        # Set events.
        self.Bind(wx.EVT_MENU, self.onDir, menuarrange)
        self.Bind(wx.EVT_MENU, self.onDelete, menuDelete)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.onHelp, menuhelp)

        self.Centre()
        self.Show(True)

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
    Deleting any files user selects
    '''
    def onDelete(self, event):
        dlg = wx.DirDialog(self, "Choose a folder to arrange",
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
            Sort = Arranger.Arranger(target)
            '''
            Executing arranging algorithm and timing
            '''
            start_time = time.time() # purely for test purposes
            audio_details = Sort.collect_audio(target)
            handle_files = Sort.music_handling(audio_details[0])
            create_folders = Sort.making_arranged_dir(target, handle_files[1])
            Sort.copy_to_arranged(create_folders[1], audio_details[0][3], handle_files[1], handle_files[0],create_folders[2])
            Sort.copy_all_unknowns(handle_files[2], create_folders[2])
            clean_arranged_folder = Sort.clean_unknown_folder(handle_files[2], create_folders[2])
            # print "Jam arrange took", time.time() - start_time, "to arrange your songs." # finding out how long process takes (purely for test purposes)
            message = "Jam arrange took: " + str(time.time() - start_time) + "s, to arrange your songs."
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
    frame = WelcomeWindow(None, "Jam arrange v0.2.4")
    app.MainLoop()
