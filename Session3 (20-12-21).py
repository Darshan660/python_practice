"""

# Length of list:
list = [1,2,3,4,5,6,7,8,9]
print(len(list))

# List Manipulation:

li = ["john","tom","alex","demo1","demo2","demo3","demo4","test"]
li[3:7] = ["newdata1","newdata2","newdata3","newdata4"]
print(li)

li1 = [1,2,3,4,5]
li1.insert(0,"new")

li1.append("demo1")
print(li1)

li3 = ["hey"]
li4 = ["hello"]
li4.extend(li3)
print(li4)

li5 = ["abc","pqr","xyz"]
li5.remove("pqr")
print(li5)

li6 = ["abc","pqr","xyz","mno","asw","hgy"]
li6.pop()
li6.pop(2)
print(li6)

li7 = ["abc","pqr","xyz","mno","asw","hgy"]
data = li7.index("mno")
print(data)

li8 = ["abc","pqr","xyz","mno","asw","hgy"]
del li8[0]
li8.clear()
print(li8)

li9 = ["a","b","c"]
li9.reverse()
print(li9)

#1 Question
a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))
c = int(input("Enter number 3:"))
li = [a,b,c]
print(li)

#2 Question
fname = input("Enter first name:")
lname = input("Enter last name:")
li1 = [fname]
li2 = [lname]
li1.extend(li2)
print(li1)


#3 Question
n = input("Enter the number:")
li = [1,2,4,5]
li.insert(2,n)
print(li)


# TUPLES :
ti = (1,2,3,4,5,6,7,8,9)
print(ti[0:5])

#1 Question
ti = (1,2,3,4,5,6,7,8,9)
li = list(ti)
li.append("new")
ti = tuple(li)
print(ti)

#2 Question
a = int(input("Enter 1 num:"))
b = int(input("Enter 2 num:"))
c = int(input("Enter 3 num:"))
d = a+b+c
t = (d,)
print(t)


#its parameter dependent
ti1 = (11,12,13)
(a,b,c) = ti1
print(a)

#unpacking
ti1 = (11,12,13,14,15,16,17,18)
(a,b,*c) = ti1
print(c)


ti2 = ("a","b","c","a","p","a")
res = ti2.count("a")
print(res)

# DICTONARY
di = {"name":"john","email":"john@gmail.com","age":12}
print(di["email"])"""

di1 = {"data1":{"std_name":"alex","num":1234},"data2":{"std_name":"tom","num":7676,"email":"tom@gmail.com"}}
print(di1["data1"]["num"])
print(di1["data2"]["email"])

di1 = {"data1":{"std_name":"alex","num":1234},"data2":{"std_name":["tom","ram","shyam"],"num":7676,"email":"tom@gmail.com"}}
print(di1["data2"]["std_name"][1])








