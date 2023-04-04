print('\033[1m'+"--Currency Converter Tool--"+'\033[0m')
# API connection part
import json
import requests
key = "ed724f91f321d929aa4c33403c626f81"
url = "http://data.fixer.io/api/latest?access_key=ed724f91f321d929aa4c33403c626f81&symbols=USD,AUD,CAD,PLN,MXN&format=1"
data = requests.get(url)
plain_text = data.text
res = json.loads(plain_text)
user_input = int(input("Enter the amount in Euros:"))
print() # For spacing in the console so that it looks clean

#Conversion Tool Part
print("Enter the following number to convert the "+str(user_input)+" Euros into:")
print() # For spacing in the console so that it looks clean

i = True
while i is True:
    user_num = int(input("1:US Dollars, 2:Australian dollar, 3.Canadian Dollars, 4:Poland złoty, 5:Mexican Peso:-"))
    if user_num == 1:
        usd = user_input * res['rates']['USD']
        inr = user_input * 73
        print(str(user_input) + " Euro is equal to " + str(usd) + " US dollars and "+str(inr)+"ind rup")
        break

    elif user_num == 2:
        usd = user_input * res['rates']['AUD']
        print(str(user_input) + " Euro is equal to " + str(usd) + " Australian dollars")
        break

    elif user_num == 3:
        usd = user_input * res['rates']['CAD']
        print(str(user_input) + " Euro is equal to " + str(usd) + " Canadian dollars")
        break

    elif user_num == 4:
        usd = user_input * res['rates']['PLN']
        print(str(user_input) + " Euro is equal to " + str(usd) + "Poland złoty")
        break

    elif user_num == 5:
        usd = user_input * res['rates']['MXN']
        print(str(user_input) + " Euro is equal to " + str(usd) + "Mexican Peso")
        break

    else:
        print("Enter a valid number!")

