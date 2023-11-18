import requests
from bs4 import BeautifulSoup
import ipaddress
import re

# Define ANSI color codes for fancy text banner
class bcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# Display fancy text banner
def print_banner():
    print(f"{bcolors.HEADER}{"Hayagriva"}{bcolors.ENDC}" +
          f" by {bcolors.OKGREEN}{"WrathfulDiety"}{bcolors.ENDC}")

# Generate a list of IP addresses within the specified subnet
def generate_ips(ip_address, subnet_mask):
    try:
        network = ipaddress.ip_network(f"{ip_address}/{subnet_mask}", strict=False)
        return [str(ip) for ip in network.hosts()]
    except Exception as e:
        print(f"{bcolors.WARNING}Error generating IP addresses: {e}{bcolors.ENDC}")
        return []

# Fetch IP subnets from the specified URL for the given organization
def get_ip_subnets(org):
    url = f"https://bgp.he.net/search?search%5Bsearch%5D={org}&commit=Search"
    response = requests.get(url)

    if response.status_code == 200:
        ip_subnets = []

        # Extract IP subnets based on the organization
        if org == "RIPE NCC":
            soup = BeautifulSoup(response.content, 'html.parser')
            ip_subnets_elements = soup.find_all('span', class_='ipSubnet')
            for ip_subnet_element in ip_subnets_elements:
                ip_address, subnet_mask = ip_subnet_element.text.split('/')
                ip_subnets.append(f"{ip_address}/{subnet_mask}")
        else:
            # Extract IP subnets using a regular expression
            pattern = r"\d+\.\d+\.\d+\.\d+\/\d+|\w+:\w+:\w+:\w+:\w+:\w+:\w+:\w+/\d+"
            for match in re.findall(pattern, response.text):
                ip_subnets.append(match)

        return ip_subnets
    else:
        raise Exception(f"{bcolors.FAIL}Failed to fetch IP subnets for {org}{bcolors.ENDC}")

# Save a list of IP addresses to a file
def save_ip_addresses(ips, filename):
    try:
        with open(filename, "w") as outfile:
            for ip in ips:
                outfile.write(f"{ip}\n")
    except Exception as e:
        print(f"{bcolors.WARNING}Error saving IP addresses to file {filename}: {e}{bcolors.ENDC}")

# Main function
if __name__ == "__main__":
    print_banner()

    while True:
        try:
            org = input("Enter the organization name: ")
            break
        except Exception as e:
            print(f"{bcolors.WARNING}Invalid input: {e}{bcolors.ENDC}")

    ip_subnets = get_ip_subnets(org)

    if not ip_subnets:
        print(f"{bcolors.FAIL}No IP subnets found for {org}{bcolors.ENDC}")
        exit()

    all_ips = []
    for ip_subnet in ip_subnets:
        ip_address, subnet_mask = ip_subnet.split("/")
        ips_in_subnet = generate_ips(ip_address, subnet_mask)
        all_ips.extend(ips_in_subnet)

    filename = f"{org}.txt"
    save_ip_addresses(all_ips, filename)

    print(f"\nAll IP addresses saved to file: {filename}")
