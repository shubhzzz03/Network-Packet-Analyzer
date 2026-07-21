# Task 1 – Network Packet Analyzer

A Python-based packet sniffer built with **Scapy** for the CodSoft Cyber Security Internship.
It captures live network traffic and extracts key details from each packet: source IP,
destination IP, protocol type, ports (if applicable), packet length, and a readable payload preview.

## Features
- Live packet capture on any available network interface
- Supports TCP, UDP, ICMP, and generic IP/IPv6 traffic
- Optional BPF filters (e.g. `tcp port 80`, `icmp`, `udp`)
- Limit capture to a specific packet count, or run until stopped (Ctrl+C)
- Clean, organized console output
- Optional logging of results to a file

## Requirements
- Python 3.7+
- [Scapy](https://scapy.net/): `pip install scapy`
- Administrator/root privileges (required for raw packet capture)
- Npcap (Windows) or libpcap (Linux/macOS, usually preinstalled)

## Installation
```bash
git clone <your-repo-url>
cd CODSOFT_TASKSNO
pip install scapy
```

## Project Structure

```
Network_Packet_Analyzer/
│── packet_analyzer.py
│── README.md
│── capture.log (generated after execution)
```

---

## Technologies Used

- Python 3
- Scapy
- Networking
- Packet Sniffing
- Cyber Security

---

## Supported Protocols

- TCP
- UDP
- ICMP
- IPv4
- IPv6

---

## Learning Outcomes

This project helped me learn:

- Packet sniffing using Scapy
- Network packet analysis
- IP addressing
- TCP/UDP communication
- Command-line argument handling
- Logging captured packets

---

## Future Improvements

- Save packets in PCAP format
- GUI using Tkinter
- Protocol-wise statistics
- Export results to CSV
- Real-time traffic graphs

---

## Usage
```bash
# Capture indefinitely on the default interface (Ctrl+C to stop)
sudo python3 packet_analyzer.py

# Capture on a specific interface
sudo python3 packet_analyzer.py -i eth0

# Capture only 50 packets
sudo python3 packet_analyzer.py -c 50

# Only capture HTTP traffic
sudo python3 packet_analyzer.py -f "tcp port 80"

# Save results to a log file as well as printing them
sudo python3 packet_analyzer.py -o capture.log
```

> On Windows, run your terminal as Administrator and ensure Npcap is installed.
> On Linux/macOS, run with `sudo`.

## Sample Output
```
============================================================
Packet #1  |  Time: 2026-07-21 10:32:11
  Source IP      : 192.168.1.10
  Destination IP : 142.250.premise.14
  Protocol       : TCP
  Source Port    : 51322
  Dest Port      : 443
  Packet Length  : 74 bytes
  Payload        : (no payload)
============================================================
```

## How It Works
1. `scapy.sniff()` captures packets in real time on the chosen interface.
2. Each packet is passed to the `analyze_packet()` callback.
3. The script checks which layers are present (IP, IPv6, TCP, UDP, ICMP) and
   pulls out the relevant fields.
4. Payload bytes (if any) are converted to a safe, printable string preview.
5. Results are printed in a structured block and optionally written to a log file.

## Ethical Use Notice
This tool is intended strictly for educational purposes and for use on networks
you own or have explicit permission to monitor. Capturing traffic on networks
without authorization may be illegal.

## Acknowledgements

- CodSoft Cyber Security Internship
- Scapy Documentation
- Python Community
  
## Author

Shubham Santosh Beloshe.

Github : https://github.com/shubhzzz03

LinkedIn : www.linkedin.com/in/shubham-beloshe-a311612b1
