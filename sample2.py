from bs4 import BeautifulSoup
import requests
import urllib
import json
import time

algolia_url = "https://lua9b20g37-dsn.algolia.net/1/indexes/test_products?x-algolia-application-id=LUA9B20G37&x-algolia-api-key=dcc55281ffd7ba6f24c3a9b18288499b&hitsPerPage=1000&page="

#with urllib.request.urlopen(f'{algolia_url}') as url:

nbhits = 1000

pageiter = 1

while nbhits!=0:

    url = algolia_url+str(pageiter)

    pageiter+=1

    pageurl = urllib.request.urlopen(url)
    
    print(f"Fetching coursera program data on page .")
    
    page_data = json.loads(pageurl.read().decode())

    jsonobj = json.dumps(page_data,indent=4,sort_keys=True)

    myfile = open('samplefile1.txt','w')
    myfile.writelines(jsonobj)

    #print(jsonobj)

    nbhits = int(page_data['nbHits'])
    print("Page :",pageiter,nbhits)
    #time.sleep(30)