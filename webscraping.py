import pandas as pd
from bs4 import BeautifulSoup
import requests
import os
req = requests.get('http://web.mta.info/developers/turnstile.html')
soup = BeautifulSoup(req.text, "html.parser")
def txt_to_pandas(filename):
    p=""
    elements = soup.find_all("div", class_="span-84 last")
    for element in elements:
        links = element.find_all("a")
        for link in links:
            #print(link.text.strip())
            if link.text.strip()==filename:
                link_url = link["href"]
                p="http://web.mta.info/developers/"+link_url
                response = requests.get(p)
                txt = open("C:/Users/21260/Desktop/Master/Python/"+filename+".txt", 'wb')
                txt.write(response.content)
                txt.close()
                p="C:/Users/21260/Desktop/Master/Python/"+filename+".txt"    
    df = pd.read_csv(p)
    return df
print(txt_to_pandas("Saturday, September 03, 2022"))