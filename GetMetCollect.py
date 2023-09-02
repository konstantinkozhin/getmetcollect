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

import base64

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


icon = b'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'

icondata= base64.b64decode(icon)
tempFile= "icon.ico"
iconfile= open(tempFile,"wb")
iconfile.write(icondata)
iconfile.close()
root.wm_iconbitmap(tempFile)
os.remove(tempFile)

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


        time.sleep(0.001) 

        url = f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{timer[i]}'
        req = requests.get(url)

        url2 = f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{timer[i]}'
        req2 = requests.get(url2)

        if str(req) == '<Response [200]>' and str(req) == '<Response [200]>':


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


        else: continue
                    
                

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
            
        time.sleep(0.001) 
            
        i = int(timer.index(i))

        url = f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{timer[i]}'
        req = requests.get(url)

        url2 = f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{timer[i]}'
        req2 = requests.get(url2)

        if str(req) == '<Response [200]>' and str(req) == '<Response [200]>':
 

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



        else: continue


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


img = b'iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAASpJREFUWEftmP0RgjAMxfM2cRNlEnUSYRJlEtlEN4mXO/A4sB9phZaj/bd97Y9Hk+YCynwgcz7aPiAzX4joGOF0A+Adqrc6yMw3IqpDN+91AleFQhoBmflARK9IuEEeDGkDlF97708QF1slrLgve0RBegMCaDSAhuuhdnJtQPlGFWQKQBVkKkBvyJSAXpCpAZ2QOQAK5BXA41eWWAzQlZImaagAugybzRcH1ZZNBPt2kJmfRHRSutgBqAbNog5uAVDqRCloNUMc/JZsizqooTKtLYCxLu7bwS1EcfZ5sKSZIQhLwbpaog5ofbhS5bg1ElTyy1sr0ap9c11gs3kAxqvmar9JtI4bQOrDPQS1re/j7LAys9R9Z4+DQpa0ADqb0AkYcuo/NQUw1s0PN8RWOM6qcpQAAAAASUVORK5CYII='


icon_i = PhotoImage(data = img)
photoimage_i = icon_i.subsample(2, 2)
Button3 = Button(labelframe2,image=photoimage_i, command=file_in,bg='#e4002b', height=25, width=25, font=("Century Gothic", 10, "bold"), justify=CENTER)
Button3.grid(row=0, column=1, ipadx=0, ipady=0, padx=0, pady=10) 








Button4 = Button(labelframe2, text='Parsing', command=parsing, bg='#e4002b',fg='white', height=1, width=20, font=("Century Gothic", 10, "bold"))
Button4.grid(row=0, column=2, ipadx=0, ipady=0, padx=15, pady=10)


def on_enter(e): title_version3['fg'] = 'gray'
def on_leave(e): title_version3['fg'] = '#f0f0f0'
title_version3 = Label(root, text='powered by Konstantin Kozhin', bg='#f0f0f0',fg='#f0f0f0', font=("Century Gothic", 9),justify=CENTER)
title_version3.place(in_=root, anchor="c", relx=.50, rely=.92)
title_version3.bind("<Enter>", on_enter)
title_version3.bind("<Leave>", on_leave)


root.mainloop()
