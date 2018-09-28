#Program to collect the data from a website

#Importing requests, Requests is the only Non-GMO HTTP library for Python, safe for human consumption.
import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com/'
ttl_lst = []

soup = BeautifulSoup(requests.get(url).text)
title = soup.findAll('h2', {'class': 'story-heading'})
for row in title:
     ttl_lst.append(row.text)

print (ttl_lst)