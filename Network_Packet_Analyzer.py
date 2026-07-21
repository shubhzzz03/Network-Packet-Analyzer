import sys
from datetime import datetime

try:
    from scapy.all import sniff, IP, TCP, UDP, ICMP
except ImportError:
    print("Scapy is not installed.")
    print("Install it using: pip install scapy")
    sys.exit(1)

PROJECT = "Network Packet Analyzer"


def process_packet(packet):
    if not packet.haslayer(IP):
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst
    packet_size = len(packet)

    protocol = "Unknown"
    details = ""

    if packet.haslayer(TCP):
        protocol = "TCP"
        details = (
            f"Ports: {packet[TCP].sport} -> {packet[TCP].dport} | "
            f"Flags: {packet[TCP].flags}"
        )

    elif packet.haslayer(UDP):
        protocol = "UDP"
        details = (
            f"Ports: {packet[UDP].sport} -> {packet[UDP].dport}"
        )

    elif packet.haslayer(ICMP):
        protocol = "ICMP"
        details = (
            f"Type: {packet[ICMP].type} | "
            f"Code: {packet[ICMP].code}"
        )

    print("-" * 60)
    print(f"Time          : {timestamp}")
    print(f"Protocol      : {protocol}")
    print(f"Source IP     : {source_ip}")
    print(f"Destination IP: {destination_ip}")
    print(f"Packet Size   : {packet_size} Bytes")

    if details:
        print(details)


def main():
    print("=" * 60)
    print(PROJECT)
    print("=" * 60)
    print("Starting packet capture...")
    print("Capturing 20 packets.\n")

    try:
        sniff(prn=process_packet, store=False,count=20)

    except PermissionError:
        print("\nRun this program as Administrator or Root.")

    except KeyboardInterrupt:
        print("\nPacket capture stopped.")


if __name__ == "__main__":
    main()