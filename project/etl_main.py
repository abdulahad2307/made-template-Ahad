
import os
## self file imports
from etl_pipeline.extractor import ExtractData as ED
from etl_pipeline.transformer import TransformData as TD
from etl_pipeline.loader import LoadData as LD
#===================================================================#
#                          User Inputs                              #
#===================================================================#
years = [2018,2019,2020,2021]
weather_stations = [17600]
db_path = os.path.join(os.getcwd(), "data", "project.sqlite") #f"sqlite:///{db_name}"
print(db_path)

weather_data_headers = ['Date', 'tavg', 'tmin', 'tmax', 'percp','snow','wdir','wspd','wpgt','pres','tsun']
#===================================================================#
def main():
    
    ## ETL of air traffic Data
    
    for year in years:
        air_traffic_url = f"https://www.data.gov.cy/sites/default/files/PAFOS%20AIRPORT%20DAILY%20AIR%20TRAFFIC%20{year}.xlsx"
                
        ##Extract
        air_traffic_data,sheet_name = ED(air_traffic_url,).fetch_data()
        print(air_traffic_data)
        ##Transform
        air_traffic_transformed_data = TD(air_traffic_data,year).apply_transformations_atd(sheet_name)
        print(type(air_traffic_transformed_data))
        ## Load Data
        table_name = f"airports_daily_traffic_{year}"
        air_traffic_data_load = LD(air_traffic_transformed_data, table_name,db_path)
        air_traffic_data_load.load_data_wt()

    
    ## ETL Weather Data
    
    for station in weather_stations:
        weather_url = f"http://bulk.meteostat.net/v2/daily/{station}.csv.gz" #"https://bulk.meteostat.net/v2/daily/VYNT0.csv.gz"#
        
        ## Extract
        daily_weather_data = ED(weather_url).fetch_data()
        
        ## Transform    
        weather_transformed_data = TD(daily_weather_data,year).apply_transformations_wd(header = weather_data_headers)
        #print(weather_transformed_data)

        ## Load Data
        weather_data_load = LD(weather_transformed_data,"daily_weather_data",db_path)   
        weather_data_load.load_data_wt()
        

if __name__ == "__main__":
    main()