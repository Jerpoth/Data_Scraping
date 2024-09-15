
import re

def extract_number(text):
    number =re.findall(r'\d+',text)
    return[int(num) for num in number]

