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

    # Data Processing
    logging.info("Processing collected changes...")
    processed_changes = text_processor.process_changes(changes)
    logging.info(f"Processed {len(processed_changes)} changes")

    # Decision Making
    logging.info("Analyzing changes with LLM...")
    analyzed_changes = llm_interface.analyze_with_llm(processed_changes)
    logging.info(f"Analyzed {len(analyzed_changes)} changes")

    if analyzed_changes:
        # Storage
        logging.info("Storing analyzed changes...")
        astra_manager.store_data(analyzed_changes)
        logging.info("Changes stored successfully")

        # Content Generation
        logging.info("Generating markdown content...")
        markdown_content = markdown_generator.generate_markdown(analyzed_changes)
        logging.info("Markdown content generated")

        # Notification
        logging.info("Sending notification...")
        discord_notifier.send_notification(markdown_content)
        logging.info("Notification sent")
    else:
        logging.warning("No changes were analyzed. Skipping storage, content generation, and notification steps.")

    logging.info("Data collection, processing, and notification completed.")

if __name__ == "__main__":
    main()
