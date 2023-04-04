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
"""
#1.
class trycatch():
    def info(self):
        print(list(map(lambda x:x['subject'],students)))
res = trycatch()
print(res.info())

#2.
class trycatch():
    def info(self):
        print(list(filter(lambda x:x['subject']=='js',students)))
res = trycatch()
print(res.info())

#3.
li = [1,2,3,4,5,6,7,8,9,10]
class trycatch():
    def info(self):
        print(list(map(lambda x:x*5,li)))

res = trycatch()
res.info()

# INHERITANCE:-
class animal():
    def __init__(self):
        print("Cat is ready")
    def whoisthis(self):
        print("This is cat")
class cat(animal):
    def __init__(self):
        print("tom is ready")
    def whoisthis(self):
        print("This is tom")
        super().whoisthis()
cat1 = cat()
cat1.whoisthis()

#When to use constructor:- if we want to use external data or we want to use for multiple purpose then use __init__
#QUESTION(doubt)
li = [{'name': 'cocker spaniel', 'height': 4, 'weight': '40kg'}, {'name': 'pug', 'height': 2, 'weight': '15kg'},
          {'name': 'bull dog', 'height': 3, 'weight': '30kg'}]
class dog():
    def __init__(self,data):
        self.data = data

class breed(dog):
    def __init__(self,data):
        super().__init__(data)
        for i in li:
            if i['name']=='pug':
                print(i)

res = breed(li)
"""
class Employee:
    count = 0;
    def __init__(self):
        Employee.count = Employee.count+1
    def display(self):
        print("The number of employee:",Employee.count)
emp = Employee()
emp2 = Employee()
try:
    print(emp.count)
except:
    emp.display()


class Employee:
    __count = 0;
    def __init__(self):
        Employee.__count = Employee.__count+1
    def display(self):
        print("The number of employee:",Employee.__count)
emp = Employee()
emp2 = Employee()
try:
    print(emp.__count)
except:
    emp.display()
