import wx

class WelcomeWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        ##wx.Frame.__init__(self, parent, title=title, style=wx.RAISED_BORDER)# no outside access
        self.SetBackgroundColour('white')
        self.CreateStatusBar()
        self.create_begin()

        # Setting up the menu
        filemenu= wx.Menu()
        viewmenu = wx.Menu()
        arrangemenu = wx.Menu()
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Learn more about Jam arrange")
        menuload = arrangemenu.Append(wx.ID_ANY, "&Load folder", "Select a folder with your songs to arrange.")
        menufullscreen = viewmenu.Append(wx.ID_ANY,"&Full screen"," Full screen")
        menufullscreenexit = viewmenu.Append(wx.ID_ANY,"&Exit full screen"," Exit Full screen")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Leave the program :( ")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        menuBar.Append(viewmenu, "&View")
        menuBar.Append(arrangemenu, "&Arrange")


        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content
        
        # Set events.
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.Onfullscreen, menufullscreen)
        self.Bind(wx.EVT_MENU, self.Onfullscreenexit, menufullscreenexit)

        self.Centre()
        self.Show(True)
##        self.Maximize(True)

    # Create and center begin button
    def create_begin(self):
##        panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
##        begin_button = wx.Button(panel, label="Get started",
##                                 size=(200,50))
        
##        begin_button.SetBackgroundColour('#00000')
        imageFile = "notclicked.png"
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        begin_button = wx.BitmapButton(self,id=-1,bitmap=image1,
                                       size=(220,60),
                                       style=wx.RAISED_BORDER)
        begin_button.SetCursor(wx.StockCursor(wx.CURSOR_HAND))
        begin_button.SetWindowStyleFlag(wx.RAISED_BORDER)
        
        main_sizer.AddStretchSpacer()
        main_sizer.Add(begin_button, 0, wx.CENTER)
        main_sizer.AddStretchSpacer()
        self.SetSizer(main_sizer)

        self.Bind(wx.EVT_BUTTON, self.Onbegin, begin_button)
        

    def Onfullscreen(self,e):
        self.Maximize(True)
    
    def Onfullscreenexit(self,e):
        self.Maximize(False)

    def Onbegin(self,e):
        dlg = wx.MessageDialog( self,
                                "Welcome to jam arrange",
                                "Lets get started", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    def OnAbout(self,e):
        dlg = wx.MessageDialog( self,
                                "Arranging your music has never been this simple",
                                "About Jam arrange", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.
    def OnExit(self,e):
        self.Close(True)  # Close the frame.

if __name__ == "__main__":
    app = wx.App(False)
    frame = WelcomeWindow(None, "Jam arrange")
    app.MainLoop()
