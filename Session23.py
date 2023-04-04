import re
"""
def check():
    password = '1agdA*$#'
    reg = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?!.*\s).{4,8}$"
    pattern = re.compile(reg)
    ans = re.search(pattern,password)
    if ans:
        print("Password is valid.")
    else:
        print("Password is invalid!!")
check()

#email
def check():
    password = 'joe@aol.com'
    exp = "^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$"
    pattern = re.compile(exp)
    ans = re.search(pattern,password)
    if ans:
        print("Password is valid.")
    else:
        print("Password is invalid!!")
check()

# This regular expression will match a hyphen-separated Social Security Number (SSN) in the format NNN-NN-NNNN.
def check():
    password = '333-22-4444'
    exp = "^\d{3}-\d{2}-\d{4}$"
    pattern = re.compile(exp)
    ans = re.search(pattern,password)
    if ans:
        print("Password is valid.")
    else:
        print("Password is invalid!!")
check()


#String with no space,number and special char
def check():
    password = 'darshan'
    exp = "^[a-zA-Z]+$"
    pattern = re.compile(exp)
    ans = re.search(pattern,password)
    if ans:
        print("Password is valid.")
    else:
        print("Password is invalid!!")
check()

#This expression matches a hyphen separated US phone number, of the form ANN-NNN-NNNN, where A is between 2 and 9 and N is between 0 and 9.
def check():
    password = '800-555-5555'
    exp = "^[2-9]\d{2}-\d{3}-\d{4}$"
    pattern = re.compile(exp)
    ans = re.search(pattern,password)
    if ans:
        print("Password is valid.")
    else:
        print("Password is invalid!!")
check()

#String Methods
#1. Strip
str1 = " hello  ".strip()
print(str1)

str2 = "@###he#llo##1#".strip('#@1')
print(str2)

str3 = "wwaw.example.coam".strip("ewcaom")
print(str3)

#2 lstrip() rstrip()
str4 = "  hello  ".lstrip()
print(str4)

str5 = "  hello  ".rstrip()
print(str5)

#3. remove prefix()
str6 = "hello how are you?".removeprefix("hello")
print(str6)
str7 = "hello how are you?".removesuffix("you?")

#
str = "Aαβγ".casefold()
print(str)

str8 = "Bαβγ".lower()
print(str8)

firstString = "der Fluß"
secondString = "der Fluss"

# ß is equivalent to ss
if firstString.casefold() == secondString.lower():
    print('The strings are equal.')
else:
    print('The strings are not equal.')
"""

"""
string = ["darshan","yash","fena"]
def upper(string):
    return string.upper()
print(list(map(upper,string)))


def even(n):
    if n%2==0:
        return True
    return False

list = [1,2,3,4,5,6,7,8,9]
print(list(filter(list,even)))

li= ["demigod","rewire","madam"]

def isplaindrome(i):
    if (i==i[::-1]) :
        return True
    else:
        return False

print(list(filter(isplaindrome,li)))
"""

