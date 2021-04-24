from google.cloud import bigquery as bq

client = bq.Client()

# Perform a query.
QUERY = 'SELECT * FROM `bqdb.Song` LIMIT 1000'
print("send query")

query_job = client.query(QUERY)  # API request
print("get result")
rows = query_job.result()        # Waits for query to finish

for row in rows:
    print(row)
