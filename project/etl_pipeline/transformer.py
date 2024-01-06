import pandas as pd

class TransformData:
    
    def __init__(self,data,year):
        self.data = data
        self.year = year
    
    ##AirTrafficData
    def apply_transformations_atd(self,sheet_name):
        combined_dataframes = pd.DataFrame()
        #print(sheet_name)
        for df, sheet_name_val in zip(self.data, sheet_name):
            df['Date'] = str(self.year) + '-' + sheet_name_val + '-' + df['DAY'].astype(str)
            #print(df)
            
            df['Date'] = pd.to_datetime(df['Date'], format='%Y-%b-%d',errors='coerce')
            df['Date'] = df['Date'].dt.date
            
            #print(df)
            
            # Call the rename_columns function
            df = self.airDataHeaderRename(df)
            
            #Columns_reset
            df.insert(0, 'Date', df.pop('Date'))
            #print(df)
            
            #combined_dataframes = combined_dataframes.append(df, ignore_index=True)
            combined_dataframes = pd.concat([combined_dataframes,df],ignore_index=True)
            
            combined_dataframes = self.cleanATD(combined_dataframes)
        return combined_dataframes
            
    ##WeatherData
    def apply_transformations_wd(self, header):
        df = self.weatherDataAddHeader(header)
        
        #print(type(df['Date']))
        
        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d',errors='coerce')
        
        df = self.weatherDataFilter(df)
        df['Date'] = df['Date'].dt.date
        
        return df
        
# ======================== airport_data_transformation Operations =========================#

    def airDataHeaderRename(self,df):
        
        column_name_mapping = {
            'DAY': 'Day',
            'R 11': 'IntlLandings_R11', 
            'R 29': 'IntlLandings_R29', 
            'TTL': 'IntlLandings_TTL', 
            'R 11.1': 'IntlTakeOffs_R11',
            'R 29.1': 'IntlTakeOffs_R29',
            'TTL.1': 'IntlTakeOffs_TTL',
            'R 11.2': 'DomsLandings_R11', 
            'R 29.2': 'DomsLandings_R29', 
            'TTL.2': 'DomsLandings_TTL', 
            'R 11.3': 'DomsTakeOffs_R11',
            'R 29.3': 'DomsTakeOffs_R29',
            'TTL.3': 'DomsTakeOffs_TTL',
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
    
    def cleanATD(self, df):
        df = df [df['TotalSum(TTL)'] > 0]
        #print(df)
        return df
            
    
        
        
#==================================== weather Data Transformation Operations===========#

    def weatherDataAddHeader(self, header):
        if header is not None:
            self.data.columns = header
        return self.data
    
    def weatherDataFilter(self,df):
        filtred_df = pd.DataFrame()
        
        for year in self.year:
            new_df = df[df['Date'].dt.year== year]
            filtred_df = filtred_df.append(new_df)
    
        return filtred_df