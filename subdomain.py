import requests
import sys
from time import sleep
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#eproxies = {'http' : 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def find_subdomains(domain, wordlist):
    subdomains = []
    
    with open(wordlist, 'r') as f:
        words = f.read().splitlines()
    
     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    
    for word in words:
        try:
            subdomain = f"{word}.{domain}" #?
            response = requests.get(f"https://{subdomain}", headers=headers)
            
            if response.status_code == 200:
                subdomains.append(subdomain)
        except Exception:
            print(f"error {subdomain}")

        sleep(0.1)
    return subdomains

if __name__=="__main__":
    # domain = "nettruyenplus.com"
    # wordlist_file = "wordlist.txt"
    try:
        domain = sys.argv[1].strip
        wordlist = sys.argv[2].strip
    except IndexError:
        print("[*]Usage: %s <domain_name> <wordlist>" %sys.argv[0])
        print("[*]Example: %s google.com wordlist.txt" %sys.argv[0])
        exit(-1)

    subdomains = find_subdomains(domain, wordlist)
    if(subdomains):
        for subdomain in subdomains:
            print(subdomain)
            print("\n")
    else:
        print("Cannot detect the subdomain!");
        
        