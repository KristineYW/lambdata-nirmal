from my_lambdata.my_mod import enlarge
from my_lambdata.my_mod1 import checks
import pandas as pd
import numpy as np


print("Hello")

print(enlarge(10))


df = pd.DataFrame(
            {"a": [4, 5, 6],
            "b": [7, 8, np.NaN],
            "c": [9, np.NaN, 11]})


print(df)

checks(df)
# new_col(df)

print(df)
