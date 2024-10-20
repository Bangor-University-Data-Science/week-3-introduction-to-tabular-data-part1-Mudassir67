#  def create_feature_type_dict(df):
    # """
    # Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    
    # Args:
    #     df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    # Returns:
    #     dict: A dictionary classifying features into numerical and categorical types.
    # """
    # feature_types = {
    #     'numerical': {
    #         'continuous': [],  # Fill with continuous numerical features
    #         'discrete': []  # Fill with discrete numerical features
    #     },
    #     'categorical': {
    #         'nominal': [],  # Fill with nominal categorical features
    #         'ordinal': []  # Fill with ordinal categorical features
    #     }
    # }
    # return feature_types


def create_feature_type_dict(df):
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    """
    feature_types = {
        'numerical': {
            'continuous': ['Age', 'Fare'],  
            'discrete': ['SibSp', 'Parch']  
        },
        'categorical': {
            'nominal': ['Sex', 'Embarked'], 
            'ordinal': ['Pclass']           
        }
    }
    return feature_types