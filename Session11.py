"""
#Question 1
def divadd(a,b):
    try:
        c = a+b
        d = a-b
        e = c/d
        print("Answer is:",e)
    except:
        print("Error")
    finally:
        print("Hey its finally")
divadd(8,'saj')

# LAMBDA Anonymous function

f = lambda a : a*a
r = f(5)
print(r)

#Question 2
try:
    f = lambda a,b : (a+b)/(a-b)
    r = f(2,2)
    print(r)
except:
    print("Error")

#FILTERS
#filter(functionality,kispe apply karni hai voh)
def even(n):
    return n%2==0
num = [1,2,3,4,5,6,8,9]
even_num = list(filter(even,num))
print(even_num)

#Same code of above using lambda
print(list(filter(lambda n : n%2==0,range(1,11))))


#Question 3
li = ["Hey","Hello","Python"]
for i in li:
    if len(i)>=5:
        print(i)

print(list(filter(lambda a : len(a)>=5,li)))

a = ["hi","hello","Python"]
b = list(map(lambda b : len(b)>5,a))

#Question 4
a = [1,2,3,4,5,6]
print(list(map(lambda c : c*5,a)))
"""
#Question
data =[
{
   'id':1,  
   'name':"abc"  
},
{
   'id': -2,
   'name':"pqr"
},
{
   'id': -1,
   'name':"xyz"
},
{
   'id': 2,
   'name':"mno"
}]
"""
def check(a):
    return a
print(list(map(check,data)))

#Same step of above but in one line:
print(list(map(lambda b: b,data)))


print(list(filter(lambda c : data.key()>=0,data)))
"""


