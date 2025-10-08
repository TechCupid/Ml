import pandas as pd
def get_date_from_user(prompt):
    while True:
        try: return pd.to_datetime(input(prompt))
        except: print("Use YYYY-MM-DD format.")

start_date = get_date_from_user("\n =>Enter the start date (YYYY-MM-DD): ")
end_date = get_date_from_user("\n =>Enter the end date (YYYY-MM-DD): ")

df = pd.DataFrame({'date': pd.date_range(start=start_date, end=end_date)})

print("\n Extracting features from date data...")
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day_of_month"] = df["date"].dt.day
df["day_of_week"] = df["date"].dt.dayofweek
df["is_weekend"] = df["day_of_week"].isin([5, 6]).astype(int)
df["day_name"] = df["date"].dt.day_name()

print("\n =>Extracted Features DataFrame\n ")
print(df)
