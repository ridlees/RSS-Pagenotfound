#!/bin/python3

import requests as r
from bs4 import BeautifulSoup as bs

url = "https://pagenotfound.cz"

def get(url):
    page = r.get(url)
    return page

def soup(page):
    return bs(page.content, 'html.parser')

class articleEntry:
    def __init__(self, title, ahref, perex):
        self.title = title
        self.ahref = ahref
        self.perex = perex
        

def get_articles():
    entries = []
    PageNotFound = soup(get(url))
    articles = PageNotFound.find_all('article')
    for article in articles:
        
        title = article.find("h2").text
        ahref = url + article.find("a").get("href")
        perex = article.find("p").text
        entry = articleEntry(title, ahref, perex)
        entries.append(entry)
    return entries
    
if __name__ == "__main__":
    articles = get_articles()
    print(articles)
