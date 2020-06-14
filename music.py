from tkinter import *
import pygame
pygame.init()
pygame.mixer.init()
a=0

root=Tk()
root.title("music")
root.geometry("300x400")
def play_1():
    pygame.mixer.music.load("1.mp3")
    pygame.mixer.music.play()
def pause_1():
    pygame.mixer.music.pause()    
def unpause_1():
    pygame.mixer.music.unpause()  
def chvol(a):
    a=volume.get()
    pygame.mixer.music.set_volume(a)



butplay=Button(root,text="play",heigh=5,width=10,bg="red",command=play_1)
butplay.pack(side=LEFT)
butpause=Button(root,text="pause",heigh=5,width=10,bg="green",command=pause_1)
butunpause=Button(root,text="unpause",heigh=5,width=10,bg="blue",command=unpause_1)
butpause.pack(side=LEFT)
butunpause.pack(side=LEFT)
volume=Scale(root,from_=0,to_=1,resolution=0.1,orient=HORIZONTAL,command=chvol)
volume.pack(side=BOTTOM)
labvol=Label(root,text="volume")
labvol.place(x=100,y=500)
labvol.pack(side=BOTTOM)

root.mainloop()
