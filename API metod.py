import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import time
from bs4 import BeautifulSoup


url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects'
req = requests.get(url)
ids = req.json()
#print(ids['total'])
ids_list = ids['objectIDs']
#print(ids_list)

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




with requests.Session() as requests:
    requests.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en"
    }


start_time = time.time()

for i in range(len(ids_list)):
    
    a = 0
    while(a==0):
        
        time.sleep(0.001) 
        
        url = f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{ids_list[i]}'
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
            
            print(i,obj['objectID'])
                        
            a = 1
            
        else: 
            a = 0

print("--- %s seconds ---" % (time.time() - start_time))

data = dict({'objectID':objectID,'isPublicDomain':isPublicDomain,'title':title,'artistDisplayName':artistDisplayName,'artistNationality':artistNationality,'additionalImages':additionalImages,'objectDate':objectDate,'objectBeginDate':objectBeginDate,'objectEndDate':objectEndDate,'medium':medium,'dimensions':dimensions,'classification':classification,'creditLine':creditLine,'repository':repository})
df = pd.DataFrame(data)
df.to_csv(r'THEMET.csv', encoding="utf-8", index=False)