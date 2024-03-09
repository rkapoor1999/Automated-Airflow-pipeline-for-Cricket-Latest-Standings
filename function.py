from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "integral-surfer-xxxxx" #YOUR PROJECT ID

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
        "jobName": "bq-load",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://cricket_data_metadata/udf.js",
        "JSONPath": "gs://cricket_data_metadata/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "integral-surfer-xxxxx:cricket_dataset.icc_odi_batsman_ranking",
        "inputFilePattern": "gs://cricket_data_airflow/batsmen_rankings.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://cricket_data_metadata",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)

