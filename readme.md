# Automated Airflow pipeline for Cricket Latest Standings

ℹ️ **Description:**
- Data Retrieval with Python and Cricbuzz API 🐍
  - Utilize Python to interface with the Cricbuzz API for fetching cricket statistics efficiently.

- Storing Data in Google Cloud Storage (GCS) ☁️
  - Safely preserve obtained data in CSV format within Google Cloud Storage (GCS) for accessibility and scalability.

- Creating a Cloud Function Trigger ⚡
  - Set up a Cloud Function triggered upon file upload to the GCS bucket, initiating subsequent data processing steps.

- Execution of the Cloud Function 🛠️
  - Craft intricate code within the Cloud Function to precisely trigger a Dataflow job for smooth data processing.

- Dataflow Job for BigQuery 🔄
  - Orchestrate the transfer of data from CSV file in GCS to BigQuery using Dataflow, configuring job settings for optimal performance.

- Looker Dashboard Creation 📊
  - Configure Looker to connect with BigQuery and create visually compelling dashboards for insightful analysis.

🚀 Get Started:
- Clone this repository.
- Follow the step-by-step instructions in each section of the README to set up and run the automated Airflow pipeline for cricket latest standings.

📝 **Instructions:**
- Python Setup and Installation:
  - Install Python on your local machine if not already installed.
  - Ensure pip is installed, which is Python's package installer.

- API Key Registration:
  - Register for an API key on the Rapid API website's Crickbuzz API to access one of their their API endpoint. I use 'stats/get-icc-standings' in this project.
  - Store the "X-RapidAPI-Key" API key and "X-RapidAPI-Host" securely, as it will be used to authenticate requests to the Cricbuzz API.

- Google Cloud Storage (GCS) Setup:
  - Set up a Google Cloud Platform (GCP) account if not already done.
  - Create a new project within the GCP Console.
  - Enable the Google Cloud Storage API for the project.
  - Create a bucket in Google Cloud Storage where the retrieved data will be stored.
  - https://cloud.google.com/sdk/docs/install-sdk Follow this link to install and authenticate your google cloud cli on your local machine(For testing and debugging if needed).

- GCS metadata
  - Create another bucket to store the metadata, and upload to it 'bq.json' and 'udf.js'

- Storing Data in GCS:
  - Modify the Python script "extract_and_push_gcs.py" to enter your API key, and your google cloud bucket name.
  - Run the script "extract_and_push_gcs.py" to test.
  - The fetched CSV file should reflect in your cloud bucket.

 - BigQuery configuration:
  - Navigate to BigQuery section in Cloud Console.
  - Create a new dataset, under which create an empty table.

- Cloud Function Creation:
  - Navigate to the Google Cloud Functions section in the GCP Console.
  - Create a new Cloud Function that will trigger upon file upload to the GCS bucket(replace all variable names with variable names corresponding to your components).
  - Configure the Cloud Function code.
    - Add the function.py code to the cloud function code part, and copy the requirements.txt to the requirements file.
  - Again trigger the "extract_and_push_gcs.py" file, and check the Dataflow section of the Cloud Console to see a new job 'bq-load' being trigerred.

- Dataflow Job:
  - Using the cloud function, Dataflow job that will ingest data from the CSV file in GCS and load it into BigQuery have been automated.

- Airflow configuration:
  - Navigate to Cloud Composer and create a new airflow composer.
  - Head to the dags folder and upload the dag.py file.

Testing the Data Pipeline:
Test the end-to-end data pipeline by triggering the DAG manually from the Airflow console
Verify that data is successfully transferred from the CSV file in GCS to BigQuery.
Monitor job logs and metrics to ensure the pipeline operates as expected.

This job is set to run automatically everyday, you can change your intervals by changing 'schedule_interval' parameter in 'dag.py'.

🔗 **Resources:**
- Airflow DAGs
  - https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html
- Google cloud
  - Storage
    - https://cloud.google.com/storage?hl=en
  - Cloud Functions
    - https://cloud.google.com/functions?hl=en
  - Dataflow
    - https://cloud.google.com/dataflow?hl=en
  - Big Query
    - https://cloud.google.com/bigquery?hl=en
  - Cloud Composer
    - https://cloud.google.com/composer?hl=en
