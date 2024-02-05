import pandas as pd
from sqlalchemy import create_engine

def create_connection():
    """
    Create a connection to the MySQL database.

    Returns:
    sqlalchemy.engine.base.Engine: The connection to the MySQL database.
    """
    # Replace 'username', 'password', 'localhost', 'port' with your actual MySQL credentials and server details

    engine = create_engine('mysql+pymysql://username:password@localhost:port/cognizant_forage')
    return engine

def load_sales_data(engine):
    """
    Load sales data from a MySQL database into a Pandas DataFrame.

    Parameters:
    engine (sqlalchemy.engine.base.Engine): The connection to the MySQL database.

    Returns:
    pd.DataFrame: The loaded sales data.
    """
    df_sales = pd.read_sql('SELECT * FROM sales', engine)

    if df_sales is not None:
        return df_sales
    else:
        print("Empty DF")

def load_stock_levels(engine):
    """
    Load stock levels data from a MySQL database into a Pandas DataFrame.

    Parameters:
    engine (sqlalchemy.engine.base.Engine): The connection to the MySQL database.

    Returns:
    pd.DataFrame: The loaded stock levels data.
    """
    df_stock_levels = pd.read_sql('SELECT * FROM sensor_stock_levels', engine)
    return df_stock_levels

def load_temperature_data(engine):
    """
    Load temperature data from a MySQL database into a Pandas DataFrame.

    Parameters:
    engine (sqlalchemy.engine.base.Engine): The connection to the MySQL database.

    Returns:
    pd.DataFrame: The loaded temperature data.
    """
    df_temperature = pd.read_sql('SELECT * FROM sensor_storage_temperature', engine)
    return df_temperature

# if __name__ == "__main__":
#     connection_engine = create_connection()
#     print(load_sales_data(connection_engine))