import json
import requests
url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo"
data = requests.get(url)
plain_text = data.text
res = json.loads(plain_text)

for i in res["Time Series (Daily)"].values():
        print(i["2. high"])



