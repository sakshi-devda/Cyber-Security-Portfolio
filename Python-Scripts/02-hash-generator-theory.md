# Hash Generator

## 1. Project Information

| Field | Details |
|--------|---------|
| Project | Hash Generator |
| Language | Python |
| Difficulty | Beginner |
| Category | Cybersecurity Utility |
| Status | Completed |

---

## 2. Objective

The objective of this project is to create a Python program that generates cryptographic hash values for user-provided text. This helps in understanding how hashing is used to verify data integrity and securely store information.

---

## 3. Introduction

Hashing is the process of converting data into a fixed-length string called a hash value (or digest). Unlike encryption, hashing is a one-way process, meaning the original data cannot be recovered from the hash.

Hashing is widely used in cybersecurity for password storage, file integrity verification, digital forensics, and digital signatures.

---

## 4. Python Module Used

### hashlib

The `hashlib` module provides secure hash algorithms such as:

- MD5
- SHA-1
- SHA-224
- SHA-256
- SHA-384
- SHA-512

For this project, SHA-256 is used because it is more secure than older algorithms like MD5 and SHA-1.

---

## 5. Working Principle

The program works as follows:

1. The user enters a text message.
2. The program converts the text into bytes.
3. The SHA-256 algorithm generates a hash value.
4. The generated hash is displayed on the screen.

---

## 6. Features

- User-friendly interface
- Uses SHA-256 hashing
- Fast execution
- Demonstrates one-way hashing
- Beginner-friendly code

---

## 7. Applications

This project can be used for:

- Password hashing
- File integrity verification
- Digital forensics
- Cybersecurity learning
- Understanding cryptographic concepts

---

## 8. How to Run

1. Open the project in Visual Studio Code.
2. Open the terminal.
3. Run the following command:

```bash
python 02-hash-generator.py
```

4. Enter any text.
5. View the generated SHA-256 hash.

---

## 9. Output

> Output screenshots will be added later.

Suggested screenshots:

- Running the program
- Generated SHA-256 hash

---

## 10. What I Learned

After completing this project, I learned how to:

- Use the hashlib module
- Generate SHA-256 hashes
- Convert strings into bytes
- Understand one-way hashing
- Apply hashing concepts in cybersecurity

---

## 11. Conclusion

This project introduced the fundamentals of cryptographic hashing using Python. It demonstrated how SHA-256 generates a fixed-length hash from user input and highlighted the importance of hashing in protecting data integrity and supporting secure cybersecurity practices.
