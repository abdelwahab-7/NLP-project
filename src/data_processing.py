# src/data_processing.py
import os

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
    
    # List to store combined data
    combined_data = []
    
    # Process CSV and TSV files
    for file in os.listdir(raw_data_path):
        if file.endswith((".csv", ".tsv")):
            file_path = os.path.join(raw_data_path, file)
            print(f"Processing raw data file: {file}")
            
            # Read the file (basic line-by-line reading)
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    combined_data.append(line.strip())
    
    # Save combined data to a single processed file
    if combined_data:
        output_file = os.path.join(processed_data_path, "processed_data.txt")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("\n".join(combined_data))
        print(f"Saved processed data to {output_file}")
    else:
        print("No data to process.")

if __name__ == "__main__":
    print("Running data processing...")
    load_and_process_data()