import hashlib

# --------------------------------------------------
# Hash Generator
# Author: Sakshi Devda
# Description: Generate SHA-256 hash of user input
# --------------------------------------------------

print("=" * 40)
print("        HASH GENERATOR")
print("=" * 40)

# Take input from the user
text = input("Enter text: ")

# Generate SHA-256 hash
hash_value = hashlib.sha256(text.encode())

# Display the hash
print("\nSHA-256 Hash:")
print(hash_value.hexdigest())

print("\nHash generated successfully!")
