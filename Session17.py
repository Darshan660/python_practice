"""

class myclass():
    x = 5
s1 = myclass()
print(s1.x)

class computer():
    def config1(darshan):
        print("i5,16gb")
    def config2(self):
        print("i6,18gb")
com1 = computer()
com2 = computer()
computer.config1(com1)
computer.config2(com2)

com1.config1()
com2.config2()


class info():
    def information(self,a,b):
        print("Name:",a,"Contact:",b)
res1 = info()
res1.information("Darshan",7710020979)

class test():
    def __init__(self):
        print("hello")
    def __add__(self):
        print("hey")
p1 = test()
p1.__add__()
p2 = test()
p3 = test()



class person():
    name = input("Enter your name:")
    age = input("Enter your age:")
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = person(name,age)
print(p1.name)
print(p1.age)
p2 = person(name,age)
print(p2.name)
print(p2.age)


students = [
{
'name' : "abc",
'email' : "abc@gmail.com",
'contact' : 1234,
'subject' : "python"
},

{
'name' : "pqr",
'email' : "pqr@gmail.com",
'contact': 1234,
'subject' : "php"
},
    {
'name' : "xyz",
'email' : "xyz@gmail.com",
'contact' : 1234,
'subject': "js"
},
{
'name' : "mno",
'email' : "mno@gmail.com",
'contact' : 1234,
'subject' : "js"
},
{
'name' : "asw",
'email' : "asw@gmail.com",
'contact' : 1234,
'subject' : "python"
}
]

class trycatch():
    def __init__(self,data):
        self.data = data
        length = len(students)
        for i in range(0,length):
            print(students[i]["name"])

res = trycatch(students)

#other method:

class trycatch():
    def __init__(self,data):
        self.data = data
    def info(self):
        for i in students:
            print(i["name"])

res = trycatch(students)
res.info()
"""

students = [
{
'name' : "abc",
'email' : "abc@gmail.com",
'contact' : 1234,
'subject' : "python"
},

{
'name' : "pqr",
'email' : "pqr@gmail.com",
'contact': 1234,
'subject' : "php"
},
    {
'name' : "xyz",
'email' : "xyz@gmail.com",
'contact' : 1234,
'subject': "js"
},
{
'name' : "mno",
'email' : "mno@gmail.com",
'contact' : 1234,
'subject' : "js"
},
{
'name' : "asw",
'email' : "asw@gmail.com",
'contact' : 1234,
'subject' : "python"
}
]
class trycatch():
    def __init__(self,data):
        self.data = data
    def subject(self):
        for i in students:
            if i["subject"]=="python":
                print(i)

res = trycatch(students)
res.subject()


