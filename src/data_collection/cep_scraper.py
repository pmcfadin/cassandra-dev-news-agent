import requests
from bs4 import BeautifulSoup

def scrape_ceps():
    """
    Scrape Cassandra Enhancement Proposals (CEPs) from the Apache Cassandra wiki.
    
    Returns:
    list: A list of dictionaries containing CEP information (title, status, link)
    """
    url = "https://cwiki.apache.org/confluence/display/CASSANDRA/CEP"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to fetch CEPs. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    ceps = []

    for row in soup.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) >= 3:
            link = cells[0].find('a')
            if link:
                title = link.text.strip()
                href = link['href']
                status = cells[2].text.strip()
                ceps.append({
                    'title': title,
                    'status': status,
                    'link': f"https://cwiki.apache.org{href}"
                })

    return ceps
