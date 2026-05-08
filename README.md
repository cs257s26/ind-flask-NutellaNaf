# README

## Reflection on the process
1. I wanted to store information that is easy to graph while also being meaningful to both researchers and a casual observer.Thus, I removed any non-numeric columns other than `model_name`, which serves as the primary key (since each model's performance is unique to it). Additionally, I removed the `pue` (power usage effectiveness) column as its result is very dependent on the infrastructure that runs it -- and so, in my eyes, its awkward to present it as a point of comparison without further context. A similar argument could be made for `hardware_power_draw_watts_per_gpu`; however, GPU information is available on the original dataset, which provides the needed context to understand this information.

2. **get_top_n_column_values_SQL()** fulfills the user need to grab the top N values in a column; thus allowing a researcher or user to view, for instance, the top 5 models by the total amount of energy it took to train it.

**get_row_by_model_name_SQL()** fulfills the user need to grab the values in a row by the model name. This allows a researcher to grab all the statistical information related to a model, which is useful for researchers and general users if they are interested in a particular model.

**get_whole_column_SQL()** fulfills the user need to grab all the values in a column, enabling them to get a sense of the range of values in a column. In the case of `model_name`, this allows a user to see all the models within this dataset.

**fetch_column_names()** and **fetch_data_length()** are helper functions and are not meant to be directly accessed by users; thus they do not fulfill user stories (see more about them in the `datasource.py` file!)

## SQL
Please set up the database with the following psql cmd:
`\copy llmenergy FROM 'llmenergy.csv' DELIMITER ',' NULL 'NULL' CSV`

Valid columns in the SQL table (and csv file) (case sensitive):
- `model_name` (non-numeric)
- `model_parameters_billion`
- `training_tokens_billion`
- `num_gpus`
- `training_hours`
- `hardware_power_draw_watts_per_gpu`
- `carbon_intensity_gco2_per_kwh`
- `total_energy_kwh`
- `total_carbon_footprint_kgco2e`

<ins>Flask paths below are not guaranteed to work, given I am unable to debug them on stearns (cannot figure out how to open the local link from the stearns instance)</ins>

## FLASK
Individual Flask project by Nafees Abdullah

Info in square brackets [] is info you must supply when navigating to the route! It will also detail the type.
Example: http://127.0.0.1:[int: PORT]/ requires you to input a port, which is an integer.

Valid columns in the csv (case sensitive) **NOTE: THESE ARE OUTDATED AND LEFT IN FOR ARCHIVAL PURPOSES. PLEASE REFER TO [SQL](#sql) ABOVE TO SEE VALID COLUMNS.**:
- `Model name`
- `model_parameters_billion`
- `training_tokens_billion`
- `gpu_type`
- `num_gpus`
- `training_hours`
- `data_center_region`
- `PUE`
- `hardware_power_draw_watts_per_gpu`
- `carbon_intensity_gco2_per_kwh`
- `total_energy_kwh`
- `total_carbon_footprint_kgco2e`

**Home route: http://127.0.0.1:[int: PORT]/**
Displays the text "Please look at the README.md to learn what routes to go to!"

**Top 5 values in a column: http://127.0.0.1:[int: PORT]/[str: column_of_interest]**
Displays the top 5 row values in the specified column with their row number. Column must be within the CSV and the majority of its contents be numeric values. If `column_of_interest` does not contain a majority of numeric values or is not within the CSV, you will be redirected to the 404 page instead.

Columns WITHOUT numeric values are:
- `Model name`
- `gpu_type` (depreciated -- no longer exists in my version)
- `data_center_region` (depreciated -- no longer exists in my version)

**Top *n* values in a column: http://127.0.0.1:[int: PORT]/[int: n]/[str: column_of_interest]**
Displays the top *n* row values in the specified column with their row number. Column must be within the CSV and contain majority numeric-values. If `column_of_interest` does not contain a majority of numeric values or is not within the CSV; or `n` is a value greater than the length of the CSV (28), you will be redirected to the 404 page instead.

Columns WITHOUT numeric values are:
- `Model name`
- `gpu_type` (depreciated -- no longer exists in my version)
- `data_center_region` (depreciated -- no longer exists in my version)

**All values in a colum, unsorted: http://127.0.0.1:[int: PORT]/all/[str: column_of_interest]**
Displays all the unsorted values in a column and their row number. If `column_of_interest`is not within the CSV, you will be redirected to the 404 page instead.

**Values by row, unsorted: http://127.0.0.1:[int: PORT]/models/[str: model_name]**
Displays the row based on a given model name. If `model_name`is not within the CSV, you will be redirected to the 404 page instead.

**404 page: Anything that does not fit the paths above.**
Displays "This is not a valid page! Please review README.md for valid paths and usage."