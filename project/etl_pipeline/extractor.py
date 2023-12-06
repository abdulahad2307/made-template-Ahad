#imports

import pandas as pd

class ExtractData:
    
    def __init__(self,url):
        self.url = url
        self.data= None
        self.sheet_name = []
        
    def fetch_data(self):
        if self.url.endswith('.xlsx'):
            #self.data = pd.read_excel(self.url,sheet_name=None, skiprows=1,header=2)
            
            xls = pd.ExcelFile(self.url)
            #Sheet_name_Extraction
            for sheet_name in xls.sheet_names:
                self.sheet_name.append(sheet_name)
            
            #Sheet_data_Extraction
            self.data = [xls.parse(sheet_name, skiprows=1,header=2)for sheet_name in xls.sheet_names]
            
            return self.data,self.sheet_name
        elif self.url.endswith('.gz'):
            self.data = pd.read_csv(self.url,compression='gzip')
            return self.data
        else:
            raise ValueError(f"Unsupported file formet from the url: {self.url}")
        