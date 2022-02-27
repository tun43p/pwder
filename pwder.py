import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=-}{"
lenght = int(input("Enter password lenght: "))
password = ""

for i in range(lenght + 1):
    password += random.choice(chars)

print(password)
