#Lyric finder 

import re, requests
from bs4 import BeautifulSoup
from tkinter import *
from selenium import webdriver
import tkinter.messagebox

def getLyrics():
    artist = artistEntry.get().replace(' ','-')
    song = songEntry.get().replace(' ','-')
    global lyricLabel
    global listbox

    listbox.delete(0, END) #clears listbox

    url = 'https://genius.com/' +artist +'-'+ song +'-lyrics'


    res = requests.get(url)
    try:
        res.raise_for_status()     #file not found
    except:
        listbox.insert(END, 'Not found, Try Again')
        pass

    soup = BeautifulSoup(res.text,'html.parser')
    page = soup.find('p').getText()

    pagelist = page.split('\n')

    for line in pagelist:     #print lyrics
        listbox.insert(END, line)

def getSong():
    artist = artistEntry.get().replace(' ','+')
    song = songEntry.get().replace(' ','+')

    if artist == '' or song =='':
        tkinter.messagebox.showinfo('Error','Please complete fields')
        return


    url = 'https://www.youtube.com/results?search_query=' + artist +'+' +song
    browser = webdriver.Firefox()
    browser.get(url)

root = Tk()
root.wm_title('Lyric Finder v1.0    Sam Noguchi')

scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = BOTH)

listbox = Listbox(root, yscrollcommand=scrollbar.set, width = 60, height = 10)
listbox.pack(side=BOTTOM, fill=BOTH)
scrollbar.config(command=listbox.yview)

inputFrame = Frame(root, width = 60, height = 10)
inputFrame.pack(side=TOP)

artistLabel = Label(inputFrame, text = 'Artist: ')
artistLabel.grid(row = 0 , column = 0)
artistEntry = Entry(inputFrame)
artistEntry.grid(row = 0, column = 1)

songLabel = Label(inputFrame, text = 'Song: ')
songLabel.grid(row = 1 , column = 0)
songEntry = Entry(inputFrame)
songEntry.grid(row = 1, column = 1)

submitButton =Button(inputFrame, text = 'Find Lyrics', command =getLyrics)
submitButton.grid(row=2, column = 0)

searchButton = Button(inputFrame, text = 'Listen', command = getSong)
searchButton.grid(row =2, column = 1)

root.mainloop()
