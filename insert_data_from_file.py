import pandas as pd
from sqlalchemy import create_engine

DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@45.9.27.251:5440/hackaton'
engine = create_engine(DATABASE_URI)

# Load spreadsheet
xl = pd.ExcelFile('source_data/1.xlsx')

# Load a sheet into a DataFrame by its name
df = xl.parse('Sheet1')

# Write to PostgreSQL
df.to_sql('ApartmentBuildingsWithTEC', engine, schema='public', if_exists='append', index=False)

