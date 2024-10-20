import pandas as pd

<<<<<<< HEAD
# def load_titanic_data(filepath: str) -> pd.DataFrame:
#     """
#     Loads the Titanic dataset from the specified file path.
    
#     Args:
#         filepath (str): Path to the Titanic CSV file.
  
     
#     Returns:
#         pd.DataFrame: Loaded Titanic dataset as a DataFrame.
#     """
#     pass  # Implement the loading logic here

def load_titanic_data(filepath: str = 'data/titanic.csv') -> pd.DataFrame:
    """Loads the Titanic dataset from the specified file path."""
    return pd.read_csv(filepath)
=======
def load_titanic_data(filepath: str) -> pd.DataFrame:
    """
    Loads the Titanic dataset from the specified file path.
    
    Args:
        filepath (str): Path to the Titanic CSV file.
    
    Returns:
        pd.DataFrame: Loaded Titanic dataset as a DataFrame.
    """
    pass  # Implement the loading logic here
>>>>>>> d3a31da53e73eba24f10da5de69923894313537e
