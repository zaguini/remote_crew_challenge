import pandas as pd
import os

class DataETL:

    @staticmethod
    def aggregate_reports():
        # Define the path to your folder containing the Excel files
        path = f'{os.getcwd()}\\technical_challenge_solution\\ExcelFiles\\'

        # Initialize an empty DataFrame
        all_data = pd.DataFrame()

        # Loop through each file and concatenate them into the DataFrame
        for file in os.listdir(path):
            df = pd.read_excel(path+file)
            all_data = pd.concat([all_data, df], ignore_index=True)
        all_data = all_data.rename(columns={all_data.columns[0]:'Geographic Area'})
        return all_data
    
    @staticmethod
    def save_report(all_data):
        # Save the combined DataFrame to a new Excel file (optional)
        os.makedirs(f'{os.getcwd()}\\technical_challenge_solution\\AgregatedData')
        all_data.to_excel(f'{os.getcwd()}\\technical_challenge_solution\\AgregatedData\\combined_data.xlsx', index=False)
