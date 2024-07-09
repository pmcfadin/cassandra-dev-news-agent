# cassandra-dev-news-agent

Apache Cassandra® is a highly dynamic and large project. With many developers working on bugs and features, it's hard to keep track of all the changes. Cassandra Dev News Agent is a AI Agent that gathers from all the sources of change and tries to distill it down for the user community so they can keep track of the latest goings on in the project. 

## Sources of information
 - When a feature change is made to the code base, committers also update the CHANGES.TXT file found here: https://github.com/apache/cassandra/blob/trunk/CHANGES.txt
 - In the CHANGES.TXT file, the changes are sectioned by Cassandra version number and in some cases, anything merged forward will have a duplicate
 - Changes are also reference a Jira number. For example a change like this "Expose current compaction throughput in nodetool (CASSANDRA-13890)" Points to https://issues.apache.org/jira/browse/CASSANDRA-13890
 - Jira entries are required for any change to the system. The include a lot of detail about the change, discussion on the solution, test data and in some cases, images that show visual infromation. 
 - Longer term changes are previewed and discussed in a Cassandra Enhancement Proposal or CEP. 
 - CEPs are officially listed here: https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=95652201
 - While CEPs are undergoing discussion, the drafts will be written here. You can look at the CEP under status and "Current state: " to see where the current proposal lies
 - Additionaly the mailing list is also a place to see the changes, however those tend to be discussions that turn into a CEP or Jira. Much more dynamic and more noise than signal. 
 - Voting is an important part of the mailing list and is very useful information for users. Every version release and CEP is voted on via the dev mailing list found here. https://lists.apache.org/list.html?dev@cassandra.apache.org
 - Each proceedural email has a particular tag in the subject [DISCUSS] for discussions about features and CEPs. [VOTE] to facilitate  voting. [ANNOUNCE] for offical project announements such as a version release. [RESULT] to finalize a vote thread and announce to users the final tally.

## Why an agent for this task?

An agentic AI system  offers the right kind of flexibilty to run a workflow of retrieve, decide, act, learn and notify.

Retrieve - Gather information from sources
Decide - Using an LLM, reason and decide on the next steps.
Act - Based on the decisions in the agentics step, act on those decisions
Learn - Update any system that needs to change based on new information
Notify - Output final result

## System Design

To build this project in Python, we propose the following system design:

1. Data Collection:
   - Use libraries like `requests` and `beautifulsoup4` to scrape data from the CHANGES.txt file, Jira, CEPs, and mailing lists.
   - Implement scheduled tasks using `apscheduler` to fetch data regularly.

2. Data Processing:
   - Use `pandas` for data manipulation and analysis.
   - Implement natural language processing with `nltk` or `spacy` to extract key information from text.

3. Decision Making:
   - Integrate with Claude 3.5 Sonnet API using the appropriate library for reasoning and decision-making.
   - Implement custom logic to determine the relevance and importance of changes.

4. Storage:
   - Use DataStax Astra and the DataAPI for cloud-native, scalable storage.
   - Store processed data, decisions, and generated content in Astra's managed Cassandra database.
   - Utilize Astra's DataAPI for efficient data access and management.

5. Content Generation:
   - Use the LLM to generate blog post content based on the processed data.
   - Implement templates using `jinja2` for consistent formatting.

6. Notification System:
   - Integrate with Discord API to post updates to the Planet Cassandra Discord server in a dedicated "dev-changes" channel.
   - Use the `discord.py` library to interact with the Discord API.

7. Web Interface:
   - Develop a simple web interface using `flask` or `fastapi` to display the weekly blog posts.

8. Logging and Monitoring:
   - Implement logging with Python's built-in `logging` module.
   - Use `prometheus_client` for monitoring and `grafana` for visualization.

9. Configuration:
   - Use `configparser` or `pyyaml` for managing configuration settings.

10. Testing:
    - Implement unit tests with `pytest` and integration tests to ensure system reliability.

This design allows for a modular, scalable system that can be easily extended or modified as the project evolves.

## Initial goal of the system
Our first goal is to build a system that will gather development changes in the Cassandra project and create a blog page once a week. Every Friday, users can see what they missed for the week. How detailed we get is based on how relevant the change is. This will have to be learned over time and the feedback will be on how frequent the changes are. If it's too much info weekly, we'll try daily. Not enough? We'll try every week. 
