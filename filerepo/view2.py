import wx

class WelcomeWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, style=wx.RAISED_BORDER)
        self.SetBackgroundColour('white')
        self.CreateStatusBar()
        self.create_begin()

        # Setting up the menu
        filemenu= wx.Menu()
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Learn more about Jam arrange")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Leave the program :( ")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content
        # Set events.
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Show(True)
        self.Maximize(True)

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
