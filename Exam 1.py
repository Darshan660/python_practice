"""

#Question1
li = [5,3,2,5,77,4,2,1]
lis=[]
for i in li:
    a = i**2
    lis.append(a)
print(lis)
 
#Question2
for i in range(1,11):
    print()
    for j in range(1,11):
        mul = i*j
        print(str(i)+"X"+str(j)+"="+str(mul))
   
#Question3
li1 = [1,2,3,4,5,6,7,8]
li2 = []
for i in li1:
    li2.append(i)
print(li2)

#Question4
for i in range(-10,0):
    print(i)

#Question5  NOT DONE
li = ['a', 'b', ['c', ['d', 'e', ['f', 'g',], 'k'], 'l'], 'm', 'n']
li1 = ["h", "i", "j"]
a = li[2][1][2]
li.insert(a,"h")
print(li)

#Question6
mul = 1
li = [1,2,3,4,5,6]
for i in li:
    mul = i*mul
print("Multiplication of the all element in list is:",mul)

#Question7 NOT DONE
a = {'data':[{'name':'student1','email' : 'student1@gmail.com'},
{'name':'student2','email' : 'student2@gmail.com'}]}
a['data']['name']
print(a)

#Question8   Not Done
li1 = [1,2,3,4,5]
li2 = [6,7,8,9,10]
li1.append(li2)
dict(li1)
print(dict)


#Question9
tu = (1,2,3,4,5)
a = list(tu)
a.pop()
a.append(50)
tunew = tuple(a)
print("Tuple before changed:",tu)
print("Tuple after changed:",tunew)

#Question10
def odd(n):
    for i in range(n+1):
        if(i%2!=0):
            print(i,end=" ")
odd(81)

#Question11
def palindrome(str):
    reverse = str[::-1]
    if(str == reverse):
        print("Its a palindrome")
    else:
        print("Its not an palindrome")
palindrome('hsaeh')

#Question12
import time as t
user_id = input("Enter the user id:")
if(len(user_id)>=3):
    t.sleep(5)
    print("Sleep mode run perfectly")
else:
    ("User input is less than 3")
"""

