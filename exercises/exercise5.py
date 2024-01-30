import urllib.request
import zipfile
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float

zip_file = "https://gtfs.rhoenenergie-bus.de/GTFS.zip"
zip_path = "GTFS.zip"
required_filename = "stops.txt" ## Required File

urllib.request.urlretrieve(zip_file, zip_path)
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extract(required_filename)

columns = ["stop_id", "stop_name", "stop_lat", "stop_lon", "zone_id"] ## Filtering Required Columns

df = pd.read_csv(filepath_or_buffer= required_filename, usecols= columns)

df = df[df["zone_id"] == 2001] ## Filtering data from zone 2001

df["stop_name"] = df["stop_name"].astype(str) ## Validation on names

valid_coordinates_range = (-90, 90)
valid_lat_range = df["stop_lat"].between(*valid_coordinates_range) ## Validation on Coordinates - latitutde 
valid_lon_range = df["stop_lon"].between(*valid_coordinates_range) ## Validation on Coordinates - longitude
df = df[valid_lat_range & valid_lon_range] 

engine = create_engine('sqlite:///gtfs.sqlite') ## Creating alchemy engine with database name
metadata = MetaData()
stops_table = Table('stops', metadata, Column('stop_id', Integer, primary_key=True),Column('stop_name', String),Column('stop_lat', Float),Column('stop_lon', Float),Column('zone_id', Integer))

metadata.create_all(engine)

dtype={'stop_id': Integer,'stop_name': String,'stop_lat': Float,'stop_lon': Float,'zone_id': Integer} ## Fitting datatypes

df.to_sql('stops', con=engine, if_exists='replace', index=False, dtype=dtype) ## data loading