from bs4 import BeautifulSoup
import requests
import urllib
import json
import time






def maincontrol():

    algolia_url = "https://lua9b20g37-dsn.algolia.net/1/indexes/test_products?x-algolia-application-id=LUA9B20G37&x-algolia-api-key=dcc55281ffd7ba6f24c3a9b18288499b&hitsPerPage=1000&page="

    #with urllib.request.urlopen(f'{algolia_url}') as url:

    nbhits = 11000 #initialising the nbhits parameter inorder to make sure that initially page is going inside while loop

    pageiter = 1 #initial page is 1

    json_objects = []

    while nbhits!=0: #goes on till empty page is read

        url = algolia_url+str(pageiter) #add page number to url

        pageurl = urllib.request.urlopen(url)
        
        print(f"Fetching coursera program data on page {pageiter}.")
        
        page_data = json.loads(pageurl.read().decode())


        jsonobj = json.dumps(page_data,indent=4,sort_keys=True) #write
        myfile = open('samplefile.txt','a')                     #data to a file for backup
        myfile.writelines(jsonobj)

        #print(jsonobj)

        json_objects.append(page_data)

        nbhits = int(page_data['nbHits'])

        print("Page :",pageiter,nbhits)
        
        #time.sleep(60) #wait for 1 min so no need to put extra load on server

        pageiter+=1 #increment the page

    

if __name__ == "__main__":
    maincontrol()