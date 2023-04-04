import json

di = {"name":"abc","age":12}
print(type(di))

a1 = json.dumps(di)
print(type(a1))
a2 = json.dumps(1234)
print(type(a2))
a3 = json.dumps((1,2,3,4))
print(type(a3))
a4 = json.dumps([1,2,3,4])
print(type(a4))
a5 = json.dumps(1.12243)
print(type(a5))
a6 = json.dumps(True)
print(a6)
a7 = json.dumps(False)
print(a7)
a8 = json.dumps(None)
print(a8)

import requests
url = 'https://reqres.in/api/users'
data = requests.get(url)
print(data)
plain_text = data.text
print(plain_text)

print(type(plain_text))
res = json.loads(plain_text)
print(res)
print(type(res))

for i in res["data"]:
    print("Id 1 email:",i["email"])
