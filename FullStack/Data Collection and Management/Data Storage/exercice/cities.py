import requests
import json
import boto3


# .get('https://api.teleport.org/api/cities/?search=paris')

r = requests.get('https://api.teleport.org/api/urban_areas/slug:paris/scores/')

fichier = r.json().get("categories",{})


with open('cities.json', 'w') as f:
    json.dump(fichier, f)
    

session = boto3.Session(aws_access_key_id="", 
                        aws_secret_access_key="")

s3 = session.resource("s3")
s3.Bucket('philippe-jeremy-first-bucket').upload_file('cities.csv', 'cities.csv') 