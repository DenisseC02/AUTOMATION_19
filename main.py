#Task 1 PasswordGnerator
#chars > 8 and chars <=16
#at least one capital letter
#At least une  number (0-9)
#At least one lower letter



import random

uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = uppercase_letters.lower()
numbers = '0123456789'

upper, lower, nums = True, True, True
all = ''

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += numbers

lenght = 16
amount = 1


for x in range(amount):
    password = ''.join(random.sample(all, lenght))
    print(password)
