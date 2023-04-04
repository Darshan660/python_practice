print('\033[1m'+"--Leap Year Detection System--"+'\033[0m')
#So for a year to be leap year it should satisfy 2 conditions
#1. Year should be divisible by 4
# And if its divisible by 4 and a century year then

#2. It should be divisible by 400

year = int(input("Enter the year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Its a leap year")
        else:
            print("Its not a leap year")
    else:
        print("Its a leap year")
else:
    print("Its not a leap year")

