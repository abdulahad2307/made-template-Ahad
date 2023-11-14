## Data Extraction from designated URL 
import pandas as pd
import sqlalchemy as sqlc

url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv" ## Loading url

dataframe = pd.read_csv(url, sep=';') ## reading csv

column_data_types = {
    "column1": sqlc.Integer(),
    "column2": sqlc.String(),
    "column3": sqlc.String(),
    "column4": sqlc.String(),
    "column5": sqlc.String(),
    "column6": sqlc.String(),
    "column7": sqlc.Float(),
    "column8": sqlc.Float(),
    "column9": sqlc.Integer(),
    "column10": sqlc.DECIMAL(),
    "column11": sqlc.String(),
    "column12": sqlc.String(),
    "geo_punkt": sqlc.Float()

} ## Assigning fitting built-in SQLite types to all columns

db_name = "airports.sqlite" ## database_name
db_path = f"sqlite:///{db_name}" ## dtabase_path
engine = sqlc.create_engine(f"{db_path}") ## SQLAlchemy Eninge
metadata = sqlc.MetaData()

sqlite_connection = engine.connect() ## SQLite Connection

airports_table = sqlc.Table("airports",metadata)

for col, dt in column_data_types.items(): ## Assiging defined Column DataTypes
    airports_table.append_column(sqlc.Column(col,dt))
'''
metadata.create_all(engine)

with engine.connect() as connection: ## Data loading from Dataframe to SQLite databse using SQLAlchemy engine
    dataframe.to_sql('temp_table',connection, if_exists='replace', index=False)
    connection.execute(f"INSERT INTO airports SELECT * FROM temp_table;")
    connection.execute ("DROP TABLE temp_table")
'''
dataframe.to_sql('airports',f"{db_path}", if_exists='replace', index=False)

print(f"Data has been successfully loaded into the SQLlite Database: {db_name}")


