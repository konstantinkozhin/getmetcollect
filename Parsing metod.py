import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import time
from bs4 import BeautifulSoup
import re




url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects'
req = requests.get(url)
ids = req.json()
ids_list = ids['objectIDs']


objectID = []

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

start_time = time.time()

for i in range(len(ids_list)-24864):
    
    import time
    import requests
    from bs4 import BeautifulSoup
    
    with requests.Session() as requests:
        requests.headers = {
            "User-Agent": f"Mozilla/{i+24864}.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Accept-Encoding": "gzip, deflate",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "en"
        }

    url = f'https://www.metmuseum.org/art/collection/search/{ids_list[i]}'
    response = requests.get(url)

    a = 0
    while(a==0):
        
        time.sleep(0.1) 

        if str(response) == '<Response [200]>':

            soup = BeautifulSoup(response.text, 'html.parser')
            
            objectID.append(i)

            
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

                
            print(i)   
                
            a = 1
            
            

        else:
            print('(')
            time.sleep(1) 
            a = 0
        
print("--- %s seconds ---" % (time.time() - start_time))

data = dict({'objectID':objectID,'title':title,'author':author,'location':location,'lacation_url':lacation_url,'description':description})
df = pd.DataFrame(data)
df.to_csv(r'THEMET2.csv', encoding="utf-8", index=False)