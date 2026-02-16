import os
import requests
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
# SAVE DATA
# =========================

if response.status_code == 200:
    os.makedirs("data/raw", exist_ok=True)

    filename = f"data/raw/{STATION_ID}_last7days.csv"

    with open(filename, "w") as f:
        f.write(response.text)

    print("✅ Data successfully saved to:", filename)

else:
    print("❌ Request failed")
    print("Status code:", response.status_code)
    print(response.text)
