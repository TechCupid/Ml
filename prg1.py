import pandas as pd

try:
    df = pd.read_csv(input("CSV file path: "))
    print("\n=> Data loaded.\n")
except Exception as e:
    print("\n=> Error:", e)
    exit()

df.fillna(0, inplace=True)
df.fillna("Unknown", inplace=True)
df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)
print("\n=> Data Cleaned.\n")

print("\n=> Adding Experience Level column.\n")

df['Experience_Level'] = pd.cut(df['Experience'], [-1, 2, 5, float('inf')], labels=['Beginner', 'Intermediate', 'Expert'])

print("\n=> Original:\n", df[['Years','Experience','Salary']].head())
print("\n=> With Experience Level:\n", df.head())

df.to_csv("cleaned_data.csv", index=False)
print("\n=> Saved to 'cleaned_data.csv'")
