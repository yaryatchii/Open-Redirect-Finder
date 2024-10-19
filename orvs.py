import os
import subprocess
import urllib.parse

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

# Fonction alternative à qsreplace pour remplacer les paramètres URL
def replace_url_param(url, new_value):
    parsed_url = urllib.parse.urlparse(url)
    query = urllib.parse.parse_qs(parsed_url.query)
    
    # Remplacer tous les paramètres ayant une URL par new_value
    for param in query:
        if 'http' in query[param][0]:
            query[param] = [new_value]
    
    new_query = urllib.parse.urlencode(query, doseq=True)
    new_url = urllib.parse.urlunparse(parsed_url._replace(query=new_query))
    
    return new_url

def scan_domain(domain):
    print(f"{YELLOW}Scanning {domain} for open redirect vulnerabilities...{RESET}")
    try:
        # Récupérer les URL via waybackurls
        urls = subprocess.getoutput(f"waybackurls {domain} | grep -a -i =http").splitlines()
        
        # Remplacer les URLs dans les paramètres avec 'http://evil.com'
        for url in urls:
            modified_url = replace_url_param(url, 'http://evil.com')
            result = subprocess.getoutput(f"curl -s -L {modified_url} -I | grep 'evil.com'")
            if result:
                print(f"{modified_url} {RED}is Vulnerable{RESET}")
            else:
                print(f"{modified_url} {GREEN}is Not Vulnerable{RESET}")
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
