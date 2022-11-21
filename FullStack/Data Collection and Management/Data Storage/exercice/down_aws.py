import boto3
import json
import os.path
import pandas as pd



PATH = os.path.dirname(r"C:\Users\jerem\Documents\Jedha\FullStack\Data\FullStack\Data Collection and Management\Data Storage\aws.py")
print(PATH)

session = boto3.Session(aws_access_key_id="AKIAXN2YJLDM5DRF6M6I", 
                        aws_secret_access_key="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")

s3 = session.resource('s3')

s3.meta.client.download_file('bucket-from-jeremy-jedha-2022', 'test.csv', f'{PATH}/test.csv')




