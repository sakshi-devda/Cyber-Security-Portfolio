# Linux File System

## 📌 What is the Linux File System?

The Linux file system is a hierarchical structure used to organize, store, and manage files and directories. Everything in Linux is treated as a file, including hardware devices, directories, and processes.

---

## 🎯 Why is the Linux File System Important?

- Organizes files and directories efficiently.
- Makes file management easier.
- Provides security through permissions.
- Helps users and administrators locate important files.
- Essential for system administration and cybersecurity tasks.

---

## 🌳 Linux File System Hierarchy

The Linux file system starts from the **Root Directory (/)**, which is the top-level directory.

```
/
├── bin
├── boot
├── dev
├── etc
├── home
├── lib
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── sbin
├── srv
├── sys
├── tmp
├── usr
└── var
```

---

## 📁 Important Directories

### `/`
The root directory. It is the starting point of the Linux file system.

---

### `/home`
Stores personal files and directories of normal users.

Example:
```
/home/kali
```

---

### `/root`
Home directory of the root (administrator) user.

---

### `/etc`
Contains system configuration files.

Examples:
- passwd
- hosts
- ssh configuration

---

### `/bin`
Contains essential user commands.

Examples:
- ls
- cp
- mv
- cat

---

### `/sbin`
Contains system administration commands used by the root user.

Examples:
- reboot
- shutdown
- fsck

---

### `/usr`
Contains installed applications, libraries, and user programs.

---

### `/var`
Stores variable data such as logs, cache files, and mail.

---

### `/tmp`
Stores temporary files created by applications.

---

### `/dev`
Contains device files such as hard disks, USB devices, and terminals.

---

### `/proc`
A virtual directory that contains information about running processes and the Linux kernel.

---

## ⭐ Key Features of the Linux File System

- Hierarchical structure
- Everything is treated as a file
- Supports file permissions
- Multi-user support
- Secure and organized

---

## 💼 Real-World Example

A cybersecurity analyst investigating failed SSH logins may check:

- `/var/log/`
- `/etc/ssh/`
- `/home/`

to analyze logs, configuration files, and user activity.

---

## ❓ Interview Questions

### Q1. What is the root directory in Linux?

### Q2. What is stored inside the `/etc` directory?

### Q3. What is the difference between `/home` and `/root`?

### Q4. Why is the `/var` directory important for cybersecurity professionals?

### Q5. Why is everything treated as a file in Linux?

---

## 🎯 Key Takeaway

The Linux file system is a hierarchical structure that organizes files and directories efficiently. Understanding important directories helps cybersecurity professionals navigate systems, locate configuration files, analyze logs, and troubleshoot security incidents.
