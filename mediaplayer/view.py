import Tkinter as tk
import ttk
import tkMessageBox
import tkFileDialog


import model
import player


class View:
    def __init__(self,root, model, player):
        self.root = root
        self.model = model
        self.player = player
        self.create_gui()

    def creat_gui(self):
        self.root.title(AUDIO_PLAYER_NAME)
        self.creat_top_display()
        self.create_button_frame()
        self.create_list_box()
        self.create_bottom_frame()
        self.create_context_menu()

if __name__ == '__main__':
    root = Tk()
    root.resizable(width=False, height=False)

    player = player.Player()
    model = model.Model()
    app = View(root, model, player)
    root.mainloop()
    
