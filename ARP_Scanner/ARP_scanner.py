#PYTHON3
import signal
import scapy.all as scapy
import argparse
import sys
from termcolor import colored

#Ctrl + C
def def_handler(sig, frame):
    print(colored(f"\n[!] Saliendo del programa...\n", 'rede'))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

#Main
def get_arguments():
    parser = argparse.ArgumentParser(description="ARP Scanner")
    parser.add_argument("-t", "--target", required=True, dest="target", help="Host / IP Range to Scan")

    args = parser.parse_args()

    return args.target

def scan(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    arp_packet = broadcast_packet/arp_packet

    answered, unanswered = scapy.srp(arp_packet, timeout=1, verbose=False)

    response = answered.summary()

    if response:
        print(response)

def main():
    target = get_arguments()
    scan(target)

if __name__ == '__main__':
    main()
