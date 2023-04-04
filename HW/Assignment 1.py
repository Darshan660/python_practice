"""                             Assignment 1                       """

# Question 1
tu = (2,3,4,5)
(a,b,c,d) = tu
print(a*b*c*d)

# Question 2
tu1 = ( "banana","apple","mango")
print(type(tu1))
string = str(tu1)
print(type(string))

# Question 3
que = ("an","a","the","a","a","the","a","the","a")
print(que.count("a"))

# Question 4
a = {"name":["john","tom","taylor","kat","alex"]}
rev = a["name"]
print(rev[::-1])

# Other method

a = {"name":["john","tom","taylor","kat","alex"]}
rev = a["name"]
rev.reverse()
print(rev)

"""
This Code is not working, the output is coming:- (None)
a = {"name":["john","tom","taylor","kat","alex"]}
rev = a["name"]
print(rev.reverse())
"""

# Question 5
b = {"contact_No":[2345526739,3457689456]}
print(b["contact_No"][1])

# Question 6
b = {'data':[{"name":"student1","email":"student1@gmail.com"},{"name":"student2","email":"student2@gmail.com"}]}
print(b["data"][0]["name"])
print(b["data"][0]["email"])
print(b["data"][1]["name"])
print(b["data"][1]["email"])

