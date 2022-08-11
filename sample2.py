from bs4 import BeautifulSoup
import requests
import urllib.request
import json
import time
import pandas as pd



def maincontrol():

    local_run = True

    if local_run:
        course_df = pd.read_json('courses.json',orient='records')
        specs_dfs = pd.read_json('specializations.json',oreint='records')
    
    else:
        
        algolia_url = "https://lua9b20g37-dsn.algolia.net/1/indexes/test_products?x-algolia-application-id=LUA9B20G37&x-algolia-api-key=dcc55281ffd7ba6f24c3a9b18288499b&hitsPerPage=1000&page="

        #with urllib.request.urlopen(f'{algolia_url}') as url:

        nbhits = 11000 #initialising the nbhits parameter inorder to make sure that initially page is going inside while loop

        pageiter = 1 #initial page is 1

        tempfp = open("samplefile.txt","w") # to clear the backup (since we append inside the file)
        tempfp.write("")

        all_product_list = []

        while nbhits!=0: #goes on till empty page is read

            url = algolia_url+str(pageiter) #add page number to url

            pageurl = urllib.request.urlopen(url)
            
            print(f"Fetching coursera program data on page {pageiter}.")

            
            # pageurl = Request(url,headers={"User-Agent": "Mozilla/5.0"})
            #page_url = urlopen(pageurl)
            
            page_data = json.loads(pageurl.read().decode())
            

            jsonobj = json.dumps(page_data,indent=4,sort_keys=True) #write
            myfile = open('samplefile.txt','a')                     #data to a file for backup
            myfile.writelines(jsonobj)

            #print(jsonobj)

            all_product_list = all_product_list+page_data["hits"]

            nbhits = int(page_data['nbHits'])

            print("Page :",pageiter,nbhits)
            
            #time.sleep(60) #wait for 1 min so no need to put extra load on server

            pageiter+=1 #increment the page

        pg_df = pd.DataFrame.from_dict(all_product_list)

        fd = open("coursedata.txt","w")

        #data cleaning to take only courses and leave out others

        course_data = pg_df.loc[pg_df["entityType"]== "COURSE"].reset_index(drop=True)
        course_data['id'] = course_data.apply(lambda row: row['objectID'].replace('course~',''),axis = 1)
        course_data = course_data.set_index('id')
        courses = course_data.to_dict('index')

        spec_data = pg_df.loc[pg_df["entityType"] == "SPECIALIZATION"].reset_index(drop = True)
        spec_data['id'] = spec_data.apply(lambda row: row["objectID"].replace('s12n~',''),axis=1)
        spec_data = spec_data.set_index('id')
        specs = spec_data.to_dict('index')

        fd.write(json.dumps(specs,indent=4))


        for index,spec_id in enumerate(list(specs.keys())):

            specs[spec_id]['courses'] = []

            spec_row = specs[spec_id]

            slug = spec_row['objectUrl'].replace("/specializations/","")

            spec_url = f"https://www.coursera.org/api/onDemandSpecializations.v1?q=slug&slug={slug}&fields=courseIds,id"

            url = urllib.request.urlopen(spec_url)

            specs_data = json.loads(url.read().decode())

            course_ids = specs_data['elements'][0]['courseIds']

            

            for course_id in course_ids:

                if course_id not in courses:
                    #print(f'Error-{course_id}-not found')
                    pass
                else:
                    if 'specializations' not in courses[course_id].keys():
                        courses[course_id]['specializations'] = []
                    
                    #print(f' -- {courses[course_id]["name"]}')

                    if spec_id not in courses[course_id]['specializations']:
                        courses[course_id]['specializations'] = []
                    
                    if course_id not in specs[spec_id]['courses']:
                        specs[spec_id]['courses'].append(course_id)
            
            specs_dfs = pd.DataFrame.from_dict(specs,orient="index")
            specs_dfs.to_json('specializations.json')

            for index,course_id in enumerate(list(courses.keys())):

                courses[course_id]['price'] = 0

                price_url = f"https://www.coursera.org/api/productPrices.v3/VerifiedCertificate~{course_id}~GBP~GB"

                try:
                    price_data = urllib.request.urlopen(price_url)
                    price_datas = json.loads(price_data.read().decode())
                    courses[course_id]['price'] = price_datas['elements'][0]['amount']
                    print(f'{courses[course_id]["name"]} : price: {courses[course_id]["price"]}')

                except:
                    print(f"error -- {course_id} not found")

            courses_df = pd.DataFrame.from_dict(courses,orient="index")
            courses_df.to_json('courses.json')

if __name__ == "__main__":
    maincontrol()