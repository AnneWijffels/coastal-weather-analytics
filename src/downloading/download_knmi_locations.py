import requests
import os
import json

API_KEY = "eyJvcmciOiI1ZTU1NGUxOTI3NGE5NjAwMDEyYTNlYjEiLCJpZCI6ImU5MTIyN2JiODQyMjQwYWNiOTIzNzExZjEyM2YzZTI5IiwiaCI6Im11cm11cjEyOCJ9"  # <-- replace this

headers = {"Authorization": API_KEY}

url = "https://api.dataplatform.knmi.nl/edr/v1/collections/10-minute-in-situ-meteorological-observations/locations"

response = requests.get(url, headers=headers)
data = response.json()

print("Status:", response.status_code)

output_file = os.path.join("data/raw", "loactions.json")
with open(output_file, "w") as f:
     json.dump(data, f, indent=4)

print("Saved to:", output_file)