import boto3
import json
import requests

import pandas as pd

from joblib import load

r = requests.get("https://house-prices-simple-api.herokuapp.com/data")
df = pd.read_json(r.json(), orient="split")

x = df.iloc[:, :-1]
y = df.iloc[:, -1]

s3 = boto3.client("s3")
with open("house_prices_model.joblib", "wb") as data:
    s3.download_fileobj(
            Bucket='full-stack-assets', 
            Key='Deployment/house_prices_model.joblib', 
            Fileobj= data
        )

model = load("house_prices_model.joblib")

prediction = model.predict(x)[0]
print(f"According to our model, this house should cost: {prediction}\n")

truth = y.iloc[0]
print(f"House actual price is: {truth}")
print(f"Our model is {abs(prediction - truth)} away from the truth!")


