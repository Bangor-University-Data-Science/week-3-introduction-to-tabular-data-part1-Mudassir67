# def get_numerical_df(df, numerical_features):
#     """
#     Creates a DataFrame containing only numerical features.
    
#     Args:
#         df (pd.DataFrame): The Titanic dataset as a DataFrame.
#         numerical_features (list): List of numerical feature names.
    
#     Returns:
#         pd.DataFrame: DataFrame containing only numerical features.
#     """
#     pass  # Implement the logic here


from data_loader import load_titanic_data
from feature_type_dict import create_feature_type_dict
df = load_titanic_data()


feature_types = create_feature_type_dict(df)


numerical_features = feature_types['numerical']['continuous'] + feature_types['numerical']['discrete']
numerical_df = df[numerical_features]

print(numerical_df)