# Network Scanner

## Description

Network Scanner is a Python project that scans a local network and detects active devices using the ping command.

The user enters a network address, and the program checks all IP addresses in the selected range.

---

## Features

- Scan a local network
- Detect active devices
- Display ACTIVE or OFFLINE status
- Count active devices
- Easy to use from the terminal

---

## Technologies Used

- Python
- Subprocess
- Networking
- GitHub

---

## How It Works

The program:

1. Asks the user for a network address.
2. Generates IP addresses.
3. Sends a ping request.
4. Checks if the device responds.
5. Displays the result.
6. Counts active devices.

---

## Example

Enter network (example 192.168.1): 192.168.1

Scanning network...

192.168.1.1 --> ACTIVE

192.168.1.2 --> OFFLINE

192.168.1.3 --> ACTIVE

======================

Total active devices: 2

======================

---

## Skills Learned

- Python Programming
- Variables
- Loops
- Conditions
- Network Fundamentals
- IP Addressing
- ICMP Ping
- GitHub Project Management

---

## Project Structure

network-scanner/

├── scanner.py

├── README.md

└── screenshots/

    └── result.png

---

## Screenshot

![Network Scanner](screenshots/result.png)

---

## Future Improvements

- Export results to CSV
- Save scan reports
- Graphical User Interface (GUI)
- Multi-threaded scanning
- Hostname detection

---

## Author

oussema

Student in Information and Communication Technology (ICT)

Interested in Networks, Systems and Cybersecurity.