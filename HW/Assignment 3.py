import json
import requests
url = "https://randomuser.me/api/"
data = requests.get(url)
plain_text = data.text
print(plain_text)
res = json.loads(plain_text)
print("First name:",res["results"][0]["name"]["first"],"   Last Name:",res["results"][0]["name"]["last"])
print("Gender:",res["results"][0]["gender"])
print("Registered date:",res["results"][0]["registered"]["date"])
print("Date of Birth:",res["results"][0]["dob"]["date"])

# Task Questions
# Question 1
di = {"Tom":80,"John":77,"Isla":88,"Emily":95,"Thomas":68}
livalues = []
for j in di.values():
    livalues.append(j)
print(livalues)

for k in livalues:
    if k<=60:
        print("It has scored F grade")
    elif k<=70:
        print("It has scored D grade")
    elif k<=80:
        print("It has scored C grade")
    elif k<=90:
        print("It has scored B grade")
    elif k<=100:
        print("It has scored A grade")

#Question 2
li = [2016,2000,2021,2024]
for i in li:
    if i%4==0:
        print("Its a leap year")
    else:
        print("Its not a leap year")

#Question 3
def pytha():
    a = int(input("Enter the a value:"))
    b = int(input("Enter the b value:"))
    c = int(input("Enter the c value:"))
    d = a**2+b**2
    e = c**2
    if e==d:
        print("Its a pythagorean")
    else:
        print("Its not a pythagorean")
pytha()

#Question 4
string = "Python"
if string[:2]=="Py":
    print("True",string)
else:
    print("Flase")
