import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from pytube import YouTube
import sys

root = Tk()
root.geometry('360x520')

title = Label(root, text='Rodolfo Ortiz\n YouTube Downloader', fg='white', bg='red', font =('cortana', 17, 'bold'))
title.place(x='51', y='90')

def downloadmp3():
    rootmp3=Tk()
    rootmp3.geometry('310x520')
    title=Label(rootmp3, text='Download mp3 file here', fg='white', bg='blue', font=('cortana',15,'italic')).pack()

    linkmp3=Label(rootmp3, text='Paste your link here', fg='red', font=('cortana',12))
    linkmp3.place(x='71',y='160')

    pastelink=Entry(rootmp3, width=20, font=('cortana', 14))
    pastelink.place(x='50', y='190')

    def downloadmp3file():
        link = pastelink.get()
        video = YouTube(link)
        stream = video.streams.get_audio_only()
        directory = filedialog.askdirectory()
        stream.download(directory)
        messagebox.showinfo('Success','Download completed')

    dmp3=Button(rootmp3, text='Download', fg='white',bg='red',font=('cortana',15,'bold'), command=downloadmp3file)
    dmp3.place(x='100', y='237')


mp3=Button(root, text='Download mp3', fg='white', bg='blue', font=('cortana',12,'bold'), command=downloadmp3)
mp3.place(x='110', y='210')

def downloadmp4():
    rootmp4=Tk()
    rootmp4.geometry('310x520')
    title=Label(rootmp4, text='Download mp4 file here', fg='white', bg='green', font=('cortana',15,'italic')).pack()

    linkmp4=Label(rootmp4, text='Paste your link here', fg='red', font=('cortana',12))
    linkmp4.place(x='71',y='160')

    pastelink=Entry(rootmp4, width=20, font=('cortana', 14))
    pastelink.place(x='50', y='190')

    def downloadmp4file():
        link = pastelink.get()
        video = YouTube(link)
        stream = video.streams.get_highest_resolution()
        directory = filedialog.askdirectory()
        stream.download(directory)
        messagebox.showinfo('Success', 'Download completed')

    dmp4=Button(rootmp4, text='Download', fg='white',bg='red',font=('cortana',15,'bold'), command=downloadmp4file)
    dmp4.place(x='110', y='237')


mp4=Button(root, text='Download mp4', fg='white', bg='green', font=('cortana',12,'bold'), command=downloadmp4)
mp4.place(x='110', y='260')

root.mainloop()