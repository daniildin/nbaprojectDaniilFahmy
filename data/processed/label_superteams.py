import pandas as pd

# Load your merged dataset
df = pd.read_csv('Merged_Financial_And_Performance_Data.csv')

# Initialize Superteam column as 0
df['Superteam'] = 0

# Define the superteam list
superteams = [
    {'Team_standardized': 'Boston Celtics', 'Start': 2007, 'End': 2012},
    {'Team_standardized': 'Miami Heat', 'Start': 2010, 'End': 2014},
    {'Team_standardized': 'Cleveland Cavaliers', 'Start': 2014, 'End': 2017},
    {'Team_standardized': 'Golden State Warriors', 'Start': 2016, 'End': 2019},
    {'Team_standardized': 'Los Angeles Lakers', 'Start': 2003, 'End': 2004},
    {'Team_standardized': 'Los Angeles Lakers', 'Start': 2012, 'End': 2013},
    {'Team_standardized': 'Brooklyn Nets', 'Start': 2013, 'End': 2014},
    {'Team_standardized': 'Oklahoma City Thunder', 'Start': 2017, 'End': 2018},
    {'Team_standardized': 'Brooklyn Nets', 'Start': 2021, 'End': 2022},
    {'Team_standardized': 'Los Angeles Lakers', 'Start': 2021, 'End': 2023},
    {'Team_standardized': 'Los Angeles Clippers', 'Start': 2023, 'End': 2024},
    {'Team_standardized': 'Phoenix Suns', 'Start': 2023, 'End': 2025}
]

# Apply superteam labels as 1
for team in superteams:
    mask = (
        (df['Team_standardized'] == team['Team_standardized']) &
        (df['SeasonStartYear'] >= team['Start']) &
        (df['SeasonStartYear'] <= team['End'])
    )
    df.loc[mask, 'Superteam'] = 1

# Save the labeled data
df.to_csv('merged_data_with_superteams.csv', index=False)

print("✅ Superteam labels added as 0/1 and saved to 'merged_data_with_superteams.csv'")
