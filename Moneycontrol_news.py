from bs4 import BeautifulSoup
import requests


url = "https://www.moneycontrol.com/news/business/markets"
web_data = requests.get(url)
web_data.encoding = 'utf-8'
web_text = web_data.text

soup = BeautifulSoup(web_text, "html.parser")


all_h2=soup.select(selector="h2 a") 
for h2 in all_h2:
    link=h2.get("href")
    title=h2.get("title")
    print(f"{title} \nfor more refrence go directly on website:{link}\n\n")







