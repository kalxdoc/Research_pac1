import pandas as pd
import sys

def load_data(filepath):
    """
    Load data from a CSV file into a pandas DataFrame.
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: DataFrame containing the loaded data
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Successfully loaded data from {filepath}")
        print(f"Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading file: {e}")
        sys.exit(1)


def display_data_info(df):
    """
    Display basic information about the DataFrame.
    
    Args:
        df (pd.DataFrame): The DataFrame to analyze
    """
    print("\n--- Data Info ---")
    print(df.info())
    print("\n--- First Few Rows ---")
    print(df.head())
    print("\n--- Basic Statistics ---")
    print(df.describe())


def process_data(df):
    """
    Process the DataFrame (example processing).
    
    Args:
        df (pd.DataFrame): The DataFrame to process
        
    Returns:
        pd.DataFrame: Processed DataFrame
    """
    # Remove rows with missing values
    df_clean = df.dropna()
    print(f"\nRemoved rows with missing values. New shape: {df_clean.shape}")
    return df_clean


def save_data(df, output_filepath):
    """
    Save the processed DataFrame to a CSV file.
    
    Args:
        df (pd.DataFrame): The DataFrame to save
        output_filepath (str): Path for the output CSV file
    """
    try:
        df.to_csv(output_filepath, index=False)
        print(f"Data successfully saved to {output_filepath}")
    except Exception as e:
        print(f"Error saving file: {e}")
        sys.exit(1)


def main():
    """
    Main function to orchestrate the data processing workflow.
    """
    if len(sys.argv) < 2:
        print("Usage: python data_processor.py <input_file.csv> [output_file.csv]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "output.csv"
    
    # Load data
    df = load_data(input_file)
    
    # Display information
    display_data_info(df)
    
    # Process data
    df_processed = process_data(df)
    
    # Save processed data
    save_data(df_processed, output_file)
    
    print("\n--- Processing Complete ---")


if __name__ == "__main__":
    main()