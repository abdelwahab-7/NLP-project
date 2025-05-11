import os
import random
import pandas as pd

def load_and_process_data():
    raw_data_path = "../data/raw/full_dataset/"
    processed_data_path = "../data/processed/"
    
    # Check if raw data folder exists
    if not os.path.exists(raw_data_path):
        print("Raw data folder not found!")
        return
    
    # Create processed folder if it doesn't exist
    if not os.path.exists(processed_data_path):
        os.makedirs(processed_data_path)
        print("Created processed data folder.")
    
    # Define the input file
    input_file = "goemotions_1.csv"
    input_path = os.path.join(raw_data_path, input_file)
    
    # Check if the input file exists
    if not os.path.exists(input_path):
        print(f"File {input_file} not found in raw data!")
        return
    
    print(f"Processing {input_file}...")
    
    # Read the CSV file using pandas
    df = pd.read_csv(input_path)
    
    # Shuffle the data
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Calculate split sizes
    total_rows = len(df)
    train_size = int(total_rows * 0.8)  # 80% for train
    test_size = total_rows - train_size  # 20% for test
    
    # Split the data
    train_df = df[:train_size]
    test_df = df[train_size:]
    
    # Define output paths
    train_output_path = os.path.join(processed_data_path, "train.csv")
    test_output_path = os.path.join(processed_data_path, "test.csv")
    
    # Save the splits as CSV files
    train_df.to_csv(train_output_path, index=False)
    test_df.to_csv(test_output_path, index=False)
    
    print(f"Saved {train_size} rows to {train_output_path}")
    print(f"Saved {test_size} rows to {test_output_path}")

if __name__ == "__main__":
    print("Running data processing...")
    load_and_process_data()