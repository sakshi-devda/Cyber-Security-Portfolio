# Cryptography Concepts

## 1. Room Information

| Field | Details |
|--------|---------|
| Platform | TryHackMe |
| Learning Path | Pre Security |
| Room Name | Cryptography Concepts |
| Difficulty | Easy |
| Status | Completed |

---

## 2. Objective

The objective of this room is to understand the fundamentals of cryptography, including encryption, decryption, hashing, digital signatures, and the role of cryptography in protecting sensitive information.

---

## 3. Introduction

Cryptography is the practice of securing information by converting readable data into an unreadable format. It helps protect sensitive information from unauthorized access during storage and transmission.

Modern cryptography is widely used in online banking, secure websites, email communication, digital certificates, VPNs, cloud computing, and many other cybersecurity applications.

---

## 4. Key Concepts

### Plaintext

Plaintext is the original, readable data before encryption.

Example:

```
Hello World
```

---

### Ciphertext

Ciphertext is the encrypted form of plaintext that cannot be understood without the correct decryption key.

Example:

```
X7@kP#9Lm!
```

---

### Encryption

Encryption is the process of converting plaintext into ciphertext using an encryption algorithm and a key.

Its primary purpose is to protect the confidentiality of information.

---

### Decryption

Decryption is the process of converting ciphertext back into its original plaintext using the correct decryption key.

---

### Symmetric Encryption

Symmetric encryption uses the **same key** for both encryption and decryption.

Examples:

- AES
- DES

Advantages:

- Fast
- Efficient for large amounts of data

Limitation:

- Secure key sharing can be difficult.

---

### Asymmetric Encryption

Asymmetric encryption uses **two different keys**:

- Public Key
- Private Key

Examples:

- RSA
- ECC

Advantages:

- Secure key exchange
- Supports digital signatures

Limitation:

- Slower than symmetric encryption.

---

### Hashing

Hashing converts data into a fixed-length hash value.

Important characteristics:

- One-way process
- Cannot be reversed
- Used to verify data integrity

Examples:

- SHA-256
- SHA-512

Common uses:

- Password storage
- File integrity verification
- Digital forensics

---

### Digital Signature

A digital signature verifies the authenticity and integrity of digital information.

It provides:

- Authentication
- Integrity
- Non-repudiation

---

### Public Key Infrastructure (PKI)

PKI is a framework used to manage digital certificates and public keys for secure communication.

Common components include:

- Certificate Authority (CA)
- Digital Certificates
- Public Keys
- Private Keys

---

## 5. Practical Activity

In this room, I explored the fundamental concepts of cryptography and learned how encryption, hashing, and digital signatures help secure modern communication and protect sensitive information.

---

## 6. Skills Learned

- Cryptography Fundamentals
- Encryption and Decryption
- Symmetric Encryption
- Asymmetric Encryption
- Hashing
- Digital Signatures
- Public Key Infrastructure (PKI)

---

## 7. Key Takeaways

- Cryptography protects sensitive information from unauthorized access.
- Encryption provides confidentiality.
- Hashing verifies data integrity.
- Digital signatures confirm authenticity and integrity.
- PKI enables secure communication through digital certificates.
- Modern cybersecurity heavily relies on cryptographic technologies.

---

## 8. Screenshots

> Screenshots will be added later.

Suggested screenshots:

- Room Overview
- Encryption Process Diagram
- Hashing Example
- Room Completion

---

## 9. What I Learned

After completing this room, I gained a solid understanding of how cryptographic techniques protect digital information. I learned the differences between encryption, hashing, and digital signatures, as well as the practical role of symmetric and asymmetric encryption in modern cybersecurity.

---

## 10. Conclusion

This room provided a strong foundation in cryptography by explaining the core concepts used to secure digital communication. Understanding encryption, hashing, digital signatures, and PKI is essential for cybersecurity professionals working in network security, cloud security, incident response, and digital forensics.
