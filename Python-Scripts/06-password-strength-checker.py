import re

# --------------------------------------------------
# Password Strength Checker
# Author: Sakshi Devda
# Description: Check the strength of a password
# --------------------------------------------------

print("=" * 40)
print("   PASSWORD STRENGTH CHECKER")
print("=" * 40)

# Get password from the user
password = input("Enter your password: ")

score = 0

# Check password length
if len(password) >= 8:
    score += 1

# Check for uppercase letter
if re.search(r"[A-Z]", password):
    score += 1

# Check for lowercase letter
if re.search(r"[a-z]", password):
    score += 1

# Check for digit
if re.search(r"\d", password):
    score += 1

# Check for special character
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1

# Display password strength
print("\nPassword Strength:")

if score <= 2:
    print("Weak Password")

elif score == 3 or score == 4:
    print("Moderate Password")

else:
    print("Strong Password")

print("\nPassword analysis completed successfully!")
