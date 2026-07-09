import socket

# --------------------------------------------------
# IP Lookup
# Author: Sakshi Devda
# Description: Resolve a hostname to its IP address
# --------------------------------------------------

print("=" * 40)
print("           IP LOOKUP")
print("=" * 40)

# Get hostname from the user
hostname = input("Enter Hostname (e.g., google.com): ")

try:
    # Resolve hostname to IP address
    ip_address = socket.gethostbyname(hostname)

    print("\nHostname :", hostname)
    print("IP Address:", ip_address)

except socket.gaierror:
    print("\nError: Unable to resolve the hostname.")

print("\nLookup completed successfully!")
