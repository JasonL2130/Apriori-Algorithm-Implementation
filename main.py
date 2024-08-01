# Collaboration Statement: Online Python Documentation for Functions & Libraries

import pandas as pd
import argparse
from clean_data import clean_data
from apriori import init_apriori
from output import output_func

    # Calls All Functions to Run Apriori
def run_apriori(dataset, threshold, output_file): 
    print('Running Apriori Algorithm...')
    apriori_data = clean_data(dataset)
    apriori_results = init_apriori(apriori_data, threshold)
    return_message = output_func(apriori_results, output_file)
    return return_message 

def main():                                       
    ##### COMMAND LINE PARSER ##### 
    command_line_parser = argparse.ArgumentParser()
    command_line_parser.add_argument("dataset", nargs='?', help="input datasert", default='data.csv', type=str)
    command_line_parser.add_argument("minsupport", nargs='?', help="input minsupport threshold", default=650, type=int) 
    command_line_parser.add_argument("output_file", nargs='?', help="input outpt file name", default = 'output.txt', type=str)

        # Parses Command Line Inputs Accordingly
    inputs = command_line_parser.parse_args()
    input_dataset = pd.read_csv(inputs.dataset)
    input_threshold = inputs.minsupport
    input_output_name = inputs.output_file

    print(run_apriori(input_dataset, input_threshold, input_output_name)) # Calls Function

if __name__ == '__main__':
    main()
    