import requests
import json
import os
from requests.utils import quote


#anonymous api key is uesed for now since I do not want to make many requests
API_KEY = "eyJvcmciOiI1ZTU1NGUxOTI3NGE5NjAwMDEyYTNlYjEiLCJpZCI6ImVlNDFjMWI0MjlkODQ2MThiNWI4ZDViZDAyMTM2YTM3IiwiaCI6Im11cm11cjEyOCJ9"
headers = {"Authorization": API_KEY}

url = "https://api.dataplatform.knmi.nl/open-data/v1/datasets/10-minute-in-situ-meteorological-observations/versions/1.0/files"
response = requests.get(url, headers=headers)
data = response.json()

filename = os.path.join("data/raw", "knmi_10min_files.json")
with open(filename, "w") as f:
    json.dump(data, f, indent=2)
