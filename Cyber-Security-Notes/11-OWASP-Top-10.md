# OWASP Top 10 (Web Application Security Risks)

## 📌 Definition
OWASP Top 10 is a list of the most critical security risks to web applications published by the Open Web Application Security Project (OWASP).

---

## 🎯 Purpose
- Increase awareness of web vulnerabilities
- Help developers build secure applications
- Guide security testing and audits

---

## 🔟 OWASP Top 10 Risks

### 1. Broken Access Control
Users can access unauthorized data or functions.

**Example:**
Accessing admin panel without permission.

---

### 2. Cryptographic Failures
Weak encryption or improper data protection.

**Example:**
Storing passwords in plain text.

---

### 3. Injection
Attacker sends malicious input to execute commands.

**Example:**
SQL Injection: `' OR 1=1 --`

---

### 4. Insecure Design
Flaws in system architecture.

**Example:**
No rate limiting on login page.

---

### 5. Security Misconfiguration
Improper server or application settings.

**Example:**
Default admin credentials left unchanged.

---

### 6. Vulnerable and Outdated Components
Using outdated libraries or frameworks.

**Example:**
Old version of Apache or WordPress plugin.

---

### 7. Identification and Authentication Failures
Weak login systems.

**Example:**
No MFA, weak password policy.

---

### 8. Software and Data Integrity Failures
Untrusted updates or code execution.

**Example:**
Malicious software update installed.

---

### 9. Security Logging and Monitoring Failures
Lack of proper logs and monitoring.

**Example:**
No detection of repeated login attempts.

---

### 10. Server-Side Request Forgery (SSRF)
Attacker forces server to make unauthorized requests.

**Example:**
Accessing internal cloud metadata services.

---

## 🧠 Real World Example
A vulnerable login page allows SQL injection, giving attacker full database access.

---

## 🛡️ Prevention
- Input validation
- Secure coding practices
- Regular security testing
- Patch management
- Strong authentication

---

## 🎯 Key Takeaway
OWASP Top 10 represents the most common and dangerous web application security risks.
