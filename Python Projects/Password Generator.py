import random
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz@#$&"  #The password would contain the mixture of this letters, numbers and symbols
password_length = int(input("Enter the length of the password:"))
ans = "".join(random.sample(password,password_length))
print(f"Your password is: {ans}")