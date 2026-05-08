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

# def top_n_column_values(column_of_interest: str, n: int):
#     """ 
#     Display the top n models in a given column.

#     This function only works with columns that have numerical values. 
#     If the column given is strictly non-numerical values, user is prompted to select a different column.

#     Args:
#         column_of_interest: A string representing the column name

#     Returns:
#         column_data: List[Tuple(2)] A list of tuples with the top 5 values in that column. 
#         The first element of the tuple has the value, the second element is the row number.

#     Raises:
#         ValueError: A non-numerical column was input OR n 
#     """

#     # Ensure the column is a valid, non-numerical column (assuming it is one in the set)
#     if ((column_of_interest == "Model name") | (column_of_interest == "gpu_type") | (column_of_interest == "data_center_region")):
#         print("FAIL AT FIRST COND")
#         raise ValueError("Input a non-numerical column.")
    
#     column_data = fetch_column_data(column_of_interest)
    
#     # Ensure data is loaded + handle case where column is not in csv.
#     if (n > len(data)-1):
#         print("FAIL AT SECOND COND")
#         raise ValueError("Input a number less than the total length of the row")

#     # Fetching the column data, because this isn't SQL so I have to do it manually, and sorting.
#     sorted_column_data = []

#     for tuple in column_data:
#         try:
#             sorted_column_data.append((float(tuple[0]), tuple[1]))
#         except ValueError:
#             sorted_column_data.append((-999,tuple[1]))

#     sorted_column_data = sorted(sorted_column_data, key=lambda x: (float(x[0])),reverse=True)
#     # print([sorted_column_data[i] for i in range(len(sorted_column_data)) if i < n])
#     return [sorted_column_data[i] for i in range(len(sorted_column_data)) if i < n]


def get_max_temp_over_threshold(connection, temp: float) -> list:
    """Retrieves all dates (and all the weather information associated with those dates) where the high temperature was above a specified threshold.

    Args:
        connection (psycopg2.connection) - the connection to the database
        temp (float) - the minimum high temperature

    Returns:
        list - a list of all dates where the high temperature is greater or equal to temp, or None if the query fails.
    """
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM weather_small WHERE max_temp>%s ORDER BY max_temp DESC;"
        cursor.execute(query, (temp,))
        return cursor.fetchall()

    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None


def top_n_column_values_SQL(connection, column_of_interest: str, n: int) -> list:
    """ 
    Display the top n models in a given column.

    This function only works with columns that have numerical values. 
    If the column given is strictly non-numerical values, user is prompted to select a different column.

    Args:
        column_of_interest: A string representing the column name

    Returns:
        column_data: List[Tuple(2)] A list of tuples with the top 5 values in that column. 
        The first element of the tuple has the value, the second element is the row number.

    Raises:
        ValueError: A non-numerical column was input OR n is greater than the length-1 of the column.
    """
    try:
        cursor = connection.cursor()
        query = "SELECT model_name, %s FROM llmenergy ORDER BY %s DESC LIMIT %s;"
        cursor.execute(query, (column_of_interest, column_of_interest, n))
        return cursor.fetchall()

    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None



def main():
    # Connect to the database
    connection = connect()

    # Execute a simple query: how many earthquakes above the specified magnitude are there in the data?
    results = top_n_column_values_SQL(connection, "model_parameters_billion", 5)
    
    if results is not None:
        print("Query results: ")
        for item in results:
            print(item)

    # Disconnect from database
    connection.close()

main()
