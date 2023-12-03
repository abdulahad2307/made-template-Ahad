## imports
import os
import sqlite3

class LoadData:
    
    def __init__(self,data,table_name,db_path ):
        self.data = data
        self.table_name = table_name
        self.db_path = db_path
        
    def load_data_at(self):
        connection = sqlite3.connect(self.db_path)
        
        for sheet_name, dataframe in self.data.items():
            table_name = self.table_name + sheet_name
            dataframe.to_sql(table_name,connection,if_exists='replace', index=False)
    
    def load_data_wt(self):
        connection = sqlite3.connect(self.db_path)
        
        self.data.to_sql(self.table_name,connection,if_exists='replace', index=False)
