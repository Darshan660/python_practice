import requests
import json
from bs4 import BeautifulSoup as bs
url = "https://www.flipkart.com/search?q=shoes&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY"
data = requests.get(url)
plain_text = data.text
soup = bs(plain_text,"html.parser")
res = soup.find_all("div",{"class":"_30jeq3"})
res1 = soup.find_all("a",{"class":"IRpwTa"})
for j in res1:
    for i in res:
        a = i.text
        b = a.replace("₹","")
        c = b.replace(",","")
        c = int(c)
        if c>=500 and c<=1000:
            print(j.text,":",c)
