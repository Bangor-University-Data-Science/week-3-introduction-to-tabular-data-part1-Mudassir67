# def display_unique_values(df, categorical_features):
#     """
#     Displays unique values for each categorical feature in the DataFrame.
    
#     Args:
#         df (pd.DataFrame): The Titanic dataset as a DataFrame.
#         categorical_features (list): List of categorical feature names.
    
#     Returns:
#         dict: A dictionary where keys are feature names and values are the unique values.
#     """
#     pass  # Implement the logic here


# Import necessary modules
from data_loader import load_titanic_data
from feature_type_dict import create_feature_type_dict
import pandas as pd

def display_unique_values(df, categorical_features):
    """
    Displays unique values for each categorical feature in the DataFrame.
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        categorical_features (list): List of categorical feature names.
    Returns:
        dict: A dictionary where keys are feature names and values are the unique values.
    """
    unique_values = {}
    for feature in categorical_features:
        unique_values[feature] = df[feature].unique().tolist()
    return unique_values

if __name__ == "__main__":

    # df = load_titanic_data('data/titanic.csv')
    df = load_titanic_data()

    feature_types = create_feature_type_dict(df)

    categorical_features = feature_types['categorical']['nominal'] + feature_types['categorical']['ordinal']

    unique_values = display_unique_values(df, categorical_features)
    print("Unique Values for Categorical Columns:", unique_values)
