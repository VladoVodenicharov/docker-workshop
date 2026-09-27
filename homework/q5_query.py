import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5433/ny_taxi')

df_green = pd.read_parquet('green_tripdata_2025-11.parquet')
df_green.to_sql(name='green_taxi_trips', con=engine, if_exists='replace', index=False)
print(df_green['PULocationID'].head(3))

df_zones = pd.read_csv('taxi_zone_lookup.csv')
df_zones.to_sql(name='taxi_zone_lookup', con=engine, if_exists='replace', index=False)
print(df_zones['LocationID'].head(3))

print(df_green.columns.str.lower())
#print(df_zones.columns.str.lower())
#print(df_green.dtypes)
#print(df_zones.dtypes)

query ="""
    SELECT zone."Zone", SUM(trip.fare_amount) as total_amount
    FROM green_taxi_trips as trip
    INNER JOIN taxi_zone_lookup as zone
        ON trip."DOLocationID" = zone."LocationID"
    WHERE DATE(trip.lpep_pickup_datetime) = '2025-11-18' AND DATE(trip.lpep_dropoff_datetime) = '2025-11-18'
    GROUP BY zone."Zone"
    ORDER BY total_amount DESC
    LIMIT 5
"""

print(pd.read_sql(query, con=engine))