## imports
import os
import sqlalchemy as sqlc

class LoadData:
    
    def __init__(self,data,table_name,db_path ):
        self.data = data
        self.table_name = table_name
        self.db_path = db_path
        
        
    '''
    def create_table(self):
        engine = sqlc.create_engine(f"sqlite:::///{self.db_path}")
        metadata = sqlc.MetaData()
        table = sqlc.Table(self.table_name,metadata)
        metadata.create_all(engine)
        
        return table
    '''
    def load_data(self, data):
        #print(data.head())
        #print(self.db_path)
        data.to_sql(self.table_name,f'sqlite:///{os.path.abspath(self.db_path)}/projectdata.sqlite',if_exists='replace', index=False)
        '''
        with sqlc.create_engine(f"sqlite:///{self.db_path}").connect() as connection:
            try:
                self.data.to_sql("temp_table",connection, index = False,if_exists = "replace")
                connection.execute(f'INSERT INTO {self.table_name} SELECT * FROM temp_table;')
            except Exception as e:
                print(f"An error occured during data loading: {str(e)}")
            finally:
                connection.execute('DROP TABLE temp_table')
        '''