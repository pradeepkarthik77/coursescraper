from bs4 import BeautifulSoup
import requests

baseurl = "https://www.coursera.org/courses?page="


pagecount = 1
course_count = 12

while course_count>=12:

    newurl = baseurl+str(pagecount)+"&index=prod_all_products_term_optimization"

    request_url = requests.get(newurl)

    soup = BeautifulSoup(request_url.content,'html5lib')

    tags = soup('li')

    for tag in tags:
        if tag['class'] == 'cds-9 css-0 cds-11 cds-grid-item cds-56 cds-64 cds-76':
            print("ghi")
    
    break