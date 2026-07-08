# Data Encoding

## 1. Room Information

| Field | Details |
|--------|---------|
| Platform | TryHackMe |
| Learning Path | Pre Security |
| Room Name | Data Encoding |
| Difficulty | Easy |
| Status | Completed |

---

## 2. Objective

The objective of this room is to understand how data encoding works, why encoding is used, and how different encoding standards allow computers to exchange and interpret information correctly.

---

## 3. Introduction

Data encoding is the process of converting information into a standardized format so that it can be stored, transmitted, and interpreted correctly by different systems.

Unlike encryption, encoding is **not** intended to protect data. Its primary purpose is compatibility and efficient data exchange between devices and applications.

Encoding is widely used in web technologies, email communication, file transfers, programming, networking, and cybersecurity.

---

## 4. Key Concepts

### What is Data Encoding?

Data encoding converts data into a specific format that can be understood by computers or communication systems.

It helps ensure that information is transmitted accurately across different platforms.

---

### ASCII

ASCII (American Standard Code for Information Interchange) is one of the earliest character encoding standards.

It represents letters, numbers, punctuation marks, and control characters using numerical values.

Example:

- A → 65
- B → 66
- a → 97

---

### Unicode

Unicode is a universal character encoding standard designed to represent characters from almost every written language.

Unlike ASCII, Unicode supports multilingual text, symbols, and emojis.

---

### UTF-8

UTF-8 (Unicode Transformation Format – 8-bit) is the most widely used Unicode encoding format on the Internet.

Advantages:

- Supports all Unicode characters
- Backward compatible with ASCII
- Efficient storage for English text
- Commonly used by websites and applications

---

### Base64 Encoding

Base64 converts binary data into readable ASCII characters.

It is commonly used for:

- Email attachments
- API communication
- Web applications
- JSON and XML data
- Encoding images and files

Base64 is **not encryption** and provides **no security**.

---

### Encoding vs Encryption

| Encoding | Encryption |
|----------|------------|
| Converts data into a standard format | Protects data from unauthorized access |
| Easily reversible | Requires a decryption key |
| Used for compatibility | Used for confidentiality |
| No security provided | Provides data protection |

---

## 5. Practical Activity

In this room, I explored different encoding standards and learned how computers represent and exchange text and binary data using formats such as ASCII, Unicode, UTF-8, and Base64.

---

## 6. Skills Learned

- Data Encoding Fundamentals
- ASCII
- Unicode
- UTF-8
- Base64 Encoding
- Encoding vs Encryption

---

## 7. Key Takeaways

- Encoding ensures data can be stored and transmitted correctly.
- ASCII is suitable for basic English characters.
- Unicode supports characters from multiple languages.
- UTF-8 is the most commonly used character encoding on the Internet.
- Base64 improves compatibility but does not secure data.
- Encoding and encryption serve completely different purposes.

---

## 8. Screenshots

> Screenshots will be added later.

Suggested screenshots:

- Room Overview
- ASCII Example
- Base64 Example
- Room Completion

---

## 9. What I Learned

After completing this room, I learned how different encoding standards help computers exchange information reliably. I also understood the differences between ASCII, Unicode, UTF-8, and Base64, and why encoding should not be confused with encryption.

---

## 10. Conclusion

This room provided a clear understanding of data encoding techniques and their role in modern computing. The concepts covered are essential for networking, programming, web technologies, digital forensics, and cybersecurity.
