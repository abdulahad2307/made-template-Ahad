import pandas as pd
import sqlalchemy as sqlc

url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv" ## Loading url

dataframe = pd.read_csv(url, sep=';') ## reading csv

column_data_types = {
    "column1": sqlc.Integer(),
    "column2": sqlc.String(),
    "column3": sqlc.String(),
    "column4": sqlc.String(),
    "column5": sqlc.Integer(),
    "column6": sqlc.String(),
    "column7": sqlc.Float(),
    "column8": sqlc.Float(),
    "column9": sqlc.Integer(),
    "column10": sqlc.DECIMAL(),
    "column11": sqlc.String(),
    "column12": sqlc.String(),
    "geo_punkt": sqlc.Float()

} ## Assigning fitting built-in SQLite types to all columns

db_table_name = "airports.sqlite" 
engine = sqlc.create_engine(f"sqlite:///{db_table_name}", echo = True)
metadata = sqlc.MetaData()

sqlite_connection = engine.connect()

airports_table = sqlc.Table("airports",metadata)
#'''
for col, dt in column_data_types.items():
    airports_table.append_column(sqlc.Column(col,dt))
#'''
#metadata.create_all(engine)

dataframe.to_sql('airports','sqlite:///airports.sqlite', if_exists='replace', index=False)

''''
with engine.connect() as connection:
    dataframe.to_sql("temp_data_table", connection, index=False, if_exists = "replace")
    connection.execute(f"INSERT INTO airports SELECT * From temp_data_table;")
    connection.execute("DROP TABLE temp_table")
'''
print(f"Data has been successfully loaded into the SQLlite Database: {db_table_name}")


