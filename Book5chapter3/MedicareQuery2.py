import pandas as pd
from google.cloud import bigquery


# set up the query 

QUERY = """
        SELECT provider_city, provider_state, drg_definition, 
        average_total_payments, average_medicare_payments
        FROM `bigquery-public-data.cms_medicare.inpatient_charges_2015`
        WHERE drg_definition LIKE  '554 %'
        ORDER BY provider_city ASC
        LIMIT 1000
        """

client = bigquery.Client.from_service_account_json(
            'medicareproject-397220-715beb5a4752.json')


query_job = client.query(QUERY)
df = query_job.to_dataframe()

print ("Records Returned: ", df.shape )
print ()
print ("First 3 Records")
pd.set_option('display.max_columns', None)
print (df.head(3))
