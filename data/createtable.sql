DROP TABLE IF EXISTS llmenergy;
CREATE TABLE llmenergy (
  model_name text PRIMARY KEY,
  model_parameters_billion int,
  training_tokens_billion int,
  num_gpus bigint,
  training_hours float,
  hardware_power_draw_watts_per_gpu real,
  carbon_intensity_gco2_per_kwh real,
  total_energy_kwh bigint,
  total_carbon_footprint_kgco2e bigint
);