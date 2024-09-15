from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd
import requests


with sync_playwright() as sp:
    browser = sp.chromium.launch(headless=True)
    page=browser.new_page()
    page.goto('https://www.flipkart.com')
    search_text = page.wait_for_selector('input[title="Search for Products, Brands and More"]')
    search_text.type('laptop')
    search_text.press('Enter')
    page.wait_for_timeout(3000)


    visited_urls = set()

    while True:
        for link in page.locator('a[class="CGtC98"]').all():
            p = browser.new_page(base_url="https://www.flipkart.com/")
            url = link.get_attribute("href")
            visited_urls.add(url)
            
            # p.goto(url)
            if url is not None:
                p.goto(url)
                p.wait_for_load_state('networkidle')
            else:
                p.close()

            

            content = p.content()
            soup = BeautifulSoup(content, 'html.parser')
            # print(soup)
            Model_name =soup.find('span',attrs={'class':'VU-ZEz'}).text
            price = soup.find('div',attrs={'class':'Nx9bqj CxhGGd'}).text
            Rating = soup. find('div',attrs={'class':'XQDdHH'}).text
            print(f'Model Name : {Model_name} \n')
            print(f'Price Rate : {price} \n ')
            print(f'Rating : {Rating} \n ')
            print("--------done---------")
     
            p.close()
           
        
            

        if url in visited_urls:
             break
    
            
        