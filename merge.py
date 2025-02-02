import pandas as pd
import os

# Set data directory
data_dir = '/Users/lenna/Desktop/aml/data-pre/csv'

# Initialize empty list to store dataframes
dfs = []

# List of cities
cities = ['amsterdam', 'athens', 'barcelona', 'berlin', 'budapest', 
          'lisbon', 'london', 'paris', 'rome', 'vienna']

# Process each city
for city in cities:
    for period in ['weekdays', 'weekends']:
        file_path = os.path.join(data_dir, f"{city}_{period}.csv")
        print(f"Trying to read: {file_path}")
        
        try:
            if os.path.exists(file_path):
                df = pd.read_csv(file_path)
                df['city'] = city
                df['time_period'] = period
                dfs.append(df)
                print(f"Successfully read {file_path}")
            else:
                print(f"Could not find file: {file_path}")
        except Exception as e:
            print(f"Error reading {file_path}: {str(e)}")

if not dfs:
    raise ValueError("No CSV files were successfully read. Check if the files are in the directory: " + data_dir)

# Merge all dataframes
merged_df = pd.concat(dfs, ignore_index=True)

# Save merged dataset
output_path = 'merged_airbnb.csv'
merged_df.to_csv(output_path, index=False)

print(f"\nMerged dataset saved to: {output_path}")
print(f"Total number of records: {len(merged_df)}")
print("\nDataset columns:")
print(merged_df.columns.tolist())
print("\nDataset preview:")
print(merged_df.head())