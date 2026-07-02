# OSI Model

## 📌 What is the OSI Model?

The OSI (Open Systems Interconnection) Model is a conceptual framework that explains how data is transmitted between devices over a network.

It divides the communication process into **7 layers**, where each layer performs a specific function.

---

## 🎯 Why is the OSI Model Important?

- Standardizes network communication.
- Makes troubleshooting easier.
- Helps understand how data flows across a network.
- Provides a foundation for networking and cybersecurity.
- Used to identify the layer where a network issue occurs.

---

# 🌐 The 7 Layers of the OSI Model

| Layer Number | Layer Name | Main Function |
|-------------|------------|---------------|
| 7 | Application | Provides network services to users and applications |
| 6 | Presentation | Data formatting, encryption, and compression |
| 5 | Session | Establishes, manages, and terminates sessions |
| 4 | Transport | Ensures reliable data delivery |
| 3 | Network | Routing and logical addressing |
| 2 | Data Link | Physical addressing and error detection |
| 1 | Physical | Transmits raw bits over the network |

---

## Layer 7 – Application Layer

### Purpose

Provides network services directly to end users and applications.

### Examples

- HTTP
- HTTPS
- FTP
- SMTP
- DNS

---

## Layer 6 – Presentation Layer

### Purpose

Converts data into a readable format.

Responsibilities:

- Encryption
- Decryption
- Compression
- Data translation

---

## Layer 5 – Session Layer

### Purpose

Creates, maintains, and terminates communication sessions between devices.

Example:

A video call remains active because the Session Layer manages the connection.

---

## Layer 4 – Transport Layer

### Purpose

Ensures reliable and complete data delivery.

Protocols:

- TCP
- UDP

Responsibilities:

- Segmentation
- Flow control
- Error recovery

---

## Layer 3 – Network Layer

### Purpose

Determines the best path for data to travel.

Key Components:

- IP Address
- Routers

Protocol:

- IP (Internet Protocol)

---

## Layer 2 – Data Link Layer

### Purpose

Transfers data between devices on the same network.

Key Components:

- MAC Address
- Switches

Responsibilities:

- Error detection
- Frame transmission

---

## Layer 1 – Physical Layer

### Purpose

Transmits raw bits over physical media.

Examples:

- Ethernet cable
- Fiber optic cable
- Wi-Fi signals

---

## 📡 Data Flow in the OSI Model

When data is sent:

Application

↓

Presentation

↓

Session

↓

Transport

↓

Network

↓

Data Link

↓

Physical

At the receiving device, the process happens in reverse.

---

## 🛡️ OSI Model in Cybersecurity

Security professionals use the OSI Model to:

- Troubleshoot network issues
- Identify attack locations
- Analyze network traffic
- Investigate security incidents
- Understand protocol behavior

Examples:

- Layer 3 → IP spoofing
- Layer 4 → TCP SYN Flood Attack
- Layer 7 → SQL Injection, Cross-Site Scripting (XSS)

---

## 💼 Real-World Example

When you open a website:

1. Application Layer creates the HTTP request.
2. Presentation Layer encrypts the data (HTTPS).
3. Session Layer manages the connection.
4. Transport Layer sends data using TCP.
5. Network Layer routes packets using IP.
6. Data Link Layer delivers frames using MAC addresses.
7. Physical Layer transmits the bits over the network.

---

## ⭐ Best Practices

- Understand the role of each layer.
- Learn common protocols associated with each layer.
- Use the OSI Model for network troubleshooting.
- Know common attacks targeting different layers.

---

## ❓ Interview Questions

### 1. What is the OSI Model?

### 2. How many layers are there in the OSI Model?

### 3. Which layer is responsible for routing?

### 4. Which layer uses IP addresses?

### 5. Which layer uses MAC addresses?

### 6. What is the difference between the Transport Layer and the Network Layer?

### 7. Why is the OSI Model important in cybersecurity?

---

## 🎯 Key Takeaway

The OSI Model is a seven-layer framework that explains how data travels across a network. Understanding each layer helps in network troubleshooting, protocol analysis, and cybersecurity investigations.
