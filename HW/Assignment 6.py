book_store = [
{
'id':'001',
'title':'Introduction to computer',
'description':'IT' ,
'publish date':'12-07-2011',
'price':'1999',
'author':'Amit Garg',
'status':'Available'
},
{
'id':'002',
'title':'Pride and Prejudice',
'description':'Novel',
'publish date':'08-04-2021',
'price':'899',
'author':'Henry Fielding',
'status':'Available'
},
{
'id':'003',
'title':'The Red and the Black',
'description':'Novel',
'publish date':'19-08-2017',
'price':'799',
'author':'Stendhal',
'status':'Available'
},
{
'id':'004',
'title':'Wings of Fire ',
'description':'Autobiography' ,
'publish date':'18-10-2002',
'price':'215',
'author':'Arun Tiwari',
'status':'Available'
},
{
'id':'005',
'title':'Origins of Marvel Comics',
'description':'Comic',
'publish date':'22-01-2020',
'price':'279',
'author':'Stan Lee',
'status':'Not Available'
}
]
# 1.
print("1.All Books name are:")
for i in book_store:
    print(i['title'])

print("*"*50)

#2.
print("2.Get books according to author name")
for i in book_store:
    print(i['title'],":",i['author'])

print("*"*50)

#3.
print("3. Get details of a particular book according to the name or id:")
for i in book_store:
    print(i['title'],":",i['id'])

print("*"*50)

#4.
print("4. Get all books whose status is available and price is less than 300:")
for i in book_store:
    c = int(i['price'])
    if i['status']=='Available' and c<=300:
        print(i['status'],":",i['id'])

print("*"*50)

#5.
print("5. Get sum of books price")
sum = 0
for i in book_store:
    a = int(i['price'])
    sum = a+sum
print("Sum price for all the books is: Rs.",sum)

print("*"*50)

#6.
print("6. Get sum of books price whose price is greater than 500")
sum = 0
for i in book_store:
    a = int(i['price'])
    if a>=500:
        sum = a+sum
print("Sum price for all the books is: Rs.",sum)

print("*"*50)
