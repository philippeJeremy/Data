import boto3
import json
import os.path
import pandas as pd



session = boto3.Session(aws_access_key_id="AKIAXN2YJLDM5DRF6M6I", 
                        aws_secret_access_key="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")

s3 = session.resource("s3")
bucket = s3.create_bucket(Bucket="bucket-from-jeremy-jedha-2022")
data = pd.DataFrame({'col1': [1,2,3,4], 'col2': ['a1','a2','a3','a4']})
csv = data.to_csv()
put_object = bucket.put_object(Key="test.csv", Body=csv)


