from bs4 import BeautifulSoup as bs
import requests


f = open("demo.html")
soup = bs(f,'html.parser')
soup1 = soup.find_all("a")
print(soup1[1])

#Find all li in the ul(Go through parent)
soup2 = soup.find_all("ul")
for i in soup2:
    data =i.find_all("li")
    for j in data:
        print(j.text)


#Find all table
soup3 = soup.find_all("table")
for i in soup3:
    data =i.find_all("td")
    for j in data:
        print(j.text)


#Find table 3
f1 = open("demo1.html")
soup = bs(f1,'html.parser')
data = soup.find_all("table",{"id":"day3"})
for i in data:
    for j in i.find_all("tr"):
        for k in j.find_all("td"):
            print(k.text)



#Find shoes Title and how much discount is on it

url = "https://www.flipkart.com/search?q=shoes&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
data = requests.get(url)
plain_text = data.text
soup = bs(plain_text,"html.parser")
res1 = soup.find_all("div",{"class":"_3Ay6Sb"})
res2 = soup.find_all("a",{"class":"IRpwTa"})
for i in res1:
    for j in res2:
        print(j.text,":",i.text)


#HW: Fav actor tweet and shoes between 500-1000 with price and title