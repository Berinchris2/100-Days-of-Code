letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
import random

password_list = ""
password_list_hard = []
for letter in range(0, nr_letters):
    password_list += random.choice(letters)
    password_list_hard.append(random.choice(letters))
for sym in range(0, nr_symbols):
    password_list += random.choice(symbols)
    password_list_hard.append(random.choice(symbols))
for num in range(0, nr_numbers):
    password_list += random.choice(numbers)
    password_list_hard.append(random.choice(numbers))

print (password_list)
random.shuffle(password_list_hard)
Final_password = ""
for hard_password in password_list_hard:
    Final_password += hard_password
print(Final_password)
