import os
import random

def load_and_process_data():
    raw_data_path = "../data/raw/"
    processed_data_path = "../data/processed/"
    
    # Check if raw data folder exists
    if not os.path.exists(raw_data_path):
        print("Raw data folder not found!")
        return
    
    # Create processed folder if it doesn't exist
    if not os.path.exists(processed_data_path):
        os.makedirs(processed_data_path)
        print("Created processed data folder.")
    
    # Define files to process
    data_files = {
        "train.tsv": "train.tsv",
        "dev.tsv": "dev.tsv",
        "test.tsv": "test.tsv"
    }
    
    # Sampling percentage (e.g., 10%)
    sample_percentage = 0.1
    
    # Process each file
    for input_file, output_file in data_files.items():
        input_path = os.path.join(raw_data_path, input_file)
        output_path = os.path.join(processed_data_path, output_file)
        
        if not os.path.exists(input_path):
            print(f"File {input_file} not found in raw data!")
            continue
        
        print(f"Processing {input_file}...")
        
        # Read all lines
        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Skip header if present (assuming first line is header)
        if lines:
            header = lines[0]
            data_lines = lines[1:]
        else:
            print(f"No data in {input_file}!")
            continue
        
        # Sample a subset of the data
        sample_size = max(1, int(len(data_lines) * sample_percentage))
        sampled_lines = random.sample(data_lines, sample_size)
        
        # Save sampled data as TSV (preserve tabs)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(header.strip() + "\n")
            for line in sampled_lines:
                f.write(line.strip() + "\n")
        
        print(f"Saved {sample_size} sampled rows to {output_path}")

if __name__ == "__main__":
    print("Running data processing...")
    load_and_process_data()
