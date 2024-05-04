#-----------Bolierplate Code Start -----
import socket
import sys
from threading import Thread
from tkinter import *
from tkinter import ttk
import select

import time
import ftplib
import os
import ntpath #This is used to extract filename from path

from tkinter import filedialog
from pathlib import Path


from playsound import playsound
import pygame
from pygame import mixer


PORT  = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

song_counter = 0
song_selected = None
listbox = None
infoLabel = None

for file in os.listdir('shared_files'):
    filename = os.fsdecode(file)
    listbox.insert(song_counter, filename)
    song_counter = song_counter + 1

def play():
    global song_selected
    global listbox
    global infoLabel
    song_selected = listbox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load('shared_files/'+ song_selected)
    mixer.music.play()
    if(song_selected != ""):
        infoLabel.configure(text = "Now Playing: " + song_selected)
    else:
        infoLabel.configure(text = "")    

def stop():
    global song_selected
    global infoLabel
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+ song_selected)
    mixer.music.pause()
    infoLabel.configure(text="")

def resume():
    global song_selected
    mixer.init()
    mixer.music.load('shared_files/'+ song_selected)
    mixer.music.play()

def pause():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+ song_selected)
    mixer.music.pause()

def browseFiles():
    global textarea
    global filePathLabel

    try:
        filename = filedialog.askopenfilename()
        filePathLabel.configure(text=filename)
        HOSTNAME = "127.0.0.1"
        USERNAME = "lftpd"
        PASSWORD = "lftpd"

        ftp_server = FTP(HOSTNAME, USERNAME, PASSWORD)
        ftp_server.encoding = "utf-8"
        ftp_server.cwd('shared_files')
        fname = ntpath.basename(filename)
        with open(filename, 'rb') as file:
            ftp_server.storbinary(f"STOR {fname}", file)
        
        ftp_server.dir()
        ftp_server.quit()
    except FileNotFoundError:
        print("Cancel Button Pressed")    

def musicWindow():

   
    print("\n\t\t\t\tMUSIC PLAYER")

    #Client GUI starts here
    window=Tk()

    window.title('Music Window')
    window.geometry("300x300")
    window.configure(bg='LightSkyBlue')

    selectlabel = Label(window, text= "Select Song",bg='LightSkyBlue', font = ("Calibri",8))
    selectlabel.place(x=2, y=1)

    listbox = Listbox(window,height = 10,width = 39,activestyle = 'dotbox', bg='LightSkyBlue', borderwidth = 2,font = ("Calibri",10))
    listbox.place(x=10, y=70)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    playButton = Button(window,text="Play", bd=1,width = 10, bg='LightSkyBlue', font = ("Calibri",10), command = play)
    playButton.place(x=30,y=200)

    Stop=Button(window,text="Stop", bd=1,width = 10, bg='LightSkyBlue', font = ("Calibri",10), command = stop)
    Stop.place(x=200,y=200)

    infoLabel = Label(window, text= "",fg = 'blue', font = ("Calibri",8))
    infoLabel.place(x=4, y=288)

    ResumeButton=Button(window,text="Resume", bd=1, width = 10, bg='LightSkyBlue', font = ("Calibri",10), command = resume)
    ResumeButton.place(x=30,y=250)

    PauseButton=Button(window,text="Pause", bd=1, width = 10, bg='LightSkyBlue', font = ("Calibri",10), command = pause)
    PauseButton.place(x=200,y=250)

    upload=Button(window,text="Upload", bd=1,width = 10, bg='LightSkyBlue', font = ("Calibri",10), command = browseFiles)
    upload.place(x=115,y=250)

    download=Button(window,text="Download", bd=1, width = 10, bg='LightSkyBlue', font = ("Calibri",10))
    download.place(x=115,y=200)

  
    window.mainloop()




def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

   
    musicWindow()

setup()
