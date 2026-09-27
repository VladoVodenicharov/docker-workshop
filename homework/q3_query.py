import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5433/ny_taxi')

df_green = pd.read_parquet('green_tripdata_2025-11.parquet')
df_green.to_sql(name='green_taxi_trips', con=engine, if_exists='replace', index=False)
#df_green.head()

df_zones = pd.read_csv('taxi_zone_lookup.csv')
df_zones.to_sql(name='taxi_zone_lookup', con=engine, if_exists='replace', index=False)
#df_zones.head()

query ="""
SELECT COUNT(*)
FROM green_taxi_trips
WHERE trip_distance <=1
AND lpep_dropoff_datetime < '2025-12-01';
"""

print(pd.read_sql(query, con=engine))