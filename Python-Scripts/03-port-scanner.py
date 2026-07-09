import socket

# --------------------------------------------------
# Port Scanner
# Author: Sakshi Devda
# Description: Scan TCP ports on an authorized host
# --------------------------------------------------

print("=" * 40)
print("         PORT SCANNER")
print("=" * 40)

# Get target from the user
target = input("Enter Target IP Address or Hostname: ")

print("\nScanning target:", target)
print("-" * 40)

# Scan ports 1 to 1024
for port in range(1, 1025):

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.5)

    result = scanner.connect_ex((target, port))

    if result == 0:
        print(f"Port {port}: Open")

    scanner.close()

print("-" * 40)
print("Scan completed successfully!")
