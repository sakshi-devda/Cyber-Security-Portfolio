# Port Scanner

## 1. Project Information

| Field | Details |
|--------|---------|
| Project | Port Scanner |
| Language | Python |
| Difficulty | Beginner |
| Category | Cybersecurity Utility |
| Status | Completed |

---

## 2. Objective

The objective of this project is to create a Python program that scans a target system for open ports. Open ports indicate which network services are running and accepting connections.

---

## 3. Introduction

A Port Scanner is a cybersecurity tool used to identify open ports on a target device. Every network service communicates through a specific port number. By scanning these ports, security professionals can determine which services are active and identify potential security risks.

Port scanning is one of the first steps performed during network enumeration and vulnerability assessment.

---

## 4. Python Module Used

### socket

The `socket` module is used to establish network connections between devices. It allows the program to test whether a specific port on a target host is open or closed.

---

## 5. Working Principle

The program works as follows:

1. The user enters the target IP address or hostname.
2. The program scans a range of port numbers.
3. It attempts to establish a connection to each port.
4. If the connection is successful, the port is marked as open.
5. If the connection fails, the port is considered closed.
6. All open ports are displayed to the user.

---

## 6. Features

- User-friendly interface
- Scans a range of TCP ports
- Displays open ports
- Uses Python's socket module
- Beginner-friendly implementation

---

## 7. Applications

This project can be used for:

- Network Enumeration
- Security Auditing
- Service Discovery
- Vulnerability Assessment
- Cybersecurity Learning

---

## 8. How to Run

1. Open the project in Visual Studio Code.
2. Open the terminal.
3. Run the following command:

```bash
python 03-port-scanner.py
```

4. Enter the target IP address.
5. View the list of open ports.

---

## 9. Output

> Output screenshots will be added later.

Suggested screenshots:

- Running the program
- Port scanning process
- Open ports displayed in the terminal

---

## 10. What I Learned

After completing this project, I learned how to:

- Use the socket module
- Scan TCP ports
- Identify open network ports
- Understand basic network communication
- Build a simple cybersecurity tool using Python

---

## 11. Conclusion

This project introduced the fundamentals of port scanning using Python. It demonstrated how network services can be identified through open ports and provided practical experience with Python networking concepts that are commonly used in cybersecurity.
