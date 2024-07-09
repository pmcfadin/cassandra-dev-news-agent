import requests
from bs4 import BeautifulSoup
import re

def scrape_mailing_list():
    """
    Scrape the Apache Cassandra dev mailing list for recent threads.
    
    Returns:
    list: A list of dictionaries containing thread information (subject, author, date, link)
    """
    url = "https://lists.apache.org/list.html?dev@cassandra.apache.org"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to fetch mailing list. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    threads = []

    for row in soup.find_all('tr', class_='messagesgroup'):
        subject_cell = row.find('td', class_='subject')
        author_cell = row.find('td', class_='author')
        date_cell = row.find('td', class_='date')

        if subject_cell and author_cell and date_cell:
            subject_link = subject_cell.find('a')
            if subject_link:
                subject = subject_link.text.strip()
                link = subject_link['href']
                author = author_cell.text.strip()
                date = date_cell.text.strip()

                # Extract vote, discuss, or announce tags
                tags = re.findall(r'\[(VOTE|DISCUSS|ANNOUNCE|RESULT)\]', subject, re.IGNORECASE)
                
                threads.append({
                    'subject': subject,
                    'author': author,
                    'date': date,
                    'link': f"https://lists.apache.org{link}",
                    'tags': tags
                })

    return threads
