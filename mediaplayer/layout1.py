from Tkinter import Tk, RIGHT, BOTH, RAISED, LEFT, CENTER, TOP, BOTTOM
from ttk import Frame, Button, Style
import pygame
from tkFileDialog import askopenfilename


class ControlDesigns(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Buttons")
        self.style = Style()
        self.style.theme_use("default")
        
        frame = Frame(self, relief=RAISED, borderwidth=2)
        frame.pack(fill=BOTH, expand=True)
        
        self.pack(fill=BOTH, expand=True)

        playButton = Button(self, text="Play", command=PlayMusic)
        playButton.pack(side=LEFT, padx=5, pady=5)
        selectSong = Button(self, text="Add song", command=songSelector)
        selectSong.pack(side=RIGHT, padx=5, pady=5)
        stopButton = Button(self, text="Stop", command=StopMusic)
        stopButton.pack(side=LEFT, padx=5, pady=5)

def StopMusic():
        pygame.mixer.music.stop()

def PlayMusic(selectedSong,songvar):
    if songvar == True:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(selectedSong)
        pygame.mixer.music.play()
    else:
        selectedSong = songSelector()
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(selectedSong)
        pygame.mixer.music.play()

def nextSong():
    print ("clicked next")

def songSelector():
    Tk().withdraw()
    selectedSong = askopenfilename()
    return selectedSong

def main():
    songvar = False
    selectedSong = ''
    root = Tk()
    root.geometry("500x300+300+300")
    app = ControlDesigns(root)
    root.mainloop()  


if __name__ == '__main__':
    main()
