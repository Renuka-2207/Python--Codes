import os
import pandas as pd

# Function to read the specified Excel sheet from the main directory
def mainDirectoryAndFinalExcelSheet(mainDirectory, finalExcelSheet):
	# Construct the full path to the Excel file
	excelFilePath = os.path.join(mainDirectory, finalExcelSheet)
	# Read the Excel file into a DataFrame
	df = pd.read_excel(excelFilePath, sheet_name="Audit Issues")
	df.columns = [col.lower().strip()  for col in df.columns]
	return df
