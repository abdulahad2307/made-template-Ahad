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
        data_types = self.data_type()
        self.data.to_sql(self.table_name,connection,if_exists='replace', index=False,dtype = data_types)
    
    def load_data_wt(self):
        connection = sqlite3.connect(self.db_path)
        data_types = self.data_type()
        self.data.to_sql(self.table_name,connection,if_exists='replace', index=False,dtype = data_types)

# =========================== Data Types ================================================#
    def data_type(self):
        if 'airports' in self.table_name:
            atd_dtype = {
                'IntlLandings_R11': 'REAL', 
                'IntlLandings_R29': 'REAL', 
                'IntlLandings_TTL':'REAL', 
                'IntlTakeOffs_R11':'REAL',
                'IntlTakeOfdss_R29':'REAL',
                'IntlTakeOfdss_TTL':'REAL',
                'DomslLandings_R11':'REAL', 
                'DomsLandings_R29':'REAL', 
                'DomsLandings_TTL':'REAL', 
                'DomsTakeOffs_R11':'REAL',
                'DomsTakeOffss_R29':'REAL',
                'DomsTakeOffss_TTL':'REAL',
                'TransitA/C':'REAL',
                'TransitHEL':'REAL',
                'TransitTTL':'REAL',
                'HeliCopLND':'REAL',
                'HeliCopT/O':'REAL',
                'HeliCopTTL':'REAL',
                'T/G':'REAL',
                'TotalSum(TTL)':'REAL',
            }
            return atd_dtype
        elif 'weather' in self.table_name:
            
            wd_dtype = {
                'tavg':'REAL',
                'tmin':'REAL',
                'tmax':'REAL',
                'percp':'REAL',
                'snow':'REAL',
                'wdir':'REAL',
                'wspd':'REAL',
                'wpgt':'REAL',    
                'pres':'REAL',
                'tsun':'REAL',
            }
            return wd_dtype
        else:
            raise ValueError (f"Table:{self.table_name} Data Type Not Found")