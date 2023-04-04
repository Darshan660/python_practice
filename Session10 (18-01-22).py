"""
# Calling function outside the function(Recusrsion oustide the function)
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print("For add=1 sub=2 mul=3 div=4")
user_choice = int(input("Enter Your Choice:"))
num1 = int(input("Enter 1st Num:"))
num2 = int(input("Enter 2nd Num:"))
if(user_choice == 1):
    print(num1,"+",num2,"=",add(num1,num2))
    
elif(user_choice == 2):
    print(num1,"-",num2,"=",sub(num1,num2))

elif(user_choice == 3):
    print(num1,"*",num2,"=",mul(num1,num2))

elif(user_choice == 4):
    print(num1,"/",num2,"=",div(num1,num2))

else:
    print("Sorry wrong input")


#Question 1
n = int(input("Enter a num:"))
li = [1,2,3,4,5]
def find():
    mul = 1    
    for i in li:
        mul = mul*i
    return mul
    
if(n in li):
    print(find())
else:
    print("Number not found in the list") 

# Question 2

url = input("Enter the url:")
def check():
    count = 0
    for i in url:
        if i == ".":
            count += 1
    if count>2:
        print("Wrong")
    else:
        print(url)
check()


#Try Catch
try:
    print(x)
except:
    print("Hello")
   
#Question 3
try:
    def div(a,b):
        c = a/b
        print("Ans of div is",c)

    div(5,0)
except:
    print("Cannot put zero")
"""
#Question 3
age = input("Enter your age:")
try:
    print("My age is ",int(age))
except:
    print("Dont enter a string")

    
        


