import os
import unittest
import pandas as pd
import sqlite3
from project.etl_pipeline.extractor import ExtractData as extractor
from project.etl_pipeline.transformer import TransformData as transformer
from project.etl_pipeline.loader import LoadData as loader


class TestDataPipeLine(unittest.TestCase):
    
    def setUp(self):
        # Set up sample data or test files if needed
        self.sample_data_url = "https://www.data.gov.cy/sites/default/files/PAFOS%20AIRPORT%20DAILY%20AIR%20TRAFFIC%202019.xlsx"
        self.weather_data_url = "http://bulk.meteostat.net/v2/daily/17600.csv.gz"
        self.years = [2019]
        self.db_path = os.path.join(os.getcwd(), "data", "project.sqlite")
        self.table_name = "airports_test_table"
        self.weather_data_headers = ['Date', 'tavg', 'tmin', 'tmax', 'percp','snow','wdir','wspd','wpgt','pres','tsun']
        
    def test_etl(self):
        data,sheet_name = extractor(self.sample_data_url).fetch_data()
        data = transformer(data,self.years).apply_transformations_atd(sheet_name)
        load_data = loader(data,self.table_name,self.db_path).load_data_at()
        
        with sqlite3.connect(self.db_path) as conn:
            query =f"SELECT * FROM {self.table_name}"
            loaded_test_data = pd.read_sql_query(query,conn)
            
        self.assertFalse(loaded_test_data.empty, "Loaded data should not be empty")
        self.assertEqual(len(load_data.data), len(loaded_test_data), "Number of rows should match")

if __name__ == '__main__':
    unittest.main()