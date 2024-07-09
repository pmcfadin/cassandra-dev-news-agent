import re
from typing import List, Dict

def process_changes(changes: List[str]) -> List[Dict[str, str]]:
    """
    Process the scraped changes from CHANGES.txt.
    
    Args:
    changes (List[str]): A list of changes, where each change is a string containing the version and description.

    Returns:
    List[Dict[str, str]]: A list of dictionaries, each containing 'version', 'description', and 'jira_id' keys.
    """
    processed_changes = []
    for change in changes:
        version, description = change.split(': ', 1)
        jira_id = extract_jira_id(description)
        processed_changes.append({
            'version': version.strip(),
            'description': description.strip(),
            'jira_id': jira_id
        })
    return processed_changes

def extract_jira_id(text: str) -> str:
    """
    Extract the JIRA issue ID from the change description.
    
    Args:
    text (str): The change description text.

    Returns:
    str: The extracted JIRA issue ID, or an empty string if not found.
    """
    match = re.search(r'(CASSANDRA-\d+)', text)
    return match.group(1) if match else ''
