import logging
from data_collection import changes_scraper, jira_scraper, cep_scraper, mailing_list_scraper
from data_processing import text_processor
from decision_making import llm_interface
from storage import astra_manager
from content_generation import markdown_generator
from notification import discord_notifier

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Data Collection
    logging.info("Starting data collection...")
    
    # Scrape changes
    changes = changes_scraper.scrape_changes()
    logging.info(f"Collected {len(changes)} changes from CHANGES.txt")

    # TODO: Implement other data collection methods as they are completed
    
    # Data Processing
    # TODO: Implement data processing once text_processor is completed

    # Decision Making
    # TODO: Implement decision making once llm_interface is completed

    # Storage
    # TODO: Implement storage once astra_manager is completed

    # Content Generation
    # TODO: Implement content generation once markdown_generator is completed

    # Notification
    # TODO: Implement notification once discord_notifier is completed

    logging.info("Data collection and processing completed.")

if __name__ == "__main__":
    main()
