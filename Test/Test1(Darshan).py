"""
#Question 1
li = [2,4,23,54,13,87,47,1]
for i in li:
    print(i**2)

#Question 2
for i in range(1,11):
    print()
    for j in range(1,11):
        print(str(i),"X",str(j),"=",i*j)

#Question 3
li1 = [1,2,3,4,5]
li2 = [6,7,8,9,10]
li1.append(li2)
print(li1)

#Question 4
for i in range(-10,0):
    print(i)

#Question 5
li = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
li1 = ["h", "i", "j"]
li[2][1][2].extend(li1)
print(li)

#Question 6
mul = 1
li = [1,2,3,4,5,6,7,8,9]
for i in li:
    mul = mul*i
print(mul)

#Question 7
a = {'data':[{'name':'student1','email' : 'student1@gmail.com'},
{'name':'student2','email' : 'student2@gmail.com'}]}
print(a["data"][0]["name"],"-",a["data"][0]["email"])
print(a["data"][1]["name"],"-",a["data"][1]["email"])

#Question 8

A=[1,2,3,4,5]
B=['a','b','c','d','e']
d = {}
for i in range(len(A)):
    d[A[i]] = B[i]
print(d)


#Question 9
tu = (1,2,8,4,5)
li = list(tu)
li[2] = 3
print(li)
"""
#Qustion 10
