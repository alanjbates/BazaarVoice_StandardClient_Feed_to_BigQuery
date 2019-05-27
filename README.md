<h1>BazaarVoice_StandardClient_Feed_to_BigQuery</h1>

The use case of this repo is collecting customer natural language product reviews for analytics and data science use.

BazaarVoice is the leading Product Ratings and Reviews partner in the Industry.  This is the definition of the data that I collect from Bazaarvoice:
https://knowledge.bazaarvoice.com/wp-content/conversations/en_US/Display/content_exports.html#standard-client-feed

The Standard Client Feed XML is parsed and flattened into two BigQuery tables. 
 - Product Granularity (Aggregated by ProductID review metrics)
 - Review Granularity (A record for each individual customer review)

<h5>Collection</h5>
 - A Google Cloud Function is triggered weekly by Google cloud Scheduler http triggers
 - A small python script runs using the pysftp package to collect the large file from BazaarVoice SFTP site
 - The raw .xml.gz files are written to a Google Cloud Storage Bucket

<h5>Wrangling</h5>
 - Performed in a Google AI Hub Notebook
 - ElementTree
 - pandas
 - Google BigQuery target tables
 
<h5>Sentiment Analysis</h5>
 - Performed in an Google AI Hub Notebook
 - Google BigQuery is used to select join to external product master data.
 - pandas
 - nltk vader is used to create the numeric sentiment scores
 - seaborn is used for visual analysis

![Image of Architecture](https://raw.githubusercontent.com/alanjbates/BazaarVoice_StandardClient_Feed_to_BigQuery/master/bazaarvoice_to_bq.png)