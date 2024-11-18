import pandas as pd
import numpy as np

def create_sample_split(df: pd.DataFrame, id_column: str, training_frac=0.8):
    """Create sample split based on ID column.

    Parameters
    ----------
    df : pd.DataFrame
        Training data
    id_column : str
        Name of ID column
    training_frac : float, optional
        Fraction to use for training, by default 0.8

    Returns
    -------
    pd.DataFrame
        Training data with sample column containing train/test split based on IDs.
    """
    unique_ids = df[id_column].unique()
    print("Unique IDs:", unique_ids)  # Debug print
    np.random.shuffle(unique_ids)
    split_index = int(training_frac * len(unique_ids))
    train_ids = set(unique_ids[:split_index])
    print("Train IDs:", train_ids)  # Debug print
    df['sample'] = df[id_column].apply(lambda x: 'train' if x in train_ids else 'test')
    print(df.head())  # Debug print to show the updated DataFrame
    return df
