# Execute this script from the project's root directory

import pandas as pd

# Retrieve the dataset
smh_data = pd.read_csv("data/smh_ref_micro_merged.csv")

# Set datetime type to the date column
smh_data["date"] = pd.to_datetime(smh_data["date"])
smh_data["date"] = smh_data["date"].dt.tz_localize(None)

# Set datetime column as index
smh_data.set_index("date", inplace=True, drop=True)

# Adapt pandas index type
smh_data.index = smh_data.index.to_period("h")

# Create columns indicating day and month
smh_data["hourofday"] = smh_data.index.hour
smh_data["monthofyear"] = smh_data.index.month

# Define a mapping of months to seasons
month_to_season = {
    12: "Winter", 1: "Winter", 2: "Winter",
    3: "Spring", 4: "Spring", 5: "Spring",
    6: "Summer", 7: "Summer", 8: "Summer",
    9: "Autumn", 10: "Autumn", 11: "Autumn",
}

# Add a "season" column based on the mapping
smh_data["season"] = smh_data["monthofyear"].map(month_to_season)

# Rename the variables
# valeur_x stands for the reference station's measures, y for the microsensor's
smh_data.rename(columns={"valeur_x": "reference_pm25", "valeur_y": "microsensor_pm25"}, inplace=True)

# Drop the undesired columns
smh_data = smh_data.loc[:, ["reference_pm25", "microsensor_pm25", "hourofday", "monthofyear", "season"]]

# Reorder columns
smh_data = smh_data.loc[:, [col for col in smh_data.columns if col != "reference_pm25"] + ["reference_pm25"]]

# Save dataset
smh_data.to_csv("data/smh_2023_training_set.csv")