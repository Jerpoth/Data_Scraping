# from utile.selectolax_basic import getDatafromUrl
# from selectolax.parser import HTMLParser

# bUrl = 'https://books.toscrape.com/'


# def getBookName(book):
#     return ''


# if __name__ == "__main__":
#     htmlPage = getDatafromUrl(bUrl)
#     print(htmlPage)
#     tree = HTMLParser(htmlPage)

#     arTitle =  tree.css_first("h3 a").attributes['title']
#     arPrice = tree.css_first("p.price_color").text
#     print('-----')
#     print('-----')
#     print('-----',arTitle)
#     print('\n')
#     print('-----',arPrice)


from utile.selectolax_basic import getDatafromUrl
from selectolax.parser import HTMLParser

bUrl = 'https://books.toscrape.com/'

if __name__ == "__main__":
    htmlPage = getDatafromUrl(bUrl)
    tree = HTMLParser(htmlPage)

    
    first_book = tree.css_first("article.product_pod")
    
    if first_book:
        
        title = first_book.css_first("h3 a").attributes['title']
        
        
        price = first_book.css_first("p.price_color").text()
        
        
        rating = first_book.css_first("p.star-rating").attributes['class'].split()[-1]
        
        print('-----')
        print('Title:', title)
        print('Price:', price)
        print('Rating:', rating)