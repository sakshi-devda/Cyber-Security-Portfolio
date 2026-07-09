import random
import string

# --------------------------------------------------
# Password Generator
# Author: Sakshi Devda
# Description: Generate a strong random password
# --------------------------------------------------

characters = (
    string.ascii_uppercase +
    string.ascii_lowercase +
    string.digits +
    string.punctuation
)

print("=" * 40)
print("      PASSWORD GENERATOR")
print("=" * 40)

length = int(input("Enter password length: "))

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:")
print(password)

print("\nPassword generated successfully!")
