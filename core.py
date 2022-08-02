from time import sleep
from bs4 import BeautifulSoup

import requests

urlbase = "https://www.coursera.org/search?query="

requirement = input("Enter the name of the course you need to take: ").split()

searchaddon = "%20".join(requirement)

urlbase = urlbase+str(searchaddon)+"&="

print(urlbase)

pageiter = 1

page_iter_count = 1

while page_iter_count <= 12:

    newurlbase = urlbase+"page={0}&index=prod_all_launched_products_term_optimization".format(pageiter)
    print(pageiter,page_iter_count,newurlbase)
    page_iter_count+=1

    html_text = requests.get(newurlbase).text

    soup = BeautifulSoup(html_text,"lxml")

    print(soup.prettify())

    break

    #answer = soup.find_all("div",class_="css-1j8ushu")

    #print(len(answer))

    pageiter+=1


