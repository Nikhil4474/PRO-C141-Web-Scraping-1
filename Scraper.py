from turtle import st
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import requests

# Url:

Bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

webpage = requests.get(Bright_stars_url)


beautisoup = bs(webpage.text, 'html.parser')

#  Convert webapge to HTML
tablefinder = beautisoup.find('table')

# Time all table elements
temp = []
table_rows = tablefinder.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp.append(row)
print("Test", temp)

stars_name = []
distance_of_stars = []
mass_of_stars = []
radius_of_stars = []

for i in range(1, 2):
    stars_name.append(temp[i][1])
    distance_of_stars.append(temp[i][3])
    mass_of_stars.append(temp[i][5])
    radius_of_stars.append(temp[i][6])

dataframe = pd.DataFrame(list(zip(stars_name, distance_of_stars, mass_of_stars, radius_of_stars)), columns=['Star_name', 'Distance', 'Mass', 'Radius'])
print(dataframe)

dataframe.to_csv('bright_stars.csv')