import pandas as pd
from titanic_analysis.data_loader import load_titanic_data

def test_load_titanic_data():
<<<<<<< HEAD
    df = load_titanic_data("data/titanic.csv")
=======
    df = load_titanic_data("../../data/titanic.csv")
>>>>>>> d3a31da53e73eba24f10da5de69923894313537e
    assert isinstance(df, pd.DataFrame), "The returned object should be a DataFrame"
    assert not df.empty, "The DataFrame should not be empty"
