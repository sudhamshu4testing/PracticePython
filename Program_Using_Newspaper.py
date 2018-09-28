# Program to read news from the website using "newspaper" module
# Install newspaper module using "pip3 install newspaper3k" for python3

from newspaper3k import Article

url = "http://www.eenadu.net/"
article = Article(url)

print (article)
