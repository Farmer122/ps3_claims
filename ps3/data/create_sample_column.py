
import pandas as pd

def create_sample_column(df: pd.DataFrame, col1: str, percent : float) -> pd.DataFrame:
    """
    Here I will create a new column called "Sample" in the dataframe "df" based on the values in the column "col1".
    This column will be a random sample of the values in the column "col1" of the dataframe "df".
    The sample column should contain a sample with values "train" and "test" based on the percentage given in the argument "percent".
    """
    df['Sample'] = df[col1].sample(frac=percent, random_state=1).apply(lambda x: 'test' if x in df[col1].sample(frac=percent, random_state=1) else 'train')
    return df

        



