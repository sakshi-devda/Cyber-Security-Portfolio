# 📊 Log Analysis Tool

## 📌 Project Overview

Log Analysis Tool is a Python-based cybersecurity project designed to analyze system logs and identify suspicious activities.

Logs are an important source of security information used by security analysts and SOC teams to monitor systems, detect threats, and investigate security incidents.

---

## 🎯 Objective

The main objectives of this project are:

- Understand security log analysis
- Identify suspicious activities from log data
- Learn basic SOC monitoring concepts
- Automate log analysis using Python
- Practice threat detection techniques

---

## 🛠️ Tools & Technologies Used

- Python 3
- Regular Expressions (Regex)
- File Handling
- Linux Log Files
- Kali Linux Environment

---

## ⚙️ Features

- Read and analyze log files
- Detect failed login attempts
- Search suspicious patterns
- Identify security events
- Count detected activities
- Generate basic analysis reports

---

## 🧠 How It Works

The tool works in the following steps:

1. User provides a log file as input.
2. The program reads log entries.
3. Each entry is analyzed using predefined patterns.
4. Suspicious activities are identified.
5. A final analysis report is generated.

Examples of suspicious activities:

- Multiple failed login attempts
- Unauthorized access attempts
- Invalid login attempts
- System errors

---

## 📂 Project Structure

```
Log-Analysis-Tool/
│
├── log_analyzer.py
├── sample_logs.txt
│
└── screenshots/
    ├── log-output.png
    └── analysis-report.png
```

---

## ▶️ How to Run

### Clone Repository

```bash
git clone <repository-link>
```

### Navigate to Project Folder

```bash
cd Log-Analysis-Tool
```

### Run Python Script

```bash
python3 log_analyzer.py
```

---

## 📸 Screenshots

### Log Analysis Output

(Add terminal screenshot here)

```markdown
![Log Analysis Output](./screenshots/log-output.png)
```

---

## 📊 Sample Output

```
Log Analysis Started...

Total Log Entries: 100

Failed Login Attempts: 15

Suspicious Activity Detected:

- Multiple failed authentication attempts
- Unknown IP activity

Analysis Completed Successfully
```

---

# 💻 Implementation Details

The Log Analysis Tool was developed using Python to automate the process of analyzing security logs.

The script reads log files, searches for suspicious patterns, and provides information that helps identify possible security events.

---

# 🧩 Code Explanation

## 1. Reading Log Files

Python file handling is used to open and read log files.

Example:

```python
with open("sample_logs.txt", "r") as file:
    logs = file.readlines()
```

---

## 2. Searching Suspicious Patterns

The tool searches for security-related keywords:

```
Failed
Error
Unauthorized
Denied
Invalid
```

---

## 3. Event Detection Process

The analysis process:

```
Read Logs
    ↓
Analyze Entries
    ↓
Match Suspicious Patterns
    ↓
Generate Report
```

---

## 4. Report Generation

The tool displays:

- Total log entries
- Detected suspicious events
- Security analysis results

---

## 📚 Learning Outcomes

Through this project, I learned:

- Basics of security log analysis
- Importance of system monitoring
- Python automation for cybersecurity
- Threat detection fundamentals
- SOC analyst workflow basics

---

## 🔐 Security Concepts Covered

- Log Monitoring
- Threat Detection
- Incident Investigation
- Security Operations Center (SOC)
- Event Analysis
- Defensive Security

---

## ⚠️ Security Note

This project is created for educational purposes and authorized security testing only.

Real-world security teams use SIEM solutions such as:

- Splunk
- IBM QRadar
- Microsoft Sentinel

for advanced log monitoring and threat detection.

---

## 🚀 Future Improvements

Possible improvements:

- Add real-time log monitoring
- Add IP reputation checking
- Generate detailed reports
- Integrate with SIEM tools
- Add dashboard visualization
- Implement anomaly detection

---

## 📌 Project Status

✅ Completed

---

## 👩‍💻 Author

**Sakshi Devda**

Cybersecurity Enthusiast
