from sqlalchemy import create_engine
import pandas as pd
from pandas import DataFrame


CONNECTION = "postgresql+psycopg2://postgres:postgres@localhost:54320/postgres"


def create_tables(schema):
    tables = schema.split(";")
    conn = create_engine(CONNECTION)

    for table in tables:
        if table.startswith("CREATE"):
            try:
                with conn:
                    transaction = conn.begin()
                    conn.execute(table)
                    transaction.commit()
            except Exception as e:
                print(e)
    print("All tables were created successfully!")


def save_data(table:str, data:DataFrame):
    conn = create_engine(CONNECTION)
    data.to_sql(name=table, con=conn,if_exists="replace")
