from etl.extract import DataExtractor
from etl.transform import DataTransformer
from etl.load import DataLoader
import yaml 

if __name__ == "__main__":
    
    #load configuration fro YAML file
    with open('config/config.yaml', 'r') as f:
        config = yaml.safe_load(f)


    #extract data from sources
    data_extractor = DataExtractor(ticker ='APPL')
    extracted_data = data_extractor.extract_stock_data(period='5y')

    #Transform data
    data_transformer = DataTransformer(data=extracted_data)
    transformed_data = data_transformer.transform_stock_data()

    #load data into PostgreSQL
    data_loader = DataLoader()
    data_loader.load_data_psql()
