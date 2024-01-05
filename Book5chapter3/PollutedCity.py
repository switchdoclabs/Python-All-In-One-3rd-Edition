import pandas as pd
from google.cloud import bigquery


# sample query from:
QUERY = """
        SELECT location, city, country, value, timestamp
        FROM `bigquery-public-data.openaq.global_air_quality`
        WHERE pollutant = "pm10" AND timestamp > "2017-04-01"
        ORDER BY value DESC
        LIMIT 1000
        """

#client = bigquery.Client()
client = bigquery.Client.from_service_account_json(
                    'medicareproject-397220-715beb5a4752.json')
query_job = client.query(QUERY)
df = query_job.to_dataframe()

print (df.head(3))
