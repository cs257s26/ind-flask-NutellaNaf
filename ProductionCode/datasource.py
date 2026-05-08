"""datasource.py

File to execute two queries scripted in Python for Part 2 of the [individual] Database assignment

Boilerplate code (connect(), main()) provided by Amy Csizmar Dalal. Thanks Amy!
"""

import psycopg2 as ps
import psqlConfig as config

def connect():
    """Establishes a connection to the database with the following credentials:
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
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM information_schema.columns WHERE table_name = llmenergy;"
        cursor.execute(query)
        return cursor.fetchall()

    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None

def fetch_data_length(connection) -> int:
    try:
        cursor = connection.cursor()
        query = "SELECT model_name FROM llmenergy"
        cursor.execute(query)
        return len(cursor.fetchall())

    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None



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
        if ((column_of_interest == "Model name") | (column_of_interest == "gpu_type") | (column_of_interest == "data_center_region")):
            # print("FAIL AT FIRST COND")
            raise ValueError("Input a non-numerical column.")
    
        data_len = fetch_data_length(connection)
        print(data_len)
        # Ensure data is loaded + handle case where column is not in csv.
        if (n > data_len-1):
            print("FAIL AT SECOND COND")
            raise ValueError("Input a number less than the total length of the row")
        
        cursor = connection.cursor()
        query = "SELECT model_name, %s FROM llmenergy ORDER BY %s DESC NULLS LAST LIMIT %s;"
        cursor.execute(query, (column_of_interest, column_of_interest, n))
        return cursor.fetchall()

    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None

def get_row_by_model_name_SQL(connection, model_name_entry) -> list:
    """ 
    Give the row of information corresponding to a model name.

    Args:
        model_name_entry: String. A string representing the name of the model

    Returns:
        corresponding_row: List. The row corresponding to this model_name

    Raises:
        Exception: SQL exception based on the case.
    """
    try:
        cursor = connection.cursor()
        query = "SELECT model_name FROM llmenergy;"
        cursor.execute(query)
        valid_names = cursor.fetchall()
        
        if model_name_entry not in valid_names:
            raise ValueError("Input a valid model name.")
        # if ((column_of_interest == "Model name") | (column_of_interest == "gpu_type") | (column_of_interest == "data_center_region")):
        #     # print("FAIL AT FIRST COND")
        #     raise ValueError("Input a non-numerical column.")
        
        # TO-DO: DEBUG ERROR EXCEPTION CHECK FOR WHAT THE NAMES ARE.

        query = "SELECT * FROM llmenergy WHERE model_name = %s;"
        cursor.execute(query, (model_name_entry,))
        corresponding_row = cursor.fetchall()
        return corresponding_row

    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None



def main():
    # Connect to the database
    connection = connect()

    # Execute a simple query: how many earthquakes above the specified magnitude are there in the data?
    results = get_top_n_column_values_SQL(connection, "model_parameters_billion", 5)
    
    if results is not None:
        print("Query results: ")
        for item in results:
            print(item)

    # Disconnect from database
    connection.close()

main()
