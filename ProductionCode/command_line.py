import argparse
import sys
import csv

data = []
FILENAME = "./data/llmenergy.csv"

def load_data():
   """Loads in data from a CSV file and stores it in `data`"""
   if len(data) == 0:
       with open(FILENAME, newline='') as datafile:
           csv_file = csv.reader(datafile)
           for row in csv_file:
               data.append(row)

def nafees_user_story(column_of_interest: str):
    """ 
    Display the top 5 models in a given column.

    This function only works with columns that have numerical values. 
    If the column given is strictly non-numerical values, user is prompted to select a different column.

    Args:
        column_of_interest: A string representing the column name

    Returns:
        column_data: List[Tuple(2)] A list of tuples with the top 5 values in that column. 
        The first element of the tuple has the value, the second element is the row number.

    Raises:
        ValueError: A non-numerical column was input
    """
    top_5 = top_n_column_values(column_of_interest, 5)
    return top_5

def top_n_column_values(column_of_interest: str, n: int):
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
        ValueError: A non-numerical column was input OR n 
    """

    # Ensure the column is a valid, non-numerical column (assuming it is one in the set)
    if ((column_of_interest == "Model name") | (column_of_interest == "gpu_type") | (column_of_interest == "data_center_region")):
        print("FAIL AT FIRST COND")
        raise ValueError("Input a non-numerical column.")
    
    column_data = fetch_column_data(column_of_interest)
    
    # Ensure data is loaded + handle case where column is not in csv.
    if (n > len(data)-1):
        print("FAIL AT SECOND COND")
        raise ValueError("Input a number less than the total length of the row")

    # Fetching the column data, because this isn't SQL so I have to do it manually, and sorting.
    sorted_column_data = []

    for tuple in column_data:
        try:
            sorted_column_data.append((float(tuple[0]), tuple[1]))
        except ValueError:
            sorted_column_data.append((-999,tuple[1]))

    sorted_column_data = sorted(sorted_column_data, key=lambda x: (float(x[0])),reverse=True)
    # print([sorted_column_data[i] for i in range(len(sorted_column_data)) if i < n])
    return [sorted_column_data[i] for i in range(len(sorted_column_data)) if i < n]

def fetch_column_data(column_of_interest: str):
    """ 
    Fetch the data in a given column.

    Args:
        column_of_interest: A string representing the column name

    Returns:
        column_data: List[Tuple(2)] A list of tuples, representing each element in the column. 
        The first element of the tuple has the value, the second element is the row number.

    Raises:
        ValueError: A non-numerical column was input.
    """

    # Ensure the column is a valid, non-numerical column (assuming it is one in the set)
    # if ((column_of_interest == "Model name") | (column_of_interest == "gpu_type") | (column_of_interest == "data_center_region")):
    #     raise ValueError("Input a non-numerical column.")
    
    # Ensure data is loaded + handle case where column is not in csv.
    if len(data) == 0:
        load_data()
    try:
        index = data[0].index(column_of_interest)
    except ValueError:
        raise ValueError("Input a valid column within the csv.")

    # Fetching the column data, because this isn't SQL so I have to do it manually, and sorting.
    column_data = []
    for i in range(1, len(data)):
        # try:
            column_data.append((data[i][index],i))
        # except ValueError:
        #     column_data.append((-999,i))

    # column_data = sorted(column_data, key=lambda x: (float(x[0])),reverse=True)
    return column_data

def may_user_story():
    """
    Analyzes energy consumption by region.
    
    Args:
        region_column: Name of the region column (default: "data_center_region")
    """
    if len(data) == 0:
        load_data()
    try:
        region_index = data[0].index("data_center_region")
        energy_index = data[0].index("total_energy_kwh")
    except:
        print("Error")
        return
    region_energy = {}
    for row in data[1:]:
        region = row[region_index].strip()
        if not region:
            continue
        energy_str = row[energy_index].strip()
        if not energy_str:
            continue
        try:
            energy = float(energy_str)
        except ValueError:
            continue
        if region not in region_energy:
            region_energy[region] = []
        region_energy[region].append(energy)
    results = []
    for region, energies in region_energy.items():
        total = sum(energies)
        average = total / len(energies)
        results.append({'region': region,'total_energies': total,'average_energies': average,})
    results.sort(key=lambda x: x['total_energies'], reverse=True)
    print("Energy Consumption by Data Center Region")
    print(f"{'Region':<30} {'Total Energy (kWh)':<20} {'Average Energy (kWh)':<18} ")
    for r in results:
        print(f"{r['region']:<30} {r['total_energies']:>18,.0f}   {r['average_energies']:>16,.0f}") 

        
def becca_user_story(LLMName: str):
    'Returns the number of model parameters for a specified LLM name'
    if len(data) == 0:
        load_data()

    name_col_num = 0
    param_col_num = 1
    name_col = []
    param_col = []

    for i in range(len(data)): 
        name_col.append(data[i][name_col_num])
        param_col.append(data[i][param_col_num])
        if (name_col[i] == LLMName): 
            return param_col[i]
        
    raise ValueError("LLM name invalid.")

def main():
    load_data()

    parser = argparse.ArgumentParser(
        usage= "Type first initial in lowercase of team member who wrote a user story to access their assigned user story",
        description="CLI API for our second deliverable"
    )

    parser.add_argument("user_story", action='store', default="n", help="access team member's user story")
    parser.add_argument("input", action='store', default="n", help="state required argument")
    parser.add_argument("in2", action='store', default="5", help="state required argument")

    args = parser.parse_args()

    match args.user_story:
        case "b":
            becca_user_story(args.input)
        case "n":
            nafees_user_story(args.input)
        case "m":
            may_user_story()
        case "2":
            print(top_n_column_values(args.input, int(args.in2)))
        case _:
            parser.print_help()

if __name__ == "__main__":
    main()