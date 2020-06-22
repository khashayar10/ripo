import os
from tkinter.filedialog import askdirectory
from tkinter import filedialog
from tkinter import *
import pygame
import time
from mutagen.id3 import ID3
from tkinter import *
from tinytag import TinyTag
import threading 
name=""
root = Tk()
root.minsize(450,330)
root.iconphoto(False, PhotoImage(file="C:/Users/Public/Music/Sample Music/icon.jpg"))
root.title("music player")
t1=0
k=0

key=0
t=0
namesong=Label(root,text="name of song:")
namesong.pack()
namesong.place(x=190,y=50)
listofsongs = []
realnames = []
timesong=StringVar()
timesong.set("00:00")
v = StringVar()
current=StringVar()
current.set("00:00")
songlabel = Label(root,textvariable=v,width=35)
totaltime=Label(root,textvariable=timesong)
totaltime.pack()
totaltime.place(x=190,y=120)
timelable=Label(root,text="total time")
timelable.pack()
timelable.place(x=190,y=100)
currentlab=Label(root,textvariable=current)
currentlab.pack()
currentlab.place(x=190,y=170)
currentlabel=Label(root,text="current time")
currentlabel.pack()
currentlabel.place(x=190,y=150)
j=0
index=0
pygame.mixer.init()
def directorychooser():
    global j
    
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith("mp3") or files.endswith("wav"):

            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])
            listofsongs.append(files)
            listbox.insert(j,files)
            
            j+=1
            print(j) 
    

    pygame.mixer.music.load(listofsongs[0])
    #pygame.mixer.music.play()
def play():
  global key
  key=2  
  global t1  
  global index
  index=listbox.curselection()[0]
  if pygame.mixer.music.get_busy:
      stopsong()
      time.sleep(2)
  pygame.mixer.music.load(listofsongs[index])
  pygame.mixer.music.play()
  ganre(index)
  artist(index)
  updatelabel(index)
  updatetimesong(index)
  chvol(0)
  t1=threading.Thread(target=currenttime)
  t1.start()
def currenttime():
    global index

    tag=TinyTag.get(listofsongs[index])  
    time_1=tag.duration
    time_1=int(time_1)
    while time_1>0 and pygame.mixer.music.get_busy()  :
        global key
        if key==1:
            continue
        minet=int(time_1/60)
        sec=time_1%60
        current.set(f"{minet}:{sec}")
        time.sleep(1)
        time_1-=1  

def updatetimesong(x):

    tag=TinyTag.get(listofsongs[x])
    x=int(tag.duration)
    minet=x/60
    sec=x%60
    timesong.set(f"{int(minet)}:{sec}")  
  


def updatelabel(x):


    v.set(realnames[x])
    
    #return songname


def nextsong():
    stopsong()
    t2=threading.Thread(target=currenttime)
    
    time.sleep(2)
    global index
    index += 1
    updatelabel(index)
    ganre(index)
    artist(index)
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatetimesong(index)
    t2.start()

    


def prevsong():
    stopsong()
    time.sleep(2)
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel(index)
    ganre(index)
    artist(index)
    t3=threading.Thread(target=currenttime)
    updatetimesong(index)
    t3.start()


def stopsong():
    pygame.mixer.music.stop()
    v.set("")
    timesong.set("00:00")
    ganresong.set("")
    artsong.set("")
    current.set("00:00")
    global t
    t=0
    time.sleep(1)
    #return songname
    

def pause():
    global key
    key=1
    pygame.mixer.music.pause()
def unpause():
    global key
    key=0
    pygame.mixer.music.unpause()
label = Label(root,text='Music library')
label.pack()
label.place(x=60,y=5)

listbox = Listbox(root)
listbox.pack()
listbox.place(x=60,y=30)

def add():
    global j
    j+=1
    
    filename=filedialog.askopenfilename()
    dire=os.path.realpath(filename)
    global name
    name=ID3(dire)
    realnames.append(name['TIT2'].text[0])
    listofsongs.append(filename)
    listbox.insert(j,name['TIT2'].text[0])
    
    print(j)
def remove():
    item=listbox.curselection()[0]
    del listofsongs[item]
    del realnames[item]
    listbox.delete(item)

def chvol(a):
    a=volume.get()
    pygame.mixer.music.set_volume(a)

def close_window (): 
    stopsong()
    root.destroy()

