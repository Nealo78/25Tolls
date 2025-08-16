#!/usr/bin/env python3
"""
CyberSecToolKit - Collection of 25 Cyber Security Tools
=======================================================
"""
import os
import sys
import subprocess
import shlex

TOOL_LIST = [
    {"name": "nmap", "desc": "Network mapping tool"},
    {"name": "metasploit-framework", "desc": "Penetration testing framework"},
    {"name": "dirb", "desc": "Directory enumeration tool"},
    {"name": "nikto", "desc": "Web server auditing tool"},
    {"name": "hydra", "desc": "Brute force hacking tool"},
    {"name": "sqlmap", "desc": "SQL injection tool"},
    {"name": "aircrack-ng", "desc": "Wi-Fi security auditing suite"},
    {"name": "wireshark", "desc": "Packet analysis tool"},
    {"name": "recon-ng", "desc": "Reconnaissance tool"},
    {"name": "theHarvester", "desc": "Email & subdomain harvester"},
    {"name": "dnsenum", "desc": "DNS enumeration tool"},
    {"name": "masscan", "desc": "Fast port scanner"},
    {"name": "dnsrecon", "desc": "Advanced DNS reconnaissance tool"},
    {"name": "commix", "desc": "Automated SQL injection tool"},
    {"name": "zaproxy", "desc": "OWASP ZAP Proxy"},
    {"name": "wpscan", "desc": "WordPress security scanner"},
    {"name": "johntheripper", "desc": "Password cracker"},
    {"name": "kismet", "desc": "Wireless network detector"},
    {"name": "ettercap", "desc": "ARP poisoning & sniffing tool"},
    {"name": "sqlcipher", "desc": "SQLite database encryption"},
    {"name": "etherape", "desc": "Graphical network analyzer"},
    {"name": "kanvas", "desc": "Network threat visualization"},
    {"name": "yara", "desc": "Malware identification tool"},
    {"name": "radamsa", "desc": "Fuzz testing tool"},
    {"name": "skipfish", "desc": "Web application scanner"},
    {"name": "burpsuite", "desc": "Web vulnerability scanner"}
]

def print_banner():
    print("""
███████╗ ██████╗  ██╗   ██╗ ██████╗ ████████╗ ██████╗ ███╗   ██╗██╗   ██╗
██╔════╝ ██╔══██╗ ██║   ██║██╔═══██╗╚══██╔══╝██╔═══██╗████╗  ██║██║   ██║
███████╗ ██████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██╔██╗ ██║██║   ██║
██╔═══██╗██╔══██╗ ██║   ██║██║   ██║   ██║   ██║   ██║██║╚██╗██║██║   ██║
██║   ██║██║  ██║╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██║ ╚██╗██║╚██████╔╝
╚═╝   ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝ ╚═════╝ 
                                                                         
--- CyberSecToolKit ---
""")

def install_tool(tool_name):
    cmd = f"apt-get install -y {tool_name}"
    try:
        subprocess.run(shlex.split(cmd), check=True)
        print(f"[+] Successfully installed {tool_name}")
    except subprocess.CalledProcessError as e:
        print(f"[-] Installation failed: {e}")

def main():
    print_banner()
    print("--- Available Tools ---")
    for i, tool in enumerate(TOOL_LIST, 1):
        print(f"{i}. {tool['name'].capitalize()} - {tool['desc']}")
    
    while True:
        choice = input("\nSelect a tool to install (1-" + str(len(TOOL_LIST)) + ") or 'q' to quit: ")
        
        if choice.lower() == 'q':
            break
            
        try:
            index = int(choice) - 1
            if 0 <= index < len(TOOL_LIST):
                tool = TOOL_LIST[index]
                install_tool(tool['name'])
            else:
                print("Invalid selection, please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("This script must be run as root!")
        exit(1)
    main()