import pandas as pd
import numpy as np
import re



#Creating a function that will load the trade data
def load_data():
    """
    A function that loads trade data for individual US states'trade
    with Mexico and Canada. We want to return a dataframe (for use in pandas)
    """

    
    #Read each csv file into a pandas dataframe

    #Data taken from trade.gov (2024 Data)
    canada_exports = pd.read_csv("/Users/alexvertikov/Desktop/Personal-Projects/ECON_1500_Project/data/Cured-State-Canadian-Exports - State-Canadian-Exports.csv", encoding='cp1252')
    canada_imports = pd.read_csv("/Users/alexvertikov/Desktop/Personal-Projects/ECON_1500_Project/data/Cured-State-Canadian-Imports - State-Canadian-Imports.csv", encoding='cp1252')

    mexico_exports = pd.read_csv("/Users/alexvertikov/Desktop/Personal-Projects/ECON_1500_Project/data/Cured-State-Mexican-Exports - State-Mexican-Exports.csv", encoding='cp1252')
    mexico_imports = pd.read_csv("/Users/alexvertikov/Desktop/Personal-Projects/ECON_1500_Project/data/Cured-State-Mexican-Imports.csv", encoding='cp1252')

   # Filter to get just the rows for individual states (not UNITED STATES or Unallocated)
        # Filter for rows where Product is "0--All Merchandise" and exclude UNITED STATES and Unallocated
    state_exports_canada = canada_exports[
        (canada_exports['Product'] == '0--All Merchandise') & 
        (canada_exports['State'] != 'UNITED STATES') &
        (canada_exports['State'] != 'Unallocated')
    ]
    state_imports_canada = canada_imports[
        (canada_imports['Product'] == '0--All Merchandise') & 
        (canada_imports['State'] != 'UNITED STATES') &
        (canada_imports['State'] != 'Unallocated')
    ]
        
    state_exports_mexico = mexico_exports[
        (mexico_exports['Product'] == '0--All Merchandise') & 
        (mexico_exports['State'] != 'UNITED STATES') &
        (mexico_exports['State'] != 'Unallocated')
    ]
        
    state_imports_mexico = mexico_imports[
        (mexico_imports['Product'] == '0--All Merchandise') & 
        (mexico_imports['State'] != 'UNITED STATES') &
        (mexico_imports['State'] != 'Unallocated')
    ]

    # Create a base dataframe with state names
    all_data = pd.DataFrame({'State': state_exports_canada['State']})
        
    # Function to convert string values with $ to numbers
    def convert_to_number(value):
        if isinstance(value, str):
                # Remove $ and commas
            return float(re.sub(r'[,$]', '', value))
        return value
        
    # Add trade data as numeric values
    all_data['Canada Exports'] = state_exports_canada['2024'].apply(convert_to_number)
    all_data['Canada Imports'] = state_imports_canada['2024'].apply(convert_to_number)
    all_data['Mexico Exports'] = state_exports_mexico['2024'].apply(convert_to_number)
    all_data['Mexico Imports'] = state_imports_mexico['2024'].apply(convert_to_number)
        
    return all_data


    """
    #Now, create a dataframe with just the state name and Canada exports in 2024
    all_data = canada_exports[["State", "2024"]].copy()

    #Rename the column to be clear that we have 2024 Canada exports
    all_data.rename(columns={"2024":"Canada Exports"}, inplace = True)

    #Now add columns to the final dataframe with the rest of Mexico/Canada imports/exports
    all_data["Canada Imports"] = canada_imports["2024"]
    all_data["Mexico Exports"] = mexico_exports["2024"]
    all_data["Mexico Imports"] = mexico_imports["2024"]

    return all_data
    """

#A function that will calculate the balance of trade for each state with Mexico+Canada
def calculate_balance(df):
    """
    Using the values within the dataframe (Canada export/imports and Mexico exports/imports)
    calculate the balance of trade for each state with Mexico and Canada combined.
    We will have to call this function on our all_data df
    """

    #First, create an extra column which calculates the balance of trade with Canada and Mexico
    df["Canada Balance"] = df["Canada Exports"] - df["Canada Imports"]
    df["Mexico Balance"] = df["Mexico Exports"] - df["Mexico Imports"]


    #Create a third column that calculates total balance
    df["Total Balance"] = df["Mexico Balance"] + df["Canada Balance"]
       
    return df



def impact_calculator(df, rate):
    """"
    A function that intakes a tarriff rate and dataframe and uses a model
    (either Penn Model or my own) to calculate the proposed effect on imports and exports
    """

    if (rate == 0):
        #If the rate is 0, we assume nothing is changing (assume that there is currently 0% tarriff, 
        #as as the case for USMCA compliant goods)
        return df
    return df