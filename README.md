# 🔍 Python-Based Advanced Port Scanners

This repository contains two functional and educational port scanner projects:

1. **Version 1: Advanced Port Scanner (Pure Python)**  
2. **Version 2: Nmap Wrapper (Subprocess-based scanner)**

These tools are useful for learning basic network security concepts, TCP scanning, service detection, and scripting with Python.

---

## 🧰 Project Structure
├── port-scanner
  |── port-scanner.py # Version 1: Native socket scanner
├── nmap-scanner
  |── nmap-scanner.py # Version 2: Nmap subprocess wrapper
├── requirements.txt # Required Python libraries
├── .gitignore # Ignored files
└── README.md # This file


---

## Version 1: Advanced Port Scanner (Pure Python)

### 📌 Description

A multithreaded Python script that performs a TCP port scan on a target host, displaying open ports and guessing their associated service names. It uses the built-in `socket` module and saves results to a file. It is ideal for educational or lab use.

### ✅ Features

- Scans a user-defined port range
- Displays open ports with service name
- Multithreaded (100 threads) for fast scanning
- Saves results to `scan_results.txt`
- Uses `colorama` for colored console output

### ▶️ How to Use

1. Install required library:

pip install -r requirements.txt

2. Start the program

python port-scanner.py



---

## Version 2: Nmap Port Scanner Wrapper (Python)


A lightweight Python script that acts as a wrapper around [Nmap](https://nmap.org/), allowing users to scan ports, detect services, and save results — all from a simple Python interface.

This is ideal for learning how to integrate powerful external security tools (like Nmap) into Python workflows.

---

## 🔍 Features

- TCP port scanning using the Nmap CLI
- Service version detection (`-sV` flag included)
- Save full Nmap results to a `.txt` file
- User-friendly CLI interface via `input()`
- Lightweight, cross-platform (Windows/macOS/Linux)

---

## 🛠️ Requirements

### ✅ System Requirements

- **Nmap must be installed on your system.**  
Download it from: [https://nmap.org/download.html](https://nmap.org/download.html)

- Ensure the `nmap` command is available in your system's PATH  
Test it by running:

nmap -v

▶️ How to Use
## Clone or download this repository:

git clone https://github.com/dkim179/multi-method-port-scanner-.git
cd nmap-wrapper

## Run the Python script:python nmap-wrapper.py

Enter target and port range when prompted:
Enter target IP or domain: scanme.nmap.org  
Enter port range (e.g., 1-1000): 1-1024

## Nmap will execute and print results like:

PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu
80/tcp   open  http    Apache httpd 2.4.29
443/tcp  open  https   Apache httpd

## Results saved to: 
nmap_scan_scanme.nmap.org.txt
