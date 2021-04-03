# global variables

import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols
from statsmodels.stats.diagnostic import linear_rainbow, het_breuschpagan
from statsmodels.stats.outliers_influence import variance_inflation_factor

def create_formula(target_name, df):
    """Returns a formula string.
    
    Args:
        target_name: A string containing the target feature.
        df: A data frame.
    Returns:
        A string containing an ols model formula.
        """
    features = df.drop(target_name, axis=1).columns
    features = "+".join(features)
    return target_name + "~" + features

def rainbow(model_results):
    """Returns the statistic and p-value of a rainbow test.
    
    Agrs:
        model_results: an ols model object.
    Returns:
        A printout containing the statistic and p-value of a rainbow test.
    """
    rainbow_statistic, rainbow_p_value = linear_rainbow(model_results)
    print("Rainbow statistic:", rainbow_statistic)
    print("Rainbow p-value:", rainbow_p_value)

