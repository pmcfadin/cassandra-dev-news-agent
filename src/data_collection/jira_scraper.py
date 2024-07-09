from jira import JIRA
import os
from dotenv import load_dotenv

load_dotenv()

def scrape_jira(issue_key):
    """
    Scrape information from a Jira issue.
    
    Args:
    issue_key (str): The Jira issue key (e.g., 'CASSANDRA-1234')
    
    Returns:
    dict: A dictionary containing the issue's summary and description
    """
    jira_url = os.getenv('JIRA_URL', 'https://issues.apache.org/jira')
    jira_username = os.getenv('JIRA_USERNAME')
    jira_password = os.getenv('JIRA_PASSWORD')

    try:
        jira = JIRA(server=jira_url, basic_auth=(jira_username, jira_password))
        issue = jira.issue(issue_key)
        
        return {
            'summary': issue.fields.summary,
            'description': issue.fields.description
        }
    except Exception as e:
        print(f"Error scraping Jira issue {issue_key}: {str(e)}")
        return None
