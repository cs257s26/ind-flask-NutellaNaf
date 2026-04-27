# README

Individual Flask project by Nafees Abdullah

Info in square brackets [] is info you must supply when navigating to the route! It will also detail the type.
Example: http://127.0.0.1:[int: PORT]/ requires you to input a port, which is an integer.

Valid columns in the csv (case sensitive):
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
Displays the top 5 row values in the specified column with their row number. Column must be within the CSV and the majority of its contents be integer values. If `column_of_interest` does not contain a majority of integer values or is not within the CSV, you will be redirected to the 404 page instead.

Columns WITHOUT integer values are:
- `Model name`
- `gpu_type`
- `data_center_region`

**Top *n* values in a column: http://127.0.0.1:[int: PORT]/[int: n]/[str: column_of_interest]**
Displays the top *n* row values in the specified column with their row number. Column must be within the CSV and contain majority integer-values. If `column_of_interest` does not contain a majority of integer values or is not within the CSV; or `n` is a value greater than the length of the CSV (28), you will be redirected to the 404 page instead.

Columns WITHOUT integer values are:
- `Model name`
- `gpu_type`
- `data_center_region`

**All values in a colum, unsorted: http://127.0.0.1:[int: PORT]/all/[str: column_of_interest]**
Displays all the unsorted values in a column and their row number. If `column_of_interest`is not within the CSV, you will be redirected to the 404 page instead.

**404 page: Anything that does not fit the paths above.**
Displays "This is not a valid page! Please review README.md for valid paths and usage."