#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
gen_letters = random.sample(letters, nr_letters)
gen_numbers = random.sample(numbers, nr_numbers)
gen_symbols = random.sample(symbols, nr_symbols)

password = []
for letter in gen_letters:
    password += letter
for symbol in gen_symbols:
    password += symbol
for number in gen_numbers:
    password += number

#Solution #1
random.shuffle(password)

pswd = ""
for passwrd in password:
    pswd += passwrd
print(f"Your password is: {pswd}")

# Solution #2
# This is solution 2 - Testing Push
# total_entries = nr_letters + nr_numbers + nr_symbols
# rand_pass = random.sample(password,total_entries)

# pswd = ""
# for paswd in rand_pass:
#   pswd += paswd
# print(pswd)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
