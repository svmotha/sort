import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Jam arrange")
frame.Show(True)
app.MainLoop()




'''
from Tkinter import Tk, Grid
from ttk import Frame, Button, Style, Progressbar
root = Tk()
arrange_button = Button(root, text="ARRANGE").grid(row=1, column=2,
                                                   rowspan=3, columnspan=3)
root.mainloop()
'''
