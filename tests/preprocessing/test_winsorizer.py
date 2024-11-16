import numpy as np
import pytest

from ps3.preprocessing import Winsorizer

# TODO: Test your implementation of a simple Winsorizer

@pytest.mark.parametrize(
    "lower_quantile, upper_quantile", [(0, 1), (0.05, 0.95), (0.5, 0.5)]
)
def test_winsorizer(lower_quantile, upper_quantile):

    X = np.random.normal(0, 1, 1000)

    #Instantiate winsorizer as Winsorizer class we build in the _winsorizer.py

    winsorizer = Winsorizer(lower_quantile=lower_quantile, upper_quantile=upper_quantile)

    #fit method
    winsorizer.fit(X)

    #Transform method

    X_transformed = winsorizer.transform(X)

    #Calculate lower/upper quantiles and check no values are below/above

    lower_bound = np.quantile(X, lower_quantile)
    upper_bound = np.quantile(X, upper_quantile)
    
    assert np.all(X_transformed >= lower_bound), f"Values below lower quantile {lower_bound} found!"
    assert np.all(X_transformed <= upper_bound), f"Values above upper quantile {upper_bound} found!" 