def replay():
    global index
    stopsong()
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel(index)
    ganre(index)
    artist(index)
    updatetimesong(index)
    t4=threading.Thread(target=currenttime)
    t4.start()
def playall():
    global j
    global t
    global index
    index=t
    pygame.mixer.music.load(listofsongs[t])
    pygame.mixer.music.play()
    ganre(t)
    artist(t)
    updatelabel(t)
    updatetimesong(t)
    t6=threading.Thread(target=currenttime)
    t6.start()
    t5=threading.Thread(target=playall_2)
    t5.start()

def playall_2():

    global t
    tag=TinyTag.get(listofsongs[t])
    time_1=tag.duration
    time_1=int(time_1)
    while time_1>0 and pygame.mixer.music.get_busy() :
        time.sleep(1)
        time_1-=1    
     
    if t<j and   pygame.mixer.music.get_busy():
        t+=1
        playall()
    if t==j:
        t=0      

        
def ganre(x):
    tag=TinyTag.get(listofsongs[x])
    g=tag.genre
    ganresong.set(g)
def artist(x):
    tag=TinyTag.get(listofsongs[x])
    art=tag.artist
    artsong.set(art)
ganresong=StringVar()
artsong=StringVar()
ganrelab=Label(root,textvariable=ganresong)
ganrelab.pack()
ganrelab.place(x=310,y=70)
glab=Label(root,text="ganre")
glab.pack()
glab.place(x=310,y=50)
artlab=Label(root,text="artist")
artlab.pack()
artlab.place(x=370,y=50)
artv=Label(root,textvariable=artsong)
artv.pack()
artv.place(x=370,y=70)
photovol=PhotoImage(file="C:/Users/Public/Music/Sample Music/vol.png")
photoimage4=photovol.subsample(10,10)    
vol=Label(root,image=photoimage4)    
vol.pack()
vol.place(x=410,y=300)
photonext=PhotoImage(file="C:/Users/Public/Music/Sample Music/download.jpg")
PhotoImage2=photonext.subsample(8,8)
nextbutton = Button(root,text = 'Next Song',image=PhotoImage2,command=nextsong)
nextbutton.pack()
nextbutton.place(x=165,y=250)
photoper=PhotoImage(file="C:/Users/Public/Music/Sample Music/p.png")
photoimage3=photoper.subsample(8,8)
previousbutton = Button(root,text ='Previous Song',image=photoimage3,command=prevsong)
previousbutton.pack()
previousbutton.place(x=85,y=250)
stopbutton = Button(root,text='Stop Music',command=stopsong)
stopbutton.pack()
stopbutton.place(x=100,y=300)


stopbutton.bind("<Button-1>",stopsong)

songlabel.pack()
songlabel.place(x=115,y=70)
pusbut=Button(root,text="pause",command=pause)
pusbut.pack()
pusbut.place(x=50,y=300)
butunpase=Button(root,text="unpase",command=unpause)
butunpase.pack()
butunpase.place(x=180,y=300)
chdir=Button(root,text="select file",bg="black",fg="white",command=directorychooser)
chdir.pack()
chdir.place(x=80,y=200)
photoplay=PhotoImage(file="C:/Users/Public/Music/Sample Music/d.jpg")
PhotoImage1=photoplay.subsample(8,8)
butplay=Button(root,text="play",command=play,image=PhotoImage1)
butplay.pack()
butplay.place(x=125,y=250)
addbut=Button(root,text="add",bg="green",command=add)
addbut.pack()
addbut.place(x=10,y=35)
delbut=Button(root,text="delete",bg="orange",command=remove)
delbut.pack()
delbut.place(x=10,y=70)
volume=Scale(root,to_=0,from_=1,resolution=0.1,orient=VERTICAL,command=chvol)
volume.pack()
volume.place(x=395,y=190)
buttonq = Button (root, text = "EXIT",bg="red",command=close_window)
buttonq.pack()
buttonq.place(x=410,y=5)
photore=PhotoImage(file="C:/Users/Public/Music/Sample Music/re.png")
photoimage5=photore.subsample(8,8)
butre=Button(root,image=photoimage5,command=replay)
butre.pack()
butre.place(x=45,y=250)

play_all=Button(root,text="playall",bg="pink",command=playall)
play_all.pack()
play_all.place(x=10,y=120)


root.mainloop()


