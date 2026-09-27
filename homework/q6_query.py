import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5433/ny_taxi')

df_green = pd.read_parquet('green_tripdata_2025-11.parquet')
df_green.to_sql(name='green_taxi_trips', con=engine, if_exists='replace', index=False)
print(df_green['PULocationID'].head(3))

df_zones = pd.read_csv('taxi_zone_lookup.csv')
df_zones.to_sql(name='taxi_zone_lookup', con=engine, if_exists='replace', index=False)
print(df_zones['LocationID'].head(3))

#print(df_green.columns.str.lower())
#print(df_zones.columns.str.lower())
#print(df_green.dtypes)
#print(df_zones.dtypes)

query ="""
SELECT dropoff_zone."Zone" AS dropoff_zone,
             MAX(trip.tip_amount) AS largest_tip
FROM green_taxi_trips AS trip
JOIN taxi_zone_lookup AS pickup_zone
    ON trip."PULocationID" = pickup_zone."LocationID"
JOIN taxi_zone_lookup AS dropoff_zone
    ON trip."DOLocationID" = dropoff_zone."LocationID"
WHERE pickup_zone."Zone" = 'East Harlem North'
GROUP BY dropoff_zone."Zone"
ORDER BY largest_tip DESC
LIMIT 10
"""

print(pd.read_sql(query, con=engine))