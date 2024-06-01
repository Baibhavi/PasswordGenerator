import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
specified_letter = input("Do you want to specify the number of Capital and small letters in the password? Write 'y' for yes and 'n' for no ")
if specified_letter ==  'y':
  nr_capital = int(input("How many capital letters would you like in your password?\n"))
  nr_small = int(input("How many small letters would you like in your password?\n"))
elif specified_letter == 'n':
  nr_letters = int(input("Okay then, just specify the number of letters you want in your password."))
else:
  print("Please write 'y' or 'n' ")

nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

if(specified_letter == 'y'):
    for char in range(1, nr_capital + 1):
        password += random.choice(capital)
    for char in range(1, nr_small + 1):
        password += random.choice(small)
else:
  for char in range(1, nr_letters + 1):
    password += random.choice(letters)


for char in range(1, nr_symbols + 1):
  password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password += random.choice(numbers)


type_of_password = input("Do you want a hard password or an easy password?\nIn easy password will follow the order: letters, symbols, numbers.\nIn hard password there will be no order among letters, symbols and numbers.\nType 'y' for yes and 'n' for no")

#Hard Level
if type_of_password == 'y':
   random.shuffle(password)
elif type_of_password != 'n' and type_of_password != 'y':
   type_of_password = input("Invalid input")
   

final_password = ""
for char in password:
  final_password += char

print(f"Your password is: {final_password}")