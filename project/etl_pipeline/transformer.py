import pandas as pd

class TransformData:
    
    def __init__(self,data,year):
        self.data = data
        self.year = year
    
    ##AirTrafficData
    def apply_transformations_atd(self,sheet_name):
        combined_dataframes = pd.DataFrame()
        print(sheet_name)
        for df, sheet_name_val in zip(self.data, sheet_name):
            df['Date'] = str(self.year) + '-' + sheet_name_val + '-' + df['DAY'].astype(str)
            
            
            df['Date'] = pd.to_datetime(df['Date'], format='%Y-%b-%d',errors='coerce')
            df['Date'] = df['Date'].dt.date
            
            # Call the rename_columns function
            df = self.airDataHeaderRename(df)
            
            #Columns_reset
            df.insert(0, 'Date', df.pop('Date'))
            print(df)
            
            combined_dataframes = combined_dataframes.append(df, ignore_index=True)
        
        return combined_dataframes
        #data = self.airDataHeaderRename()
        #print(type(data))
        #data = self.addingDate(data)
        #print(type(data))
        
        
        #return data
    
    ##WeatherData
    def apply_transformations_wd(self, header):
        data = self.weatherDataAddHeader(header)
        
        return data
        
# ======================== airport_data_transformation Operations =========================#

    def airDataHeaderRename(self,df):
        
        column_name_mapping = {
            'DAY': 'Day',
            'R 11': 'IntlLandings_R11', 
            'R 29': 'IntlLandings_R29', 
            'TTL': 'IntlLandings_TTL', 
            'R 11.1': 'IntlTakeOffs_R11',
            'R 29.1': 'IntlTakeOfdss_R29',
            'TTL.1': 'IntlTakeOfdss_TTL',
            'R 11.2': 'DomslLandings_R11', 
            'R 29.2': 'DomsLandings_R29', 
            'TTL.2': 'DomsLandings_TTL', 
            'R 11.3': 'DomsTakeOffs_R11',
            'R 29.3': 'DomsTakeOffss_R29',
            'TTL.3': 'DomsTakeOffss_TTL',
            'A/C': 'TransitA/C',
            'HEL': 'TransitHEL',
            'TTL.4': 'TransitTTL',
            'LND': 'HeliCopLND',
            'T/O': 'HeliCopT/O',
            'TTL.5': 'HeliCopTTL',
            'T/G': 'T/G',
            'TTL.6': 'TotalSum(TTL)',
            
            }
        df.rename(columns=column_name_mapping, inplace=True)
        return df
        
        '''
        return {sheet_name: sheet_data.rename({
            'DAY': 'Day',
            'R 11': 'IntlLandings_R11', 
            'R 29': 'IntlLandings_R29', 
            'TTL': 'IntlLandings_TTL', 
            'R 11.1': 'IntlTakeOffs_R11',
            'R 29.1': 'IntlTakeOfdss_R29',
            'TTL.1': 'IntlTakeOfdss_TTL',
            'R 11.2': 'DomslLandings_R11', 
            'R 29.2': 'DomsLandings_R29', 
            'TTL.2': 'DomsLandings_TTL', 
            'R 11.3': 'DomsTakeOffs_R11',
            'R 29.3': 'DomsTakeOffss_R29',
            'TTL.3': 'DomsTakeOffss_TTL',
            'A/C': 'TransitA/C',
            'HEL': 'TransitHEL',
            'TTL.4': 'TransitTTL',
            'LND': 'HeliCopLND',
            'T/O': 'HeliCopT/O',
            'TTL.5': 'HeliCopTTL',
            'T/G': 'T/G',
            'TTL.6': 'TotalSum(TTL)',
            
            }, axis = 1) 
                     for sheet_name, sheet_data in self.data.items()}
        '''
    def addingDate(self,data):
        
        for sheet_name, sheet_data in data.items():
            print(sheet_name,sheet_data)
            sheet_data['Day'] = sheet_data['Day']
            sheet_data['Month'] = sheet_name
            sheet_data['Year'] = self.year
            
            sheet_data['Date'] = pd.to_datetime(sheet_data['Year'].astype(str) + '-' +
                                            sheet_data['Month'].astype(str) + '-' +
                                            sheet_data['Day'].astype(str),  format='%Y-%b-%d', errors='coerce')
    
        
        
#==================================== weather Data Transformation Operations===========#

    def weatherDataAddHeader(self, header):
        if header is not None:
            self.data.columns = header
        return self.data
    
    