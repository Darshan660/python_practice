"""
#Recurssion Function
li = []
def guess_the_num():
    ans = 55
    guess = int(input("Enter the number:"))
    if(guess>ans):
        print("Greater")
        li.append(guess)
        print(li)
        guess_the_number()
    elif(guess<ans):
        print("Less")
        li.append(guess)
        print(li)
    elif(guess == ans):
        print("Right Ans")
        li.append(guess)
        print(li)
guess_the_number()

#Question 1
li = []
def guess_the_number():
    ans = 55
    guess = int(input("Enter the number:"))
    if(guess>ans):
        print("Greater")
        li.append(guess)
        print(li)
        guess_the_number()
    elif(guess == ans):
        print("Right Ans")
        li.append(guess)
        print(li)    
    elif(guess>=50 and guess<=60):
        print("Very Close")
        li.append(guess)
        print(li)
        guess_the_number()        
    elif(guess<ans):
        print("Less")
        li.append(guess)
        print(li)
        guess_the_number()
    
guess_the_number()

# Question 2
def fact(n):
        if(n==0):
            return 1
        elif(n<0):
            return 'Enter a greater value than 0'
        else:   
            return n*fact(n-1)
        
res = fact(-2)
print(res)
"""

