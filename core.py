from time import sleep
from bs4 import BeautifulSoup

import requests

urlbase = "https://www.coursera.org/search?query="

requirement = input("Enter the name of the course you need to take: ").split()

searchaddon = "%20".join(requirement)

urlbase = urlbase+searchaddon+"&="

print(urlbase)

pageiter = 1

page_iter_count = 1

while page_iter_count <= 12:

    newurlbase = urlbase+"page={0}&index=prod_all_launched_products_term_optimization".format(pageiter)
    print(pageiter,page_iter_count,newurlbase)
    page_iter_count+=1

    urlgetrequest = requests.get(newurlbase).text

    #sleep(100)

    soup = BeautifulSoup(urlgetrequest,"lxml")

    #print(soup.select("div.rc-SearchTabs"))

    #break

    #print(type(soup.prettify()))

    courseslist = soup.find('div',class_='rendered-content')#,class_="cds-63 css-0 cds-65 cds-grid-item cds-110 cds-118 cds-130")

    print(courseslist)

    #page_iter_count = len(courseslist)

    #print("pagecount",page_iter_count)

    #print(pageiter,newurlbase)

    pageiter+=1


