import unittest
from unittest.mock import patch, MagicMock
from ..src.data_collection import changes_scraper, jira_scraper, cep_scraper, mailing_list_scraper

class TestDataCollection(unittest.TestCase):

    @patch('src.data_collection.changes_scraper.requests.get')
    def test_changes_scraper(self, mock_get):
        # Mock the response
        mock_response = MagicMock()
        mock_response.text = "4.2:\n* Add new feature (CASSANDRA-1234)\n"
        mock_get.return_value = mock_response

        # Call the function
        result = changes_scraper.scrape_changes()

        # Assert the result
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIn('CASSANDRA-1234', result[0])
        self.assertIn('Add new feature', result[0])

    @patch('src.data_collection.jira_scraper.JIRA')
    def test_jira_scraper(self, mock_jira):
        # Mock the JIRA client and its methods
        mock_issue = MagicMock()
        mock_issue.fields.summary = "Test JIRA issue"
        mock_issue.fields.description = "This is a test description"
        mock_jira.return_value.issue.return_value = mock_issue

        # Call the function
        result = jira_scraper.scrape_jira("CASSANDRA-1234")

        # Assert the result
        self.assertIsInstance(result, dict)
        self.assertEqual(result['summary'], "Test JIRA issue")
        self.assertEqual(result['description'], "This is a test description")

    @patch('src.data_collection.cep_scraper.requests.get')
    def test_cep_scraper(self, mock_get):
        # Mock the response
        mock_response = MagicMock()
        mock_response.text = "<html><body><h1>CEP-1: Test CEP</h1><p>Status: Draft</p></body></html>"
        mock_get.return_value = mock_response

        # Call the function
        result = cep_scraper.scrape_ceps()

        # Assert the result
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['title'], "CEP-1: Test CEP")
        self.assertEqual(result[0]['status'], "Draft")

    @patch('src.data_collection.mailing_list_scraper.requests.get')
    def test_mailing_list_scraper(self, mock_get):
        # Mock the response
        mock_response = MagicMock()
        mock_response.text = "<html><body><h2>[VOTE] Release Apache Cassandra 4.2</h2></body></html>"
        mock_get.return_value = mock_response

        # Call the function
        result = mailing_list_scraper.scrape_mailing_list()

        # Assert the result
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIn("[VOTE]", result[0])
        self.assertIn("Release Apache Cassandra 4.2", result[0])

if __name__ == '__main__':
    unittest.main()
