from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

import requests

# Making a GET request
r = requests.get('https://www.imdb.com/chart/toptv')

# check status code for response received
# success code - 200
#print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
movies=[]
s = soup.find('tbody', class_='lister-list')
content = s.find_all('tr')
for i in range(len(content)):
    title_col=content[i].find('td','titleColumn')
    rating_col = content[i].find('td', 'ratingColumn imdbRating')
    title=title_col.find('a').text
    rating=rating_col.find('strong').text
    print(title)
    print(rating)
    print("------------------------------")
#print(content)
