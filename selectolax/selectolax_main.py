

from utile.selectolax_basic import getDatafromUrl
from utile.selectolax_basic import book_Rating
from selectolax.parser import HTMLParser

bUrl = 'https://books.toscrape.com/'

if __name__ == "__main__":
    htmlPage = getDatafromUrl(bUrl)
    tree = HTMLParser(htmlPage)

    
    book_list = tree.css("article.product_pod")
    
    for book in book_list:
        
        title = book.css_first("h3 > a ").attributes['title']
        
        price = book.css_first("p.price_color").text()
        
        text_rating = book.css_first("p.star-rating").attributes['class'].split()[-1]
        rating = book_Rating(text_rating)
        
        print('-----')
        print('Title:', title)
        print('Price:', price)
        print('Rating:', rating)