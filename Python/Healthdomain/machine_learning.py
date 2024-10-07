import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

def train_model(data):
    """
    Train a machine learning model on the dataset.
    """
    # Replace 'Diabetes_012' with the correct outcome column name if needed
    outcome_column = 'Diabetes_012'  # Adjust this if needed

    # Prepare the features and target variable
    X = data.drop(columns=[outcome_column])  # Drop the target column from features
    y = data[outcome_column]  # Target variable

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Random Forest model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    print("Model Evaluation:")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))
