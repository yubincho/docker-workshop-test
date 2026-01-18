
import sys

print('arguments', sys.argv)
print('hello pipeline')

month = int(sys.argv[1])

import pandas as pd

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df.head())

df2 = pd.DataFrame({"day": [1,2], "num_passengers": [3,4]})
df2['month'] = month
print(df2.head())

df2.to_parquet(f"output_day_{sys.argv[1]}.parquet")

print(f"Running pipeline for day {month}")



