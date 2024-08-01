THIS CODE IS MY OWN WORK, IT WAS WRITTEN
WITHOUT CONSULTING CODE WRITTEN BY OTHER STUDENTS. Jason Lebov

Required Packages:
    - Pandas
    - Numpy
    - Combinations from Itertools
    - Argparse

    - Imports from some Files in SRC Code File [*ENSURE ALL CODE IS IN SAME LOCATION WHEN RUN*]

Files Explained:
    - main.py --> 
        - Location of Main Method & Method that Calls all Necessary Functions to perform Apriori
    - clean_data.py -->
        - Takes in the Data that is being Analyzed and One-Hot Encodes all Keywords in the 'text_keywords' feature
        - Returns the One-Hot Encoded DataFrame
    - apriori --> 
        - init_apriori()
            - Creates Final DataFrame that gets Populated with Itemsets & Thresholds
            - Iterates over all Necessary Functions Until Stop Condition is Met
        - create_c()
            - Creates All Possible Itemsets given 'Master Key' (Contains all Combinations of Items)
            - Finds Frequency of Each Itemset Combination
        - prune()
            - Takes the DataFrame created in create_c(), and Removes Any Rows with a Frequency < MinSupport
        - updateMaster()
            - Updates Master Key with all Possible Combinations of Items given the Previously Pruned Data
        - make_combos()
            - Given a List of all Item left in the Previously Pruned Data, Creates all Possible Combinations of those Items
            - Uses Combinations Function from Itertools
        - add_final()
            - Adds the Pruned DataFrames to the Final DataFrame that is eventually Returned as the 'Apriori Results'
        - checkFlag()
            - Checks the Data after each Iteration to determine when to Stop Running the Apriori Algorithm
    - output.py -->
        - Takes in the Final Apriori Output (Keywords & Frequencies) in a DataFrame
        - Orders Data in Descending Order based on Frequency
        - Formats Data based on Rules Outlined in Assignment
        - Converts & Outputs Dataframe to a .txt with the 'Name' Specified by the User when Starting the Program

How to Run my Code:
    - In the Command Line... Call the 'main.py' File w/ 3 Paramters (Input Data (str), Support Threshold (int), Output File Name (str))
                            python main.py _____ _____ _____

    Example Terminal Command: Ex1: python main.py 'data.csv' 500 'output.txt'
                              Ex2: python main.py 'data.csv' 900 'test.txt'
                              ExN: ... so on

                    DEFUALT Inputs = 'data.csv' 650 'output.txt' -------- *Defaults are used If 'main.py' is called without any command line parameters...if so, the 'Defaults' are used as the set parameters
                    
    **Important: Ensure that the Passed Data is in Same Location (Folder) as Code in src Folder or Proper Path for Data is Passed in Command Line** 

