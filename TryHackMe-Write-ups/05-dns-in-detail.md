# DNS in Detail

## 1. Room Information

| Field | Details |
|--------|---------|
| Platform | TryHackMe |
| Learning Path | Pre Security |
| Room Name | DNS in Detail |
| Difficulty | Easy |
| Status | Completed |

---

## 2. Objective

The objective of this room is to understand the Domain Name System (DNS), how domain names are translated into IP addresses, and the role of DNS in network communication.

---

## 3. Introduction

The Domain Name System (DNS) is often called the "phonebook of the Internet." Humans remember domain names such as **google.com**, while computers communicate using IP addresses. DNS translates domain names into IP addresses so that devices can locate and communicate with each other over the Internet.

Without DNS, users would need to remember numerical IP addresses for every website they visit.

---

## 4. Key Concepts

### What is DNS?

DNS (Domain Name System) is a distributed naming system that converts domain names into IP addresses.

Example:

- google.com → 142.250.x.x
- github.com → 140.82.x.x

---

### Domain Name

A domain name is the human-readable address of a website.

Examples:

- google.com
- tryhackme.com
- microsoft.com

---

### IP Address

An IP address is the unique numerical identifier assigned to a device on a network.

DNS resolves a domain name into its corresponding IP address.

---

### DNS Resolver

A DNS Resolver receives a user's DNS query and works to find the correct IP address by contacting other DNS servers if needed.

---

### Root DNS Server

The Root DNS Server is the first step in the DNS lookup process. It directs the resolver to the appropriate Top-Level Domain (TLD) server.

---

### Top-Level Domain (TLD)

The TLD server manages domains based on their extensions.

Examples:

- .com
- .org
- .net
- .edu

---

### Authoritative DNS Server

The Authoritative DNS Server stores the official DNS records for a domain and returns the final IP address.

---

## 5. Common DNS Record Types

### A Record

Maps a domain name to an IPv4 address.

---

### AAAA Record

Maps a domain name to an IPv6 address.

---

### CNAME Record

Creates an alias for another domain name.

---

### MX Record

Specifies the mail server responsible for receiving emails.

---

### NS Record

Identifies the authoritative name servers for a domain.

---

### TXT Record

Stores text-based information such as domain verification and email security configurations.

---

## 6. DNS Lookup Process

A typical DNS lookup follows these steps:

1. The user enters a domain name in the browser.
2. The DNS Resolver receives the query.
3. The Resolver contacts the Root DNS Server.
4. The Root Server refers the Resolver to the appropriate TLD Server.
5. The TLD Server directs the Resolver to the Authoritative DNS Server.
6. The Authoritative Server returns the correct IP address.
7. The browser connects to the destination server using that IP address.

---

## 7. Practical Activity

In this room, I explored how DNS works, learned the purpose of different DNS servers, understood common DNS record types, and followed the complete DNS resolution process.

---

## 8. Skills Learned

- DNS Fundamentals
- Domain Name Resolution
- DNS Lookup Process
- DNS Record Types
- Network Communication Basics

---

## 9. Key Takeaways

- DNS translates domain names into IP addresses.
- DNS makes the Internet easier to use by eliminating the need to remember IP addresses.
- Multiple DNS servers work together during the lookup process.
- DNS records provide different types of information required for network communication.
- Understanding DNS is essential for both networking and cybersecurity.

---

## 10. Screenshots

> Screenshots will be added later.

Suggested screenshots:

- Room Overview
- DNS Lookup Diagram
- DNS Record Types
- Room Completion

---

## 11. What I Learned

After completing this room, I gained a solid understanding of how DNS operates behind the scenes whenever a website is accessed. I also learned how different DNS servers cooperate during name resolution and why DNS is one of the most important services on the Internet.

---

## 12. Conclusion

This room provided a comprehensive introduction to the Domain Name System and explained how domain names are resolved into IP addresses using a structured hierarchy of DNS servers. Understanding DNS is essential for network troubleshooting, security analysis, and cybersecurity investigations.
