# TASK :Create a function which receive a pandas dataframe.

# You will filter (using loc() or query()) in order to have all Index == 'A'.

# You will return the result.
import pandas as pd
def my_pandas_journey_filtering(df):
    return df.query('Index == "A"')