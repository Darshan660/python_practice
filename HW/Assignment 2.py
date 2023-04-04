"""                                ASSIGNMENT 2                                  """

# Question 1
thirty = ['january','January','march','March','may','May','july','July','august','August','october','October','december','December']
thirtyone = ['april','April','June','june','september','September','november','November']
feb = ['february','February']
a = input("Enter the name of the month(Be careful with the spelling):")
if(a in thirty):
    print("It has 30 days")
elif(a in thirtyone):
    print("It has 31 days")
elif(a in feb):
    print("It has 28 days if leap year than 29")
else:
    print("Enter the proper spelling")

# Question 2
a = int(input("Enter 1 side:"))
b = int(input("Enter 2 side:"))
c = int(input("Enter 3 side:"))
if(a==b and b==c):
    print("Its a Equilateral triangle")
elif(a==b or b==c or a==c):
    print("Its a isosceles triangle")
else:
    print("Its a scalene triangle")

# Question 3

di={}
li1=["name","age","gender"]
li2=["darshan",19,"male"]
i=0
while(i<len(li1)):
    di.update({li1[i]:li2[i]})
    i = i+1
print(di)

# Question 4
li=[]
a = int(input("Enter the number:"))
i = 1
while(i<=a):
    if(a%i==0):
        li.append(i)
        i = i+1
    else:
        i = i+1
print("Factors of",a,"are:",li)

# Question 5
a = int(input("Enter the number up to which you want to print the cube:"))
for i in range(1,a+1):
    print(i*i*i,end=" ")

# Question 6
sum = 0
list = [10,20,30,40,50,60,70,80]
for i in list:
    sum = sum+i
print("The addition of all the elements from the list is:",sum)

# Question 7
si = {1,2,3,4,5,2,4,1,3,5,1,4,3,1,}
b = int(input("Enter how many times you want to add an element in set:"))
for i in range(1,b+1):
    a = int(input("Enter the "+ str(i) +" number you want to add in set:"))
    si.add(a)
print(si)

# Question 8
dict1 = {1:10,2:20}
dict2 = {3:30,4:40}
dict3 = {5:50,6:60}
for i in (dict2,dict3):
    dict1.update(i)
print(dict1)

# Question 9
ceven = 0
codd = 0
list=[12,32,43,643,7,3,64,121,96,43,866,34,78,72,38,90,81,39,56]
for i in list:
    if(i%2==0):
        ceven = ceven+1
    else:
        codd = codd+1
print("There are",ceven,"even numbers and",codd,"odd numbers in the list")

# Question 10
list=[]
b = int(input("Enter how many times you want to add an element in the list:")) 
for i in range(1,b+1):
    a = int(input("Enter the "+ str(i) +" number you want to add in set:"))
    list.append(a*a)
print(list)   

# Question 11
li = ['sam','lisa','dave','tom','john','alex']
for i in li:
    print("Hello",i)
