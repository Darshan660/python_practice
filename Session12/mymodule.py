"""
#Question 1
def abc(name):
    print("Hello",name)
di = {"name":"john","age":12,"Email":"john@gmail.com"}

#Question 2
li = [1,2,3,4,5]

def list():
        return li

    
#Question 3

def check(n):
    count = 0
    li = [1,32,5,2,6,7,2,3,1,1,1]
    for i in li:
       if (i==n):
          count+=1
    print(n,"has occured",count,"times")


#Question 4
def greater(li):
    (a,b,c) = li
    a = max(li)
    return a
"""
#Question 5
def multiply(li):
    print(list(filter(lambda x : x>5,li)))
    print(list(map(lambda a:a*5,li)))

    
