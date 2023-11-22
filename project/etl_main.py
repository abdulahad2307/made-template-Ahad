
import os
## self file imports
from etl_pipeline.extractor import ExtractData as ED
from etl_pipeline.transformer import TransformData as TD
from etl_pipeline.loader import LoadData as LD
#===================================================================#
#                          User Inputs                              #
#===================================================================#
weather_url = "https://bulk.meteostat.net/v2/daily/17600.csv.gz"
air_traffic_url = "https://www.data.gov.cy/sites/default/files/PAFOS%20AIRPORT%20DAILY%20AIR%20TRAFFIC%202019.xlsx"
db_path = os.path.join(os.getcwd(), "data") #f"sqlite:///{db_name}"
print(db_path)
#===================================================================#
def main():
    
    ## Extraction of Data
    
    air_traffic_data = ED(air_traffic_url).fetch_data()
    daily_weather_data = ED(weather_url).fetch_data()
    

    

if __name__ == "__main__":
    main()