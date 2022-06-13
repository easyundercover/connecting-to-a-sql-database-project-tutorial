

# 1) Connect to the database here using the SQLAlchemy's create_engine function
import pandas as pd
import numpy as np
import sqlalchemy as db 
import os
from dotenv import load_dotenv
from sqlalchemy import *

load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_DATABASE = os.getenv('DB_DATABASE')
DB_NAME = os.getenv('DB_NAME')
#Esto no es estrictamente necesario pero es una buena práctica

print(DB_HOST)

def connect():
    global engine # this allows us to use a global variable called engine
    # A "connection string" is basically a string that contains all the databse credentials together
    connection_string = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}?autocommit=true"
    print("Starting the connection...")
    engine = create_engine(connection_string)
    engine.connect()
    return engine

connect()

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
#engine.execute("""
#CREATE TABLE publishers(
#publisher_id INT NOT NULL,
#name VARCHAR(255) NOT NULL,
#PRIMARY KEY(publisher_id)
#);
#""")

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
engine.execute("INSERT INTO publishers(publisher_id, name) values (1,'O Reilly Media');")

# 4) Use pandas to print one of the tables as dataframes using read_sql function
df = pd.read_sql("Select * from publishers;", engine)