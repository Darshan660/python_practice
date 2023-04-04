"""
#Question 1
def check(n):
    li = [1,2,6,7,12]
    if (n in li):
        print("Present")
    else:
        print("Absent")
check(7)

#Question 2
def area(r):
    ar = 3.14*(r**2)
    print("Area of the circle is:",ar)
area(4)

#Question 3
def tup():

    sum = 0
    mul = 1
    li = []
    a = int(input("Enter how many element you want to add:"))
    for i in range(1,a+1):
        b = int(input("Enter the"+str(i)+" element into tuple:"))
        li.append(b)
    print(tuple(li))

    for j in tuple(li):
        sum = sum+j
        mul = mul*j
    print(sum)
    print(mul)
tup()


#Question 4
li = [1,1,1,33,22,11,11,22]
a = set(li)
print(a)

#Question 4
a = [1,1,1,33,22,11,22]
b = []
def unique():
    for i in a:
        if i not in b:
            b.append(i)
    print(b)
unique()

#Question 5
def palindrome(n):
    a = n[::-1]
    if n == a:
        print("Its an palindrome")
    else:
        print("Its not a palindrome")
    
palindrome('helleh')

#Question 6 
li = [1,2,3,4,5,6,7,8,9,10,11,12]
def out():
    for i in li:
        if(i%2==0):
            continue
        else:
            print(i**2)
out()

#Question 7
def table(n):
    for i in range(1,n+1):
        print()
        for j in range(1,11):
            mul = i*j
            print(str(i)+"X"+str(j)+"="+str(mul))
table(3)

#Question 8
def prime(num):
        if num >1:
            for i in range(2,int(num/2)+1):
                if (num % i) == 0:
                    print(num, "is not a prime number")
                    break
                else:
                    print(num, "is a prime number")
                    break
        elif num==0:
            print("0 is neither prime nor composite")
        elif num==1:
            print(num, "is not a prime number")
            
prime(1)
"""
a = (1)
print(type(a))

i = 1
while i<=10:
    print(i)
    i = i+1
