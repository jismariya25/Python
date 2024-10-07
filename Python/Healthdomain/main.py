from data_preprocessing import load_data, clean_data
from eda import perform_eda
from machine_learning import train_model

def main():
    file_path = 'C:\\Users\\JOY AUGUSTINE\\OneDrive\\Documents\\Python\\Healthdomain\\Diabetes.csv'  # Update path if necessary
    data = load_data(file_path)  # This should match the load_data function definition
    cleaned_data = clean_data(data)
    perform_eda(cleaned_data)
    train_model(cleaned_data)

if __name__ == '__main__':
    main()
