import os
import pandas as pd

from Library import Install_Required_Python_Modules
from Library import Read_Excel
from Library import Validate_User_Input
from Library import Update_New_Excel

def readInputDetails(filePath):
	details = {}
	try:
		with open(filePath, 'r') as file:
			for line in file:
				# Split each line into key-value pairs using ':-' as delimiter
				parts = line.strip().split(':-')
				if len(parts) == 2:
					key = parts[0].strip()
					value = parts[1].strip()
					# Ensure that key and value are not empty
					if key and value:
						details[key] = value
					else:
						print("Warning: Empty key or value found in input file.")
				else:
					print(f"Error: Invalid line format in input file: '{line.strip()}'")
	except FileNotFoundError:
		print(f"Error: Input details file '{filePath}' not found.")
	except Exception as e:
		print(f"Error while reading input file: {e}")
	
	return details


def main():
	inputFilePath = "Input_Details.txt"

	# Check if the input details file exists
	if not os.path.exists(inputFilePath):
		print(f"Error: Input details file '{inputFilePath}' not found.")
		return  # Program exits here

	# Read input details from file
	details = readInputDetails(inputFilePath)

	mainDirectory = details.get("Path where excel sheet stored").strip('"').strip()
	finalExcelSheet = details.get("Name of final excel sheet (Without extension)").strip()
	columnNameForPageName = details.get("Column name for page/component name").lower().strip()
	columnNameForScreenshotName = details.get("Column name for screenshot name").lower().strip()
	screenshotsPath = details.get("path where screenshots folder located").strip('"')

	# Validate user inputs
	if not Validate_User_Input.validateMainDirectory(mainDirectory):
		print("Exiting program.")
		return
	if not Validate_User_Input.validateFinalExcelSheet(mainDirectory, finalExcelSheet):
		print("Exiting program.")
		return
	if not Validate_User_Input.validateScreenshotFolderPath(screenshotsPath):
		print("Exiting program.")
		return

	# Calling the functions
	Install_Required_Python_Modules.installingRequiredPythonModules()
	df = Read_Excel.mainDirectoryAndFinalExcelSheet(mainDirectory, finalExcelSheet)

	# Validate the column names after df is assigned
	if not Validate_User_Input.validateColumnNameForPageName(df, columnNameForPageName):
		print("Exiting program.")
		return

	if not Validate_User_Input.validateColumnNameForScreenshotName(df, columnNameForScreenshotName):
		print("Exiting program.")
		return

	# Call function to update new Excel
	Update_New_Excel.updatingDFAndCreatingNewExcelSheet(df, mainDirectory, columnNameForPageName, screenshotsPath, columnNameForScreenshotName)

if __name__ == "__main__":
	main()
