import requests
from bs4 import BeautifulSoup

def scrape_changes():
    """
    Scrape the CHANGES.txt file from the Apache Cassandra GitHub repository.
    
    Returns:
    list: A list of changes, where each change is a string containing the version and description.
    """
    url = "https://raw.githubusercontent.com/apache/cassandra/trunk/CHANGES.txt"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to fetch CHANGES.txt. Status code: {response.status_code}")
        return []

    changes = []
    current_version = None

    for line in response.text.split('\n'):
        line = line.strip()
        if line.endswith(':'):  # This is a version line
            current_version = line[:-1]  # Remove the colon
        elif line.startswith('*') and current_version:
            changes.append(f"{current_version}: {line[1:].strip()}")

    return changes
