import socket
from urllib.parse import urlparse

def get_ip_from_url(url):
    # Parse the URL to extract the domain name
    parsed_url = urlparse(url)
    domain = parsed_url.netloc or parsed_url.path

    # Get the IP address of the domain
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        return f"Error retrieving IP address: {e}"

url = "(Enter your TARGET URL here)"
ip = get_ip_from_url(url)
print(f"The IP address of {url} is: {ip}")
