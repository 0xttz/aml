import pandas as pd
import numpy as np

def transform_features(df):
    # Remove lng, lat, and index columns
    columns_to_drop = ['lng', 'lat', 'attr_index', 'rest_index']
    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])
    
    # Convert room_type to boolean (True if "Entire home/apt")
    df['entire_home'] = df['room_type'] == 'Entire home/apt'
    df = df.drop(columns=['room_type'])
    
    # Convert numeric columns to boolean
    bool_columns = ['multipleRooms', 'businessListing']
    df[bool_columns] = df[bool_columns].astype(bool)
    
    # Keep person_capacity and drop bedrooms as it's less relevant for pricing
    if 'bedrooms' in df.columns:
        df = df.drop(columns=['bedrooms'])
    
    # Add luxury flag
    df['is_luxury'] = df['price'] > 1000
    
    # Log transform price
    df['log_price'] = np.log1p(df['price'])
    
    return df

def main():
    # Load preprocessed dataset
    input_path = 'preprocessed_airbnb.csv'
    print(f"Loading data from {input_path}")
    df = pd.read_csv(input_path)
    
    print("Original columns:", df.columns.tolist())
    
    df = transform_features(df)
    print("\nColumns after transformation:", df.columns.tolist())
    
    # Print luxury properties summary
    print("\nLuxury properties summary:")
    print(f"Count: {df['is_luxury'].sum()}")
    print(f"Percentage: {(df['is_luxury'].mean() * 100):.2f}%")
    
    # Save final dataset
    output_path = 'final_airbnb.csv'
    df.to_csv(output_path, index=False)
    print(f"\nFinal dataset saved to: {output_path}")
    print(f"Final shape: {df.shape}")
    print("\nDataset preview:")
    print(df.head())

if __name__ == "__main__":
    main() 