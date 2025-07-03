import string
import pandas as pd
def clean_strings(strings):
    strings = strings.str.strip()
    strings = strings.str.lower()
    for i in range(len(string.punctuation)):
        strings = strings.str.replace(string.punctuation[i], '')
    strings = strings.dropna()
    return strings
assert clean_strings(pd.Series(["      ChaRLI!$)E"]))[0] == "charlie"