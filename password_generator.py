import random
import string

print("Password Generator")
print("Choose password strength:")
print("1 - Weak (letters only)")
print("2 - Medium (letters and numbers)")
print("3 - Strong (letters, numbers, and symbols)")

choice = input("Enter your choice (1/2/3): ")
length = int(input("Enter desired password length: "))

if choice == "1":
    characters = string.ascii_letters
elif choice == "2":
    characters = string.ascii_letters + string.digits
elif choice == "3":
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid choice. Defaulting to strong password.")
    characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for _ in range(length):
    password += random.choice(characters)

print("Generated Password:", password)
