#TASK2

import random

def password_generator():

    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    numbers = "0123456789"

    upper, lower, nums = True, True, True
    all = " "

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += numbers

    lenght = 16
    amount = 1

    for x in range(amount):
        password = "".join(random.sample(all,lenght))
    return password


    #print(password)

password_generator()

option = "0"
saved = {}

while option != 3:
    print("Hello to Generate Pasword!")
    print("1. Password generator")
    print("2. Get password")
    print("3. Exit")

    option = input("Enter a option: ")

    if option == "1":
        account = input("Enter the account name for the generated password: ")
        saved[account] = password_generator()
        print("\n", account, ":", saved[account])

    elif option == "2":
        account = input("\n Enter the name of the account you want to get the password for: ")
        if account in saved:
            print("\n", account, ":", saved[account])
        else:
            print("\n", "The account entered does not exist")

    elif option == "3":
        pass

    else:
        print("\n The number entered is not valid, please enter a valid number")








