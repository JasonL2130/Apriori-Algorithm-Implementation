# Collaboration Statement: Online Python Documentation for Functions & Libraries

import pandas as pd
from itertools import combinations

# Overall Apriori Function that Runs Needed # Times
def init_apriori(dataset, threshold):
    apriori_results_df = pd.DataFrame(columns = ['Itemset', 'Frequency'])  # Data to Store all Frequent Itemsets
    minsupport = threshold
    data = dataset
   
    master_list = list(data.columns) # Master Key of Keywords

    flag = True
    counter = 1 # Initializes Counter to Know Itemset Length
    while flag != False:         
        temp_data = create_c(master_list, data, counter) # Creates Full Itemset Lists
        pruned_data = prune(temp_data, minsupport) # Prunes Itemset Lists for Values above Threshold
        apriori_results_df = add_final(apriori_results_df, pruned_data) # Adds Pruned Data to Final DF
        counter += 1
        master_list = updateMaster(pruned_data, counter) # Updates Master List for all Items that can used in Next Run of Algorithm
        flag = checkFlag(pruned_data, minsupport, master_list) # Checks if Algorithm is Done

    return apriori_results_df.reset_index(drop=True)


######################

    # Creates Full Itemset Lists    
def create_c(master_key, data, count):
    temp_df = pd.DataFrame(columns = ['Itemset', 'Frequency']) # Temporary DF that is Filled w/ this Itemset's Values
    if count == 1:
        temp_df = pd.DataFrame(columns = ['Itemset', 'Frequency'])
        for item in master_key:
            set_values = {'Itemset': item, 'Frequency': data[item].sum()}
            temp_df.loc[len(temp_df)] = set_values
        
        return temp_df
    else:
        for item in master_key: 
            cols = list(item)
            condition = data[cols].all(axis=1) == 1
            filtered_data = data[condition == True]
            total = len(filtered_data)
            set_values = {'Itemset': item, 'Frequency': total}
            temp_df.loc[len(temp_df)] = set_values

        return temp_df

    # Prune Function: Finds L's --> Final (Pruned) Frequency Lists
def prune(data, threshold):
    prune = lambda frequency: frequency['Frequency'] >= threshold
    pruned_df = data[data.apply(prune, axis=1)].reset_index(drop=True)
    return pruned_df

    # Updates Master List for all Items that can used in Next Run of Algorithm
def updateMaster(data, counter): # Data is Previously Pruned 
    if counter < 2:
        values = list(data['Itemset'])
    else:
        values_start = data["Itemset"].explode()
        values = set(values_start.tolist())

    new_master = make_combos(values, counter)
    new_master_return = list(new_master)

    return new_master_return

    # Makes Combinations of Itemsets to Update MasterKey
def make_combos(list, length):
    values = combinations(list, length)
    return values

    # Adds Pruned Data to Final DF
def add_final(final_df, new_values):
    final_df = pd.concat([final_df, new_values])
    return final_df

    # Stopping Criteria for Apriori Algorithm
def checkFlag(data, threshold, master):
    flag = True
    if ((data['Frequency'] >= threshold).any() == False or data.empty or len(master) == 0):
        flag = False
    return flag

