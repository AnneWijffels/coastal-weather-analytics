import pandas as pd

df = pd.read_csv(
    "data/processed/0-20000-0-06209_last7days_clean.csv",
    parse_dates=["timestamp"],
    index_col="timestamp"
)

print("Max wind speed:", df["ff"].max())
print("Max gust:", df["gff"].max())
print("Average wind speed:", df["ff"].mean())

daily_max_wind = df["ff"].resample("D").max()
print(daily_max_wind)

dominant_dir = df["dd"].mean()
print("Average wind direction:", dominant_dir)

df["dd"].hist(bins=36)

gust_ratio = df["gff"] / df["ff"]
print("Average gust factor:", gust_ratio.mean())

threshold = df["ff"].quantile(0.95)
strong_winds = df[df["ff"] > threshold]

print("High wind events:")
print(strong_winds)
