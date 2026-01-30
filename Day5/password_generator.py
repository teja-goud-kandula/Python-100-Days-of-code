import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
no_of_letters = int(input("How many letters do you want in the password?"))
no_of_numbers = int(input("How many numbers do you want in the password?"))
no_of_symbols = int(input("How many symbols do you want in the password?"))

password = []
for i in range(no_of_letters):
    password.append(random.choice(letters))


for i in range(no_of_numbers):
    password.append(random.choice(numbers))

for i in range(no_of_symbols):
    password.append(random.choice(symbols))

print(password)
# shuffle the items of the list
random.shuffle(password)
print(password)
# join the items of the list and create a string out of it
password = ''.join(password)
print(password)
