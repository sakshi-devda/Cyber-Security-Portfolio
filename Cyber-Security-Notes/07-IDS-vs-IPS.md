# IDS vs IPS (Intrusion Detection System vs Intrusion Prevention System)

## 📌 Definition

### IDS (Intrusion Detection System)
IDS is a security tool that **monitors network/system activity and detects suspicious behavior**, but does NOT block it.

### IPS (Intrusion Prevention System)
IPS is a security tool that **detects and actively blocks malicious activity in real time**.

---

## 🔍 Key Difference

| Feature | IDS | IPS |
|--------|-----|-----|
| Function | Detects attacks | Detects + Prevents attacks |
| Action | Passive | Active |
| Response | Alerts only | Blocks traffic |
| Position | Out-of-band | Inline |
| Impact | Monitoring | Protection |

---

## ⚙️ How IDS Works
1. Monitors network traffic
2. Compares with known attack signatures
3. Generates alert if suspicious activity found

---

## ⚙️ How IPS Works
1. Monitors traffic in real time
2. Detects malicious patterns
3. Automatically blocks or drops packets

---

## 🧠 Real World Example

### IDS Example:
Security team gets alert: "Suspicious login attempt detected"

### IPS Example:
System automatically blocks IP after multiple failed login attempts

---

## 🛡️ Advantages

### IDS:
- Good for monitoring
- Low impact on network performance

### IPS:
- Real-time protection
- Prevents attacks instantly

---

## ⚠️ Limitations

### IDS:
- Cannot stop attack
- Requires manual response

### IPS:
- Can block legitimate traffic (false positives)
- Slight network latency

---

## 🎯 Key Takeaway
IDS detects threats, while IPS detects and prevents threats automatically.
