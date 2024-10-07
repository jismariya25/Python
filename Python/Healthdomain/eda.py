import seaborn as sns
import matplotlib.pyplot as plt

def perform_eda(data):
    """
    Perform Exploratory Data Analysis (EDA) on the cleaned dataset.
    """
    print(data.head())
    print(data.describe())
    print("Missing values:\n", data.isnull().sum())

    # Update this line to use 'Diabetes_012' instead of 'Outcome'
    sns.histplot(data['Diabetes_012'], kde=True)
    plt.title('Distribution of Diabetes Outcome')
    plt.xlabel('Diabetes Outcome (0 = No, 1 = Yes)')
    plt.ylabel('Frequency')
    plt.show()

    # Add any additional EDA visualizations or analyses you need here
