# Loops
#if we want to work with sequence we use loop
"""
# While loop
#Question 1
i = 5
while(i>0):
    print("darshan",i)
    i = i-1

#Question 2
i=10
while(i<=100):
        print(i)
        i = i+10
# Question3
i=1
while(i<=10):
        print(i*19)
        i = i+1

# Question 4
i=1
while(i<=5):
    print(i*"*")
    i = i+1

# Question 5
i=5
while(i>=1):
    print(i*"*")
    i = i-1

# Question 6
i = 1
while (i<=3):
    a = 5
    while(a<=7):
        print(i,a)
        a = a+1
        i = i+1
        
# QUestion 7
list = ['abc','xyz','pqr']
while(i<len(list)):
    print(list[i])
    i = i+1

# Question 8
name = input("Enter your name:")
i = 0
while(i < len(name)):
    print(name[i])
    i = i+1

# Question 9
a = int(input("Enter 1 num:"))
b = int(input("Enter 2 num:"))
c = int(input("Enter 3 num:"))
list=[a,b,c]
i = 0
while(i<len(list)):
    ans = list[i]*2
    print(ans)
    i = i+1

# For loop
# Question 1
name = input("Enter your name:")
vowel = ['a','e','i','o','u','A','E','I','O','U']
for i in name:
    if(i in vowel):
        print(i)

# Question 2
a = int(input("Enter 1 num:"))
b = int(input("Enter 2 num:"))
c = int(input("Enter 3 num:"))
list=[a,b,c]
for i in list:
    if(i%2==0):
        print(i,"is even")
    else:
        print(i,"is odd")
"""      
# Question 3
name = input("Enter your name:")
counter = 0
for i in name:
    counter = counter+1
print("The length of the string is",counter)
    
    
        
   
