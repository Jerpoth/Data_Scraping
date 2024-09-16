from playwright.sync_api import sync_playwright

def getDatafromUrl(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless = False)

        page = browser.new_page()

        page.goto(url)
        page.wait_for_load_state('networkidle')
        htmlpage = page.inner_html('body')

        return htmlpage
    

def book_Rating(rating):
    match rating.lower():
        case 'one':
            return 1
        case 'two':
            return 2
        case 'three':
            return 3
        case 'four':
            return 4
        case 'five':
            return 5
        case _:
            return 0
        
    