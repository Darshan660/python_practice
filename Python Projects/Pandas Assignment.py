"""                                                    ---Excercise 1---                                                         """
"""
import pandas as pd
chipo = pd.read_csv("D:\Datasets\Chipotle.csv")
# print("First 10 entries are:-",chipo.head(10))
# print("Number of observations are:-",chipo.shape)
# print("number of columns is:-",chipo.shape[1])
# print("Names of the column are:-",chipo.columns)
# print(chipo['item_name'].value_counts())   #The first one here(Chicken Bowl) is the most ordered item
# print("Number of chicken bowl orderd is:-",chipo['item_name'].value_counts().max())
# print(chipo.groupby(["choice_description"])["choice_description"].count().sort_values(ascending=False))
# print(chipo['quantity'].sum())

chipo['item_price'] = chipo['item_price'].str.replace('$',"",regex=False)
chipo['item_price'] = chipo['item_price'].astype(float)

# print(chipo['item_price'].dtypes)
# chipo['item_price'].apply(lambda x: str(x))
# print(chipo['item_price'].dtypes)

print("Total Revenue is:-",chipo['item_price'].sum())

# print(chipo.groupby(['order_id'])['order_id'].max())  #doubt how to take order id max number like 1834
# print("Average order price is:-",chipo['item_price'].mean())

count=0
for i in chipo['item_name'].value_counts():
    count = count+1
print(count)


#                                                  ---Excercise 2---                                                         

# step 1,2,3,4,5 Done in excercise 1

chipo.drop_duplicates(subset=['item_name','quantity'],keep="first",inplace=True)
print(chipo)

rslt_df = chipo.loc[chipo['quantity'] == 1]
print(rslt_df)

b = chipo.drop_duplicates(subset='item_name').reset_index()
print(b[['item_name','item_price']])


# print(chipo.sort_values(by='item_names'))
 
b1 = chipo.loc[chipo['item_price']==chipo['item_price'].max()]
print(b1)

p = 3.14

class geometry:
    def __init__(self,r,l,b,c):
        self.radius = r
        self.length = l
        self.breadth = b
        self.volume = c

    def area(self):
        print(p*self.radius)

    def area(self):
        print(self.length*self.breadth)

    def volume(self):
        print(self.volume)

g = geometry(8,9,2,1)
g.volume()"""

"""
import pandas as pd
m1 = int(input("Enter data wrangling marks: "))
m2 = int(input("Enter maths marks: "))
m3 = int(input("Enter chemistry marks: "))
m4 = int(input("Enter english marks: "))
m5 = int(input("Enter physics marks: "))

percentage = ((m1+m2+m3+m4+m5)/500)*100

if percentage>=90 and percentage<=100:
    print("Grade is O")
elif percentage>=80 and percentage<=89:
    print("Grade is A+")
elif percentage>=70 and percentage<=79:
    print("Grade is A")
elif percentage>=50 and percentage<=69:
    print("Grade is B")
elif percentage>=35 and percentage<=49:
    print("Grade is A")
else:
    print("Fail")
#2.
v_counter = 0
c_counter = 0
vowels = ['A','a','E','e','I','i','O','o','U','u']
name = input("Enter your name:")
for i in name:
    if i in vowels:
        v_counter += 1
    else:
        c_counter +=1
print("Vowels are:",v_counter)
print("Consonents are:",c_counter)
"""
"""
# Q3
bal = 0
a = int(input("Enter 1 to Open balance, 2 to Deposit, 3 to Withdraw, 4 to Exit:"))
if a==1:
    balance = int(input("Enter your opening balance:"))
    deposit = int(input("Enter the amount to be deposited:"))
    print("Your deposited amount is:","$",deposit,"and Your total balance is:","$",balance+deposit)
    balance = balance+deposit
    withdraw = int(input("Enter the amount to withdraw:"))
    if withdraw>=balance:
        print("Insufficent balance:")
        withdraw = int(input("Enter the amount to withdraw:"))
    else:
        balance = balance-withdraw
        print("Withdraw sucessful and your remaining amount is:",balance)
if a == 2:
    balance = 0
    deposit = int(input("Enter the amount to be deposited:"))
    balance = balance + deposit
    withdraw = int(input("Enter the amount to withdraw:"))
    if withdraw >= balance:
        print("Insufficent balance:")
        withdraw = int(input("Enter the amount to withdraw:"))
        balance = balance - withdraw
        print("Withdraw sucessful and your remaining amount is:", balance)
    else:
        balance = balance - withdraw
        print("Withdraw sucessful and your remaining amount is:", balance)

if a == 3:
    balance = 0
    withdraw = int(input("Enter the amount to withdraw:"))
    if withdraw >= balance:
        print("Insufficent balance")
        withdraw = int(input("Enter the amount to withdraw:"))
        print("Your balance is 0 you cannot withdraw any amount")
    else:
        balance = balance - withdraw
        print("Withdraw sucessful and your remaining amount is:", balance)

if a == 4:
    print("Exited!")
"""

# Kessc@54321 kes password
"""

li = []
n = int(input("Enter how many elements you want to add in a list:"))
for i in range(1,n+1):
    user_input = int(input("Enter "+str(i)+" element in list:"))
    li.append(user_input)
li.sort()
print("After sorting list:",li)
key = int(input("Enter which number you want to find in the list by Binary Search:"))
beg = 0
end = (len(li)-1)
mid = int((beg+end)/2)
while beg<=end:
    counter = 0
    if key==li[mid]:
        print("Element found after "+str(counter)+" Iteration"+str(key))
        break
    elif key>li[mid]:
        mid = mid+1
    elif key<li[mid]:
        mid = mid-1
    counter = counter+1

"""
""" 
# Binary Search
def binary_search(list1,n):
    low = 0
    high = len(list1)-1
    mid = 0
    while low <= high:
        mid = (high + low)//2
        if list1[mid]<n:
            low = mid+1
        elif list1[mid]>n:
            high = mid-1
        else:
            return mid
    return -1

list1 = [12,24,32,39,45,50,54]
n = 45
result = binary_search(list1,n)
if result != -1:
    print("Element is present at index",str(result))
else:
    print("Element is not present")
"""
t = (1,2,3,4,5)
l = list(t)
c = l.sorted()
print(c)
