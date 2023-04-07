from pandas import pd
from sqlalchemy import create_engine

class DataLoader:

    def load_data_psql(data,table_name, db_config):
        engine = create_engine(db_config)
        data.to_sql(table_name,engine,if_exists ='replace',index=False)

    
