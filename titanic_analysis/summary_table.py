# def create_summary_table(df):
#     """
#     Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
#     Args:
#         df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
#     Returns:
#         pd.DataFrame: A summary DataFrame.
#     """
#     pass  # Implement the logic here

import pandas as pd
from data_loader import load_titanic_data
def create_summary_table(df):
    """
    Creates a summary DataFrame with columns such as Feature Name, Data Type,
    Number of Unique Values, and Has Missing Values?.
    Args:
        df (pd.DataFrame): The DataFrame to summarize.
    Returns:
        pd.DataFrame: A DataFrame that summarizes the input DataFrame.
    """
    summary = pd.DataFrame({
        "Feature Name": df.columns,
        "Data Type": df.dtypes,
        "Number of Unique Values": df.nunique(),
        "Has Missing Values?": df.isnull().any()
    })
    return summary


if __name__ == "__main__":


    # df = load_titanic_data('data/titanic.csv')  
    df = load_titanic_data()
    summary_df = create_summary_table(df)
    print(summary_df)
