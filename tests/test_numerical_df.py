from titanic_analysis.numerical_df import get_numerical_df
<<<<<<< HEAD

def test_get_numerical_df():
    # Mock a DataFrame
    mock_df = {
        'Age': [22, 38, 26, 35],
        'Fare': [7.25, 71.83, 7.92, 53.10],
        'Survived': [0, 1, 1, 0]
    }
=======
import pandas as pd
def test_get_numerical_df():
    # Mock a DataFrame
    mock_df = pd.DataFrame(data={
        'Age': [22, 38, 26, 35],
        'Fare': [7.25, 71.83, 7.92, 53.10],
        'Survived': [0, 1, 1, 0]
    })
>>>>>>> d3a31da53e73eba24f10da5de69923894313537e
    numerical_features = ['Age', 'Fare']
    
    numerical_df = get_numerical_df(mock_df, numerical_features)
    
    assert not numerical_df.empty, "Numerical DataFrame should not be empty"
    assert all(col in numerical_df.columns for col in numerical_features), "All numerical features should be present"
