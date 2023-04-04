import json
from bs4 import BeautifulSoup as bs
import requests

url = "https://www.flipkart.com/search?q=books&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&as-backfill=on"
data = requests.get(url)
print(data)
plain_text = data.text
print(type(plain_text))
#print(plain_text)


soup = bs(plain_text,"html.parser")
res = soup.find_all('a',{'class':'s1Q9rs'})
print(type(res))
for i in res:
    print(i.text)
    print(i.get("title"))
    print("*"*50)

#To print price of flipkart books
soup = bs(plain_text,"html.parser")
res = soup.find_all('div',{'class':"_30jeq3"})
print(type(res))
for i in res:
    print(i.text)
    print("*"*50)
#To print the deal of the day products name
url = "https://www.flipkart.com/"
data = requests.get(url)
plain_text = data.text
print(type(plain_text))

soup = bs(plain_text,"html.parser")
res = soup.find_all('div',{'class':"_3LU4EM"})
print(type(res))
for i in res:
    print(i.text)
    print("*"*50)

#Practice amazon
url = "https://www.amazon.in/b/ref=s9_acss_bw_cg_Budget_1a1_w?node=26851561031&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-3&pf_rd_r=XGH9X6194JXB8PD3DPTT&pf_rd_t=101&pf_rd_p=b85830d5-ce87-470b-89cf-795f9b88c7ff&pf_rd_i=1389401031"
data = requests.get(url)
plain_text = data.text

soup = bs(plain_text,"html.parser")
res = soup.find_all('div',{'class':"DealContent-module__truncate_sWbxETx42ZPStTc9jwySW"})
for i in res:
    print(i.text)
    print("*"*30)
