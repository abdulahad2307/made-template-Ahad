#imports

import pandas as pd

class ExtractData:
    
    def __init__(self,url):
        self.url = url
        
    def fetch_data(self):
        if self.url.endswith('.xlsx'):
            return pd.read_excel(self.url)
        elif self.url.endswith('.gz'):
            return pd.read_csv(self.url,compression='gzip')
        else:
            raise ValueError(f"Unsupported file formet from the url: {self.url}")