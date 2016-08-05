import wx
from wx.lib.buttons import GenButton

class Example(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs) 
            
        self.InitUI()
        
    def InitUI(self):    

        panel = wx.Panel(self)

        btn = GenButton(panel, label='Button', 
            pos=(100, 100))
        btn.SetBezelWidth(1)
        btn.SetBackgroundColour('DARKGREY')

        wx.EVT_ENTER_WINDOW(btn, self.OnEnter)
        wx.EVT_LEAVE_WINDOW(btn, self.OnLeave)

        self.SetSize((300, 200))
        self.SetTitle('Interactive button')
        self.Centre()
        self.Show(True)
        
    def OnEnter(self, e):
        
        btn = e.GetEventObject()        
        btn.SetBackgroundColour('GREY79')
        btn.Refresh()

    def OnLeave(self, e):
        
        btn = e.GetEventObject()
        btn.SetBackgroundColour('DARKGREY')
        btn.Refresh()

def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()
