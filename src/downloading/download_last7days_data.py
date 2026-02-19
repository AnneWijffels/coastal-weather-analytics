import os
import requests
import json
import pandas as pd
from datetime import datetime, timedelta, timezone

# =========================
# CONFIGURATION
# =========================

API_KEY = "eyJvcmciOiI1ZTU1NGUxOTI3NGE5NjAwMDEyYTNlYjEiLCJpZCI6ImU5MTIyN2JiODQyMjQwYWNiOTIzNzExZjEyM2YzZTI5IiwiaCI6Im11cm11cjEyOCJ9"  # <-- replace this

STATION_ID = "0-20000-0-06209"  # This is the station with name "Ijmond"
COLLECTION = "10-minute-in-situ-meteorological-observations"

# =========================
# DATE RANGE (last 7 days)
# =========================

end_date = datetime.now(timezone.utc)
start_date = end_date - timedelta(days=7)

datetime_range = f"{start_date.strftime('%Y-%m-%dT%H:%M:%SZ')}/{end_date.strftime('%Y-%m-%dT%H:%M:%SZ')}"

# =========================
# BUILD REQUEST
# =========================

url = f"https://api.dataplatform.knmi.nl/edr/v1/collections/10-minute-in-situ-meteorological-observations/locations/{STATION_ID}"

params = {
    "f": "CoverageJSON",
    "datetime": datetime_range
}

headers = {
    "Authorization": API_KEY
}

print("Requesting data...")
print("Datetime range:", datetime_range)

response = requests.get(url, headers=headers, params=params)

# =========================
# PARSE JSON DIRECTLY
# =========================

data = response.json()

# KNMI returns CoverageCollection
coverage = data["coverages"][0]

times = coverage["domain"]["axes"]["t"]["values"]
parameters = data["parameters"].keys()
ranges = coverage["ranges"]

df = pd.DataFrame(index=pd.to_datetime(times))

for param in parameters:
    df[param] = coverage["ranges"][param]["values"]

df.index.name = "timestamp"

# =========================
# SAVE CLEAN FILES
# =========================

os.makedirs("data/processed", exist_ok=True)

# Save clean CSV (real CSV)
df.to_csv(f"data/processed/{STATION_ID}_last7days_clean.csv")

# Save original JSON if you want archive
with open(f"data/raw/{STATION_ID}_last7days.json", "w") as f:
    import json
    json.dump(data, f)

print("✅ Data processed and saved.")
print(df.head())