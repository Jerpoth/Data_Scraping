import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

purl='https://www.worldometers.info/world-population/population-by-country/#google_vignette'

pheader={
    'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}

p_resp=rq.get(url=purl,headers=pheader)
print(p_resp.status_code)

soup = BeautifulSoup(p_resp.content,'html.parser')
# print(soup)

# print(soup.find('table').find('tbody').find_all('tr')[0].getText())

Table=soup.find('table').find('tbody').find_all('tr')

Country_list=[]

for rows in Table:
    dic ={}
    
    dic['Country'] = rows.find_all('td')[1].getText()
    dic['Population'] = rows.find_all('td')[2].getText()
    dic['Land Area km^2'] =rows.find_all('td')[6].getText()
    dic['Fert.Rate'] =rows.find_all('td')[8].getText()
    dic['World Share'] =rows.find_all('td')[11].getText()
    



    Country_list.append(dic)

#  print(Country_list[0])


df =pd.DataFrame(Country_list)

print(df)

df.to_csv('Country_population.csv',index=False)
