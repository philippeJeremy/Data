import boto3
import json
import os.path
import pandas as pd



session = boto3.Session(aws_access_key_id="", 
                        aws_secret_access_key="")

s3 = session.resource("s3")
bucket = s3.create_bucket(Bucket="")
data = pd.DataFrame({'col1': [1,2,3,4], 'col2': ['a1','a2','a3','a4']})
csv = data.to_csv()
put_object = bucket.put_object(Key="test.csv", Body=csv)


