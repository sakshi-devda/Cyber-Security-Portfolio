# Hashing and Digital Signatures

## 📌 Hashing

### Definition
Hashing is a one-way process that converts input data into a fixed-length string called a hash value.

---

## 🎯 Purpose of Hashing
- Ensure data integrity
- Store passwords securely
- Detect data tampering

---

## ⚙️ How Hashing Works
1. Input data is passed into a hash function
2. Hash function generates fixed-length output
3. Even a small change in input changes the hash completely

---

## 🔑 Properties of Hashing
- One-way function (cannot be reversed)
- Fixed output size
- Deterministic (same input = same output)
- Collision resistant (hard to find same hash for different input)

---

## 🧠 Example Algorithms
- MD5 (old, insecure)
- SHA-1 (deprecated)
- SHA-256 (widely used)

---

## 🧠 Real World Example
- Password storage in databases
- File integrity verification (downloads)

---

# 📌 Digital Signatures

## 📌 Definition
A digital signature is a cryptographic technique used to verify the authenticity and integrity of a message or document.

---

## 🎯 Purpose of Digital Signatures
- Verify sender identity
- Ensure message integrity
- Prevent data tampering

---

## ⚙️ How Digital Signatures Work
1. Sender hashes the message
2. Hash is encrypted using sender’s private key
3. Receiver decrypts using sender’s public key
4. Hash is compared to verify integrity

---

## 🧠 Real World Example
- Online legal documents
- Software updates verification
- Email authentication

---

## 🔐 Difference Between Hashing and Digital Signatures

| Feature | Hashing | Digital Signature |
|--------|--------|------------------|
| Purpose | Data integrity | Authentication + integrity |
| Keys used | No keys | Public & Private keys |
| Reversible | No | Partially (verification only) |
| Security level | Lower | Higher |

---

## 🎯 Key Takeaway
Hashing ensures data integrity, while digital signatures ensure both integrity and authenticity.
