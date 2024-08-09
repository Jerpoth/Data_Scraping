import requests as rq
from bs4 import BeautifulSoup
from bs4 import NavigableString
import re

burl ='https://books.toscrape.com/'
bheader ={'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

bresp = rq.get(url=burl, headers=bheader)

print(bresp.status_code)

bsoup = BeautifulSoup(bresp.content,'html.parser')

#print(soup.prettify())

def removenavigablestring(value):
    return list(filter(lambda x : type(x) != NavigableString,value))

bsoup1 = removenavigablestring(bsoup)
# print(bsoup1)

book_element= bsoup.find_all('article')
# print(book)
# print(book[0].find('h3').find('a').attrs['title'])

# title =[booktitle.find('h3').find('a').attrs['title'] for booktitle in book]
# print(title)

# price = book_element[0].find('p',attrs={'class':'price_color'}).getText().split('£')[1]
# print(price)

# rating =book_element[0].find('p').attrs['class'][1]
# print(rating)

def get_book_Title(book):
    return book.find('h3').find('a').attrs['title']

def get_book_Price(book):
    pricetext=book.find('p',attrs={'class':'price_color'}).getText()
    clean_text= re.sub(r"[^\d.]","",pricetext)
    pricevalue = float(clean_text)
    return pricevalue

def get_book_Rating(book):
    rating_chart ={
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5
    }
    rating_text= book.find('p').attrs['class'][1].lower()
    return rating_chart[rating_text]


def get_book_Data(book):
    return {
        'Title': get_book_Title(book),
        'Price': get_book_Price(book),
        'Rating':get_book_Rating(book)
    }

book_data = [get_book_Data(book) for book in book_element ]

print(book_data)


import pandas as pd

book_df=pd.DataFrame(book_data)
# book_df.to_csv('book_df.csv')