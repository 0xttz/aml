import pandas as pd

def rename_columns(df):
    column_mapping = {
        'Unnamed: 0': 'id',
        'realSum': 'price',
        'multi': 'multipleRooms',
        'biz': 'businessListing',
        'dist': 'city_dist'
    }
    df = df.rename(columns=column_mapping)
    return df

def clean_columns(df):
    columns_to_drop = ['id', 'attr_index_norm', 'rest_index_norm']
    df = df.drop(columns=columns_to_drop)
    return df

def main():
    # Load merged dataset
    input_path = 'merged_airbnb.csv'
    print(f"Loading data from {input_path}")
    df = pd.read_csv(input_path)
    
    # Apply transformations
    print("Original columns:", df.columns.tolist())
    
    df = rename_columns(df)
    print("\nColumns after renaming:", df.columns.tolist())
    
    df = clean_columns(df)
    print("\nColumns after cleaning:", df.columns.tolist())
    
    # Save preprocessed dataset
    output_path = 'preprocessed_airbnb.csv'
    df.to_csv(output_path, index=False)
    print(f"\nPreprocessed dataset saved to: {output_path}")
    print(f"Final shape: {df.shape}")

if __name__ == "__main__":
    main()
