
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
    

    ## Transform
    
    air_traffic_transformed_data = TD(air_traffic_data).transformations()
    #(air_traffic_transformed_data)
    weather_transformed_data = TD(daily_weather_data).transformations()
    #print(weather_transformed_data)
    
    ## Load Data
    
    air_traffic_data_load = LD(air_traffic_transformed_data, "airports_daily_traffic_2019",db_path)
    print(type(air_traffic_data_load))
    
    weather_data_load = LD(weather_transformed_data,"daily_weather_data",db_path)
    print(type(air_traffic_data_load))
    
    #air_traffic_data_table = air_traffic_data_load.create_table()
    
    air_traffic_data_load.load_data(air_traffic_transformed_data)
    weather_data_load.load_data(weather_transformed_data)
    

if __name__ == "__main__":
    main()