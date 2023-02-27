import os
from dotenv import load_dotenv
import pandas as pd
import sqlalchemy as alch


load_dotenv()

#read pd dataframe output from the extract and transform .py

df = pd.read_csv("data\glassdoor_tableau.csv", index_col=0)

# connect do MySQL local server, upload dataframe to a new table, or append if existing

password = os.getenv("password")
dbName="glassdoor_reviews"
connectionData = f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)
df.to_sql("reviews", if_exists="append", con=engine, index=False)


def query_server(sql_query):
    return pd.DataFrame(pd.read_sql_query(sql_query, engine))
