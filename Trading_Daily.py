

import requests
from bs4 import BeautifulSoup
raw_html = simple_get('http://finance.google.com')
html = BeautifulSoup(html, 'html.parser')
for i, li in enumerate(html.select('li')):
        print(i, li.text)

