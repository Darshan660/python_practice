"""
# SETS
si = {1,2,3,3,4,5,5,5,5,1,1,1,1,8,8,8,8}
si.add("new")

si.update({"demo1","demo2"})

si.remove(3)

si.discard("abc")
print(si)

print(len(si))

# Some dict methods

di = {"name":"hiral","email":"hiral@gmail.com"}
di["name"] = "john"
print(di)

y = di.get("name")
print(y)

di.update({"new-key":"new-val"})
print(di)

di.pop("email")
#You have to mention the key value in pop items if you use pop function in dict
# But if you don't want to use parameters then use popitem function
di.popitem()

print(di)
del di

#arithmetic operators
+
-
*
/
%
// => Floor division
** => Power
# Comparison Operators
==
!=
>
<
>=
<=

#Logical Operators
and
or

x = 5
if(x==5):
    print("X is 5")
elif(x==7):
     print
else:
    print("X ix",x)

"""

# If
"""
# Question 1
x = int(input("Enter a number:"))
if (x==0):
    print("x is not +ve nor -ve")
elif(x>0):
    print("Its +ve")
else:
    print("Its -ve")

# Question 2
n = input("Enter the alphabet:")
vowel = ["a","A","e","E","i","I","o","O","u","U"]
if(n in vowel):
    print("Its a Vowel")
else:
    print("Its a consonent")


# Question 3
a = int(input("Enter 1 num:"))
b = int(input("Enter 2 num:"))
c = int(input("Enter 3 num:"))

if(a>b and a>c):
    print(a,"is the biggest")
elif(b>a and b>c):
    print(b,"is the biggest")
else:
    print(c,"is biggest")

# Question 4
a=int(input("Enter 1 num:"))
b=int(input("Enter 2 num:"))
c=a+b
if(c>=150):
    print("Its greater than 150")
else:
    print("Its smaller than 150")


# Question 5
fname = input("Enter your first name:")
lname = input("Enter your last name:")
if(len(lname)>=13):
    print("Limit Excedeed")
else:
    print("Program Finished")
    

# Question 6
a=int(input("Enter a num:"))
if(a%2==0):
    print("Its Even")
else:
    print("Its Odd")


# Question 7
a=int(input("Enter a num:"))
if(a%3==0 and a%5==0):
    print("Its Divisible by both")
elif(a%5==0):
    print("Its Divisible by 5")
elif(a%3==0):
    print("Its Divisible by 3")
else:
    print("Its not Divisible by both")

"""
