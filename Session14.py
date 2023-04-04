import json
import requests
"""
key = "0e0c4f2c027b4909b4ae63ce6d671a94"
city = input("Enter:")
url = "https://api.weatherbit.io/v2.0/current?city="+city+"&key="+key
data = requests.get(url)
plain_text = data.text
print(plain_text)
res = json.loads(plain_text)
print(res)
def temp():
    print(res["data"][0]["temp"])
temp()

#Question2
key = "0e0c4f2c027b4909b4ae63ce6d671a94"
city = "san francisco"
url = "https://api.weatherbit.io/v2.0/current?lat=37.7749&lon=-122.4194"+"&key="+key
print(url)
data = requests.get(url)
print(data)
plain_text = data.text
print(plain_text)
res = json.loads(plain_text)
print(res)

def check():
    print("Timezone is:",res["data"][0]["timezone"])
    print("Country Code is",res["data"][0]["country_code"])
    print("Weather is:",res["data"][0]["weather"])
check()
"""
#Question 3
url = "https://www.flipkart.com/search?q=books&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
data = requests.get(url)
print(data)