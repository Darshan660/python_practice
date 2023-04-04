#Method overloading
"""

class Addition:
    def add(self,a=None,b=None,c=None,d=None):
        if a!=None and b!=None and c!=None and d!=None:
            s = a+b+c+d
        elif a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        elif a!=None:
            s=a
        else:
            return("Enter a parameter")
        return s
s1 = Addition()
print(s1.add(1,2,3,4))

#Multiplication
class Addition:
    def mul(self,a=None,b=None,c=None,d=None):
        if a!=None and b!=None and c!=None and d!=None:
            s = a*b*c*d
        elif a!=None and b!=None and c!=None:
            s = a*b*c
        elif a!=None and b!=None:
            s = a*b
        elif a!=None:
            s=a
        else:
            return("Enter a parameter")
        return s
s1 = Addition()
print(s1.mul(1,2,3,4))

#
class Info:
    def name(self,n=None):
        a = type(n)
        if a==str:
            if n!=None:
               return(n)
        elif a==int:
            return("Enter string")
        else:
            return("Please enter your name")
s2 = Info()
print(s2.name())

#Method overriding
class Animal:
    def speak(self):
        print("Speaking")
class Dog(Animal):
    def speak(self):
        print("Barking")
d = Dog()
d.speak()

# (__) is prefix for protecting a code, implementation then Abstraction and information hiding then Encapsulation
#Encapsulation = information hiding
class Computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("Selling Price:",(self.__maxprice))

c = Computer()
c.sell()
#Change the price
c.__maxprice = 100
c.sell()
"""
#Pandas
import pandas as pd
data = pd.read_csv("Workbook1.csv")
print(data)
