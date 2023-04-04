"""
#Time module

import time
id_num = "hello123"
i = 1
while True:
    id_check = input("Enter your ID:")
    if(id_check == id_num):
        print("Hey! Welcome")
        break
    elif(i == 3):
        print("Sorry try again after 10sec")
        time.sleep(10)
        i = 1
    elif(id_check != id_num):
        print("Try Again")
        i = i+1
print("Outside the loop")


# Regular Expression(password question)
import re
p = input("Enter your password")
x = True
while x:
    if(len(p)<6 or len(p)>12):
        break
    elif not(re.search("[A-Z]",p)):
        break
    elif not(re.search("[a-z]",p)):
        break
    elif not(re.search("[0-9]",p)):
        break
    elif not(re.search("[@#$^%]",p)):
        break
    else:
        x = False
        print("Valid Password")

if x:
    print("Not a valid password")


# FUNCTIONS
def hello():
    print("Hey how are you?")
hello()

def add(x,y):
    c = x+y
    print(c)
add(4,5)
add(7383,893)
add(74,987)

#Question 1
def merge(a,b):
    a = input("Enter your first name:")
    b = input("Enter your last name:")
    print(a+b)
merge('darshan','kholakiya')

#Question 2
#Not Working
def largest(a):
    li=[]
    a = int(input("Enter how many elements you want to add in the list:"))
    for i in range(1,a):
        b = int(input("Enter the"+str(i)+"number:")
        li.append(b)
    for i in li:
        if(li[i] > max):    
         max = li[i];
    print("The biggest number in the listr is",max)

largest(5)
       
#Working code
def largest(a):
    li=[]
    a = int(input("Enter how many elements you want to add in the list:"))
    for i in range(1,a):
        b = int(input("Enter the"+str(i)+"number:"))
        li.append(b)
    li.sort()
    print("The largest elemnt is",li[-1])

largest(5)


# Return Type
def add(a,b):
    c = a+b
    return c
res = add(4,5)
print(res)
 """

# Question 
def greatest(a,b,c):
    if(c>b and c>a):
        max_value = c
    elif(b>c and b>a):
        max_value = b
    elif(a>b and a>c):
        max_value = a
    return max_value
res = greatest(70,3,67)
print(res)

