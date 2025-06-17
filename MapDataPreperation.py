all_states = [
    'Andaman & Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam',
    'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra & Nagar Haveli & Daman & Diu',
    'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir',
    'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh',
    'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha',
    'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana',
    'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'
]
import pandas as pd

# Load your dataset
df = pd.read_csv("TopPerformingStates_MapData.csv")

# Convert to title case and handle special corrections
df['State'] = df['State'].str.replace('-', ' ').str.title()

# Special cases (GeoJSON uses '&' instead of 'And', and other exact names)
replace_map = {
    "Andaman & Nicobar Islands": "Andaman & Nicobar Islands",
    "Dadra & Nagar Haveli & Daman & Diu": "Dadra & Nagar Haveli & Daman & Diu",
    "Jammu & Kashmir": "Jammu & Kashmir"
}

# Apply final name correction
df['State'] = df['State'].replace(replace_map)

# All official states/UTs as per GeoJSON
all_states_set = set(all_states)

# States already present
existing_states_set = set(df['State'])

# Find missing ones
missing_states = all_states_set - existing_states_set

# Create dataframe for missing ones
missing_df = pd.DataFrame({
    'State': list(missing_states),
    'total_transaction_count': 0,
    'total_transaction_amount': 0
})

# Append to main df
full_df = pd.concat([df, missing_df], ignore_index=True)

# Sort alphabetically
full_df = full_df.sort_values(by='State').reset_index(drop=True)

# Save to new CSV
full_df.to_csv("TopPerformingStates_UC1_Completed.csv", index=False)
