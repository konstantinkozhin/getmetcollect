import pandas as pd
from time import sleep
import os

import tkinter.messagebox as mb
from idlelib.tooltip import Hovertip
from tkinter import ttk
from tkinter import Frame
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import CENTER
from tkinter import PhotoImage
from tkinter import END
from tkinter import Radiobutton
from tkinter import IntVar
from tkinter import LabelFrame
from tkinter import filedialog
from tkinter.ttk import Notebook, Style
from tkinter import StringVar
from tkinter import colorchooser
import tkinter as tk    

import math
from datetime import datetime
from tqdm import tqdm

import random
import re 

import requests
import json
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import time
from bs4 import BeautifulSoup

root = tk.Tk()
root.title('GetMetCollect')
root.geometry("550x350")
root.resizable(width=False, height=False)
root.iconbitmap('icon.ico')


def create_a_file():
    
    req = str(req_Input.get())
    
    if req == '':

        url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects'
        req = requests.get(url)
        ids = req.json()
        ids_list = ids['objectIDs']

        with open("file.txt", 'w') as output:
            for row in ids_list:
                output.write(str(row) + '\n')
                
    else:
        
        url = f'https://collectionapi.metmuseum.org/public/collection/v1/search?q={req}'
        req = requests.get(url)
        ids = req.json()
        ids_list = ids['objectIDs']
        
        if ids_list != None:
            with open("file.txt", 'w') as output:
                for row in ids_list:
                    output.write(str(row) + '\n')
        else:
            print('No objects found on request')

                
def api():
            
    with open(fileName, "r", encoding="utf-8") as f:
        timer = [line.strip() for line in f if line.strip()]
        
    kol = len(timer) 
    
    del timer[int(kol):]

        
    ids_list = timer

    objectID = []
    isPublicDomain = []
    title = []
    artistDisplayName = []
    artistNationality = []
    additionalImages = []
    objectDate = []
    objectBeginDate = []
    objectEndDate = []
    medium = []
    dimensions = []
    classification = []
    creditLine = []
    repository = []
    
    import time
    import requests
    from bs4 import BeautifulSoup

    with requests.Session() as requests:
        requests.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Accept-Encoding": "gzip, deflate",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "en"
        }


    first = time.strftime("%X", time.localtime())

    for i in tqdm(timer):
        
        import time
        import requests
        from bs4 import BeautifulSoup
        
        with requests.Session() as requests:
            requests.headers = {
                "User-Agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
                "Accept-Encoding": "gzip, deflate",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Language": "en"
            }
        
        i = int(timer.index(i))

        a = 0
        while(a==0):

            time.sleep(0.001) 

            url = f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{timer[i]}'
            req = requests.get(url)

            if str(req) == '<Response [200]>':


                obj = req.json()


                objectID.append(obj['objectID'])

                isPublicDomain.append(str(obj['isPublicDomain']))

                title.append(obj['title'])

                artistDisplayName.append(obj['artistDisplayName'])
                artistNationality.append(obj['artistNationality'])
                additionalImages.append(obj['additionalImages'])

                objectDate.append(obj['objectDate'])
                objectBeginDate.append(obj['objectBeginDate'])
                objectEndDate.append(obj['objectEndDate'])

                medium.append(obj['medium'])

                dimensions.append(obj['dimensions'])

                classification.append(obj['classification'])

                creditLine.append(obj['creditLine'])

                repository.append(obj['repository'])

                a = 1

            else: 
                a = 0

    second = time.strftime("%X", time.localtime())
    format = '%H:%M:%S'
    razn = datetime.strptime(second, format) - datetime.strptime(first, format)
    print(f'Execution time - {str(razn)}')

    data = dict({'objectID':objectID,'isPublicDomain':isPublicDomain,'title':title,'artistDisplayName':artistDisplayName,'artistNationality':artistNationality,'additionalImages':additionalImages,'objectDate':objectDate,'objectBeginDate':objectBeginDate,'objectEndDate':objectEndDate,'medium':medium,'dimensions':dimensions,'classification':classification,'creditLine':creditLine,'repository':repository})
    df = pd.DataFrame(data)
    df.to_csv(r'Final file [API].csv', encoding="utf-8", index=False)
    
    
def parsing():
    
    with open(fileName, "r", encoding="utf-8") as f:
        timer = [line.strip() for line in f if line.strip()]
        
    kol = len(timer) 
    
    del timer[int(kol):]

        
    ids_list = timer
    title = []
    author = []
    location = []
    lacation_url = []
    description = []



    import time
    import requests
    from bs4 import BeautifulSoup

    with requests.Session() as requests:
        requests.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Accept-Encoding": "gzip, deflate",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "en"
        }

    first = time.strftime("%X", time.localtime())

    for i in tqdm(timer):

        import time
        import requests
        from bs4 import BeautifulSoup

        with requests.Session() as requests:
            requests.headers = {
                "User-Agent": f"Mozilla/{i}.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
                "Accept-Encoding": "gzip, deflate",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Language": "en"
            }
            
        i = int(timer.index(i))

        url = f'https://www.metmuseum.org/art/collection/search/{ids_list[i]}'
        response = requests.get(url)

        a = 0
        while(a==0):

            time.sleep(0.1) 

            if str(response) == '<Response [200]>':

                soup = BeautifulSoup(response.text, 'html.parser')


                quotes = soup.find_all('span', class_='artwork__title--text')
                for quote in quotes:
                    title.append(quote.text)


                quotes = soup.find_all('p', class_='artwork__creation-origin')
                for quote in quotes:
                    author.append(quote.text.replace("\n", ""))


                quotes = soup.find_all('span', class_='location__onview')
                for quote in quotes:
                    location.append(re.sub('\s+', ' ', str(quote.text)))

                url_map = str(quotes).split('a href="', 1)[-1]
                url_map = url_map.split('=="', 1)[0]
                lacation_url.append(url_map)
                #print(url_map)


                quotes = soup.find_all('div', class_='artwork__intro__desc')
                for quote in quotes:
                    description.append(re.sub('\s+', ' ', str(quote.text)))


                a = 1



            else:
                print('Attempt to connect to the server')
                time.sleep(10) 
                a = 0

    second = time.strftime("%X", time.localtime())
    format = '%H:%M:%S'
    razn = datetime.strptime(second, format) - datetime.strptime(first, format)
    print(f'Execution time - {str(razn)}')

    data = dict({'objectID':ids_list,'title':title,'author':author,'location':location,'lacation_url':lacation_url,'description':description})
    df = pd.DataFrame(data)
    df.to_csv(r'Final file [Parsing].csv', encoding="utf-8", index=False)
                
                



def _onKeyRelease(event):
    ctrl  = (event.state & 0x4) != 0
    if event.state & 4 > 0 and chr(event.keycode) == 'V' and event.keysym == "??": #V
        root.focus_get().event_generate("<<Paste>>")
    if event.state & 4 > 0 and chr(event.keycode) == 'C' and event.keysym == "??": #V #C
        root.focus_get().event_generate("<<Copy>>")  
    if event.state & 4 > 0 and chr(event.keycode) == 'X' and event.keysym == "??": #X
        root.focus_get().event_generate("<<Cut>>") 
    if event.state & 4 > 0 and chr(event.keycode) == 'A' and event.keysym == "??": #A
        root.focus_get().event_generate("<<SelectAll>>")  
root.bind_all("<Key>", _onKeyRelease, "+")




labelframe1 = LabelFrame(root, background="gray", text='Forming a dictionary with ids', bg='#f0f0f0', fg='black', font=("Century Gothic", 12, "bold"), labelanchor="n")
labelframe1.place(in_=root, anchor="c", relx=.50, rely=.30)
 
title_head = Label(labelframe1, text='Request (or leave it empty)', bg='#f0f0f0',fg='black', font=("Century Gothic", 10))
title_head.grid(row=0, column=0, ipadx=0, ipady=0, padx=15, pady=0)
req_Input = Entry(labelframe1, bg='white', font=("Century Gothic", 13, "bold"), justify=CENTER, width=25)
req_Input.grid(row=1, column=0, ipadx=0, ipady=0, padx=15, pady=0)

Button1 = Button(labelframe1, text='Create a file',command=create_a_file, bg='#e4002b',fg='white', height=1, width=25, font=("Century Gothic", 10, "bold"))
Button1.grid(row=2, column=0, ipadx=0, ipady=0, padx=15, pady=10)





labelframe2 = LabelFrame(root, background="gray", text='Select the file, and then the data collection mode', bg='#f0f0f0', fg='black', font=("Century Gothic", 12, "bold"), labelanchor="n")
labelframe2.place(in_=root, anchor="c", relx=.50, rely=.67)

Button2 = Button(labelframe2, text='API',command=api, bg='#e4002b',fg='white', height=1, width=20, font=("Century Gothic", 10, "bold"))
Button2.grid(row=0, column=0, ipadx=0, ipady=0, padx=15, pady=10)


def file_in():
    global fileName
    fileName =filedialog.askopenfilename(filetypes=[("TXT",".txt")])
    #title_file_name2.configure(text=fileName2[:25]+'...'+fileName2[-25:])
    print(f'Selected file: {fileName}')


icon_i = PhotoImage(file="file.png")
photoimage_i = icon_i.subsample(2, 2)
Button3 = Button(labelframe2,image=photoimage_i, command=file_in,bg='#e4002b', height=25, width=25, font=("Century Gothic", 10, "bold"), justify=CENTER)
Button3.grid(row=0, column=1, ipadx=0, ipady=0, padx=0, pady=10) 








Button4 = Button(labelframe2, text='Parsing', command=parsing, bg='#e4002b',fg='white', height=1, width=20, font=("Century Gothic", 10, "bold"))
Button4.grid(row=0, column=2, ipadx=0, ipady=0, padx=15, pady=10)



root.mainloop()
