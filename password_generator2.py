
#TASK2

import random
file = open("password_generator.txt","a")

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


option = "0"
saved = {}

while True:
    print("Hello to Password Generator!")
    print('****************************************')
    print("1. Generate a Password for an account")
    print("2. Get password for an account")
    print("3. Exit")

    option = input("\nPlease enter a number option: ")

    if option == "1":
        account = input("Enter the account name for the generated password: ")
        saved[account] = password_generator()
        print("\n", account, ":", saved[account])

    elif option == "2":
        account = input("\n Enter the name account : ")
        if saved.get(account) == None:
            print("The enter account isn't registrated, please register it first")
        else:
            print(f'{account} : {saved.get(account)}')

    elif option == "3":
        print("Exit")
        break
    else:
        print("\n The number entered is not valid, please enter a valid number")




