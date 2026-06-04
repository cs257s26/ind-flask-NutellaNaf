"""datasource.py

File to execute two queries scripted in Python for Part 2 of the [individual] Database assignment

Boilerplate code (connect(), main()) provided by Amy Csizmar Dalal. Thanks Amy!
"""

import psycopg2 as ps
from psycopg2 import sql as psysql
from . import psqlConfig as config

def connect():
    """
    Establishes a connection to the database with the following credentials:
        user - username, which is also the name of the database
        password - the password for this database on perlman

    Returns: a database connection.

    Note: exits if a connection cannot be established.
    """
    try:
        connection = ps.connect(database=config.database, user=config.user, password=config.password, host="localhost")
    except Exception as e:
        print("Connection error: ", e)
        exit()
    return connection

def fetch_column_names(connection) -> list:
    """A helper query to fetch column names in the table.
    
    Args:
        connection: a psycopg2 connection

    Returns:
        List[n]: A list of all the columns.
    """
    try:
        cursor = connection.cursor()
        query = """
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = 'llm_energy';
        """
        cursor.execute(query)

        results = cursor.fetchall()
        return [item[0] for item in results]

    except Exception as e:
        print("Something went wrong when executing the query: ", e)
        # return None

def fetch_data_length(connection) -> int:
    """A helper query to fetch the "data length" a.k.a. the number of rows in the table.
    
    Args:
        connection: a psycopg2 connection

    Returns:
        int: The number of rows in a table, based on the primary key.
    """
    try:
        cursor = connection.cursor()
        query = "SELECT model_name FROM llmenergy"
        cursor.execute(query)
        return len(cursor.fetchall())

    except Exception as e:
        print (f"Something went wrong when executing the query: {e}")
        # return None

def get_top_n_column_values_SQL(connection, column_of_interest: str, n: int) -> list:
    """ 
    Display the top n models in a given column.

    This function only works with columns that have numerical values. 
    If the column given is strictly non-numerical values, user is prompted to select a different column.

    Args:
        column_of_interest: A string representing the column name

    Returns:
        column_data: List[List(2))] A list of lists with the top 5 values in that column. 
        The first element of the tuple is the name of the model, second element is the value.

    Raises:
        ValueError: A non-numerical column was input OR n is greater than the length-1 of the column.
    """
    try:
        valid_columns = fetch_column_names(connection)
        if column_of_interest not in valid_columns:
            raise ValueError("Input a valid model name.")

        if ((column_of_interest == "model_name") | (column_of_interest == "gpu_type") | (column_of_interest == "data_center_region")):
            raise ValueError("Input a non-numerical column.")
    
        # Ensure data is loaded + handle case where column is not in csv.
        data_len = fetch_data_length(connection)
        if (n > data_len-1):
            print("FAIL AT SECOND COND")
            raise ValueError("Input a number less than the total length of the row")
        
        cursor = connection.cursor()
        query = psysql.SQL("SELECT model_name, {column} FROM llmenergy ORDER BY {column} DESC NULLS LAST LIMIT %s;")
        cursor.execute(query.format(column = psysql.Identifier(column_of_interest)), (n,))
        return cursor.fetchall()

    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        # raise ValueError
        # return None

def get_whole_column_SQL(connection, column_of_interest: str) -> list:
    """ 
    Get all values in a given column.

    Args:
        column_of_interest: A string representing the column name

    Returns:
        column_data: List[] A list of all values in that column. 

    Raises:
        ValueError: Invalid column was input.
    """
    try:
        valid_columns = fetch_column_names(connection)
        
        if column_of_interest not in valid_columns:
            print("FALSE!")
            raise ValueError("Input a valid model name.")
        
        cursor = connection.cursor()
        query = psysql.SQL("SELECT {column} FROM llmenergy")
        cursor.execute(query.format(column = psysql.Identifier(column_of_interest)))
        return cursor.fetchall()

    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        raise ValueError("Input a valid model name.")
        # return None

def get_row_by_model_name_SQL(connection, model_name_entry) -> list:
    """ 
    Give the row of information corresponding to a model name.

    Args:
        model_name_entry: String. A string representing the name of the model

    Returns:
        corresponding_row: List. The row corresponding to this model_name

    Raises:
        ValueError: If an invalid model name is provided.
        Exception: SQL exception.
    """
    try:
        valid_names = get_whole_column_SQL(connection, "model_name")
        model_name_tuple = (model_name_entry, )
        
        if model_name_tuple not in valid_names:
            raise ValueError("Input a valid model name.")

        cursor = connection.cursor()
        query = "SELECT * FROM llmenergy WHERE model_name = %s;"
        cursor.execute(query, (model_name_entry,))
        corresponding_row = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        return [column_names, list(corresponding_row[0])]

    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        # return None



def main():
    # Connect to the database
    connection = connect()

    # Execute a simple query: how many earthquakes above the specified magnitude are there in the data?
    results = get_top_n_column_values_SQL(connection, "nah", 5)
    
    if results is not None:
        print("Query results: ")
        for item in results:
            print(item)

    # Disconnect from database
    connection.close()

main()
