"""
#Question 1
a = input("Enter the sentence:")
b = a.count(" ")
count = 0
counter = 0

for i in a:
    count+=1
char = count-b
print("Character present in the string are "+str(char))
for i in a:
    if(a==" "):
        counter+=1
    else:
        continue
print(counter)



user_input = input("Enter a string")
word = 1
char = 0
for i in user_input:
    if(i==" "):
        word+=1
    else:
        char = char+1
print("The num of words is",word)
print("The num of char is",char)

# Question 2
li = [1,2,3,4]
add = 0
mul = 1
for i in li:
    add = add+i
    mul = mul*i

print("Addition is:",add)
print("Multiplication is:",mul)

# Break keyword in looping
av = 5
user_input = int(input("Enter how many candies you want?"))
i = 1
while(i<=user_input):
    print("candy",i)
    i = i+1
    if(i>av):
        print("Out of stock")
        break

# Question 3
for i in range(1,100):
    if(i>30):
        break
    else:
        print(i)


# Question 4
domain = "@gmail.com"
a = input("Enter the email:")
for i in a:
    if(i in domain):
        print("Email added is:",a)
    else:
        print("Invalid email")
        break
 
# Question 5
a = input("Enter the email:")
for i in a:
    if (not "@" in a):
       print("Invalid email")
       break
            
    elif (not ".com" in a):
        print("Invalid email")
        break
    else:
        print(a)
        break
      
# Question 6
li = [3,4,2,1,5,64,24,65,6783,35,847,24]
for i in li:
    if(i%2!=0):
        continue
    else:
        print(i)

# Question 7
a = int(input("Enter the range:"))
for i in range(1,a+1):
    i = i*i
    if(i==256):
        continue
    print(i)
 """

# Question 8
    
        
