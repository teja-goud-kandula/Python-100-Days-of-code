import random

# generated a random integer between inclusive start range and inclusive end range
random_integer = random.randint(1, 10)
print(f"Random integer: {random_integer}")

# generates a random floating number between 0.0 inclusive and exclusive 1
random_0_to_1 = random.random()
print(f"Random 0 to 1: {random_0_to_1}")

# generates a random floating number between 0.0 inclusive and exclusive 10
random_0_to_10 = random.random() * 10
print(f"Random 0 to 10: {random_0_to_10}")

