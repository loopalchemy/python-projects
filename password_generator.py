import random
import string

print("Password Generator")

length = int(input("Enter desired password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for _ in range(length):
    password += random.choice(characters)

print("Generated Password:", password)
