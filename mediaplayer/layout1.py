from Tkinter import Tk, RIGHT, BOTH, RAISED, LEFT, CENTER, TOP, BOTTOM
from ttk import Frame, Button, Style, Progressbar
import pygame
from tkFileDialog import askopenfilename



class ControlDesigns(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("jam arrange V.0.1")
        self.style = Style()
        self.style.theme_use("default")
        '''
        frame = Frame(self, relief=RAISED, borderwidth=2)
        frame.pack(fill=BOTH, expand=True)
        '''

        frame1 = Frame(self, relief=RAISED, borderwidth=2)
        frame1.pack(fill=BOTH, expand=True)
        songProgress = Progressbar(frame1)
        songProgress.pack(side=BOTTOM, padx=5, pady=5)
        
        self.pack(fill=BOTH, expand=True)

        playButton = Button(self, text="Play", width=4, command=PlayMusic)
        playButton.pack(side=LEFT, padx=5, pady=5)
        selectSong = Button(self, text=" + ", width=2 , command=addSong)
        selectSong.pack(side=RIGHT, padx=5, pady=5)
        stopButton = Button(self, text="Stop", width=4, command=StopMusic)
        stopButton.pack(side=LEFT, padx=5, pady=5)

def StopMusic():
        pygame.mixer.music.stop()

def addSong():
    playme = songSelector()
    if (playme != ''):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(playme)
        pygame.mixer.music.play()

def nextSong():
    print ("clicked next")

def songSelector():
    Tk().withdraw()
    global globalvar
    globalvar = askopenfilename()
    global globalvar
    return globalvar

def PlayMusic():
    if (globalvar != ''):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(globalvar)
        pygame.mixer.music.play()
    if (globalvar == ''):
        playme = songSelector()
        if (playme != ''):
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load(playme)
            pygame.mixer.music.play()

def globeVariables():
    songName = ''
    return songName

globalvar = globeVariables()
def main():
    root = Tk()
    root.geometry("350x150+300+300")
    app = ControlDesigns(root)
    root.mainloop()


if __name__ == '__main__':
    main()
