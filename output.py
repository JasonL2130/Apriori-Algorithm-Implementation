# Collaboration Statement: Online Python Documentation for Functions & Libraries

import pandas as pd

def output_func(data, file_name):
    message = ''
    final_data = format_data(data)

    try:
            # tries to save WORKS 
        final_data.to_csv(file_name, sep=' ', index=False, header = False) # Saves File as TXT
            # Reads in Saved Above... Contains " " for some Words
        official_data = pd.read_csv(file_name)
            # Re-Saves the file as a .txt without " "
        official_data.to_csv(file_name, index=False)

        message = 'Success! File has been saved and outputted.'
    except:
        message = 'Failed! File has not been saved and outputted.'
    
    return message

# Formats the Data based on Guidlines in Instructions
def format_data(data):
    # Sorts Data in Descending Order
    sorted_data = data.sort_values(by=['Frequency'], ascending = False).reset_index(drop=True) 
    
    final_data = sorted_data # Dataframe that is use to be Formatted Properly

    # Format Frequency Values
    format_frequency = lambda freq: f'({freq})'
    final_data['Frequency'] = final_data['Frequency'].apply(format_frequency)

    # Format Itemset Values
    def format_itsemset(itemset):
        if isinstance(itemset, tuple):
            item_list = []
            for items in itemset:
                item_to_string = str(items)
                item_list.append(item_to_string)
                
            format_items = ' '.join(item_list).strip('"')
            return format_items
        else:
            return itemset

    final_data['Itemset'] = final_data['Itemset'].apply(format_itsemset)

    final_data['Itemset'] = final_data['Itemset'].str.replace('"', '') # Removes Quotes Issue I Was Experiencing

    return final_data