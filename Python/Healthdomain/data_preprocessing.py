import pandas as pd

def load_data(file_path):
    """
    Load the diabetes dataset from a CSV file.
    """
    try:
        data = pd.read_csv(file_path)
        print("Dataset loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def clean_data(data):
    """
    Clean the dataset by removing duplicates and handling missing values.
    """
    # Remove duplicates
    data = data.drop_duplicates()
    
    # Handle missing values (for example, drop them)
    data = data.dropna()
    
    print("Data cleaned successfully.")
    return data
