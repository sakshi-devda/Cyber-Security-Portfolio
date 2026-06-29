# Linux File System

## 📌 What is the Linux File System?

The Linux file system is a hierarchical structure used to organize and manage files and directories. Everything in Linux is treated as a file, including devices and processes.

---

## 🌳 Linux File System Hierarchy

The top-most directory is called the **Root Directory (/)**.

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

### /

The root directory. It is the starting point of the Linux file system.

---

### /home

Stores personal files of users.

Example:

/home/sakshi

---

### /root

Home directory of the root (administrator) user.

---

### /etc

Contains system configuration files.

Example:
- passwd
- hosts
- ssh configuration

---

### /bin

Contains essential user commands.

Examples:
- ls
- cp
- mv
- cat

---

### /sbin

Contains system administration commands.

Examples:
- reboot
- shutdown
- ifconfig

---

### /usr

Contains installed applications and user programs.

---

### /var

Stores variable data.

Examples:
- Logs
- Cache
- Mail

---

### /tmp

Stores temporary files.

Files may be deleted automatically after reboot.

---

### /dev

Contains device files.

Examples:
- Hard disk
- USB devices
- Terminal

---

### /proc

Virtual directory containing information about running processes and the kernel.

---

## 🎯 Why File System is Important?

- Organizes data efficiently.
- Controls file storage.
- Helps manage permissions.
- Essential for system administration and cybersecurity.

---

## 🧠 Key Takeaway

Understanding the Linux file system helps cybersecurity professionals navigate systems, locate configuration files, analyze logs, and troubleshoot security issues.
