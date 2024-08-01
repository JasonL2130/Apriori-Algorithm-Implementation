# Collaboration Statement: Online Python Documentation for Functions & Libraries

import pandas as pd

    # Function to Clean and One-Hot Encode the Data
def clean_data(data):
    dummy_data = data['text_keywords'].str.get_dummies(sep = ';') # One Hot Encodoes Data so Each Keyword is it's own Column
    return dummy_data