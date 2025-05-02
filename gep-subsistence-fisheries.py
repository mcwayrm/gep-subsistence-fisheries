"""
This script cleans the constructed data from Lynch et al. (2024). 
The paper can be found at: https://hull-repository.worktribe.com/preview/4748071/Lynch%20et%20al%202024_Nat_Food.pdf
The data can be found at: https://www.sciencebase.gov/catalog/item/644ae0e0d34e45f6ddccf773
What we want at the end is a TCUV for each country. This is a cross-section of national value. 
"""
# Depenendencies
import os
import pandas as pd

# Loads in the data
def load_data(path: str):
    try:
        data = pd.read_excel(path, engine='openpyxl')
        return data
    except FileNotFoundError:
        print(f"File not found at {path}. Please check the path and try again.")
    except pd.errors.EmptyDataError:
        print(f"The file at {path} is empty. Please provide a valid CSV file.")
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")

# Cleans the data 
def clean_data(data: pd.DataFrame):
    """
    Only keep the TCUV for each country.
    """
    # Keep only the TCUV column
    data = data[["admin", "TCUV"]]
    # Collapse data to keep only the first TCUV for each admin
    data = data.drop_duplicates(subset=["admin"], keep="first")
    # Return clean data
    return data

# Saves the data as a gep csv file
def save_data(data: pd.DataFrame, path: str):
    try:
        data.to_csv(path, index=False)
        print(f"Data saved successfully at {path}.")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

# Run main function
def run():
    """
    Runs the main function to load, clean, and save the data.
    """
    # 1. Load data 
    df_raw = load_data("Rec fish food_20230509_for USGS data release.xlsx")
    # 2. Clean data 
    df_clean = clean_data(df_raw)
    # 3. Save data 
    save_data(df_clean, "gep-subsistence-fisheries.csv")

# Run 
if __name__ == "__main__":
    run()