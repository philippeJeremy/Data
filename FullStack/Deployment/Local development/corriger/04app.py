import boto3
from joblib import load
import pandas as pd
import requests 

## Load Data 
r = requests.get("https://house-prices-simple-api.herokuapp.com/data")
test_data = pd.read_json(r.json(), orient="split")
## Splitting into X and y
X = test_data.iloc[:, :-1]
y = test_data.iloc[:, -1]

## Load model 
s3 = boto3.client("s3")
with open("house_prices_model.joblib", "wb") as data:

    s3.download_fileobj(
            Bucket='full-stack-assets', 
            Key='Deployment/house_prices_model.joblib', 
            Fileobj= data
        )

print("Loading model...")
model = load("house_prices_model.joblib")
print("model loaded!\n")


print("Using model to make prediction...")
prediction = model.predict(X)[0]
print(f"According to our model, this house should cost: {prediction}\n")

print("Checking accuracy...")
truth = y.iloc[0]
print(f"House actual price is: {truth}")
print(f"Our model is {abs(prediction - truth)} away from the truth!")
