import socket

# --------------------------------------------------
# Network Scanner
# Author: Sakshi Devda
# Description: Scan a range of IP addresses and
#              identify active hosts.
# --------------------------------------------------

print("=" * 40)
print("        NETWORK SCANNER")
print("=" * 40)

# Get the network prefix from the user
network = input("Enter Network Prefix (Example: 192.168.1): ")

print("\nScanning Network...")
print("-" * 40)

# Scan IP addresses from .1 to .10
for i in range(1, 11):

    ip = f"{network}.{i}"

    try:
        hostname = socket.gethostbyaddr(ip)
        print(f"{ip} : Active ({hostname[0]})")

    except socket.herror:
        print(f"{ip} : Inactive")

print("-" * 40)
print("Network scan completed successfully!")
