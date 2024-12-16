# Execute this script from the project's root directory

import pandas as pd

# Retrieve the datasets
smh_data = pd.read_csv("data/smh_ref_micro_merged.csv")
smh_hum_temp = pd.read_csv("data/smh_23-24_humidity_temp.csv")

# Set datetime type to the date column
for df in [smh_data, smh_hum_temp]:
    df["date"] = pd.to_datetime(df["date"])
    df["date"] = df["date"].dt.tz_localize(None)
    # Set datetime column as index
    df.set_index("date", inplace=True, drop=True)


# Build seasonality categorical variables

# Adapt pandas index type
smh_data_datetime_idx = smh_data.index.to_period("h")

# Create columns indicating day and month
smh_data["hourofday"] = smh_data_datetime_idx.hour
smh_data["monthofyear"] = smh_data_datetime_idx.month

# Define a mapping of months to seasons
month_to_season = {
    12: "Winter",
    1: "Winter",
    2: "Winter",
    3: "Spring",
    4: "Spring",
    5: "Spring",
    6: "Summer",
    7: "Summer",
    8: "Summer",
    9: "Autumn",
    10: "Autumn",
    11: "Autumn",
}

# Add a "season" column based on the mapping
smh_data["season"] = smh_data["monthofyear"].map(month_to_season)


# Rename the variables
# valeur_x stands for the reference station's measures, y for the microsensor's
smh_data.rename(
    columns={"valeur_x": "reference_pm25", "valeur_y": "microsensor_pm25"}, inplace=True
)
# valeur_x stands for the temperature measures, y for the humidity
smh_hum_temp.rename(
    columns={"valeur_x": "temperature", "valeur_y": "humidity"}, inplace=True
)

# Drop the undesired columns
smh_data = smh_data.loc[
    :, ["reference_pm25", "microsensor_pm25", "hourofday", "monthofyear", "season"]
]
smh_hum_temp = smh_hum_temp.loc[:, ["temperature", "humidity"]]

# Reorder columns
smh_data = smh_data.loc[
    :, [col for col in smh_data.columns if col != "reference_pm25"] + ["reference_pm25"]
]

# Merge the two datasets
smh_merge = pd.merge(
    smh_data, smh_hum_temp, left_index=True, right_index=True
)  # inner join

# Save dataset
smh_merge.to_csv("data/smh_23-24_training_set.csv")
