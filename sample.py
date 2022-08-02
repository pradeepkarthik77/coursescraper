from bs4 import BeautifulSoup
import requests

html_text = requests.get("http://www.coursera.org/courses").text 

soup = BeautifulSoup(html_text,"lxml")

print(type(soup))

mainer = soup.find_all("main",class_="rc-SearchPage css-ws691w")

tager = soup.select("li")

print(mainer)
    
