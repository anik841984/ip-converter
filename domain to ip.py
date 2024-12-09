import socket
import pyfiglet
from termcolor import colored
from datetime import datetime

# Stylish banner with new colors
print(colored("#@@@@@@########### Created by Anik #################################", 'cyan'))
banner = colored(pyfiglet.figlet_format("EHACKER ANIK"), 'green')
print(banner)

# Display scan time
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(colored(f"Scan started at: {current_time}", 'magenta'))
print(colored("="*60, 'yellow'))

# Input domain from user
domain_name = input(colored("Enter the Target Domain: ", 'cyan'))

# Resolving domain
try:
    print(colored("\n[+] Resolving Domain...", 'yellow'))
    ip = socket.gethostbyname(domain_name)
    print(colored(f"[✔] Domain Resolved Successfully!", 'green'))
    print(colored(f"Target Domain: {domain_name}", 'blue'))
    print(colored(f"Resolved IP Address: {ip}\n", 'blue'))
except socket.gaierror:
    print(colored("\n[!] Error: Invalid domain name or network issue!", 'red'))

# Finishing the script
print(colored("="*60, 'yellow'))
print(colored("#@@@@@@########### Scan Complete #################################", 'cyan'))
