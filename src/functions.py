from statsmodels.stats.diagnostic import linear_rainbow

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

