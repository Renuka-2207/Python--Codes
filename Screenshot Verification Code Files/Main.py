import os
import pandas as pd
from Library.Read_Input_Details import readInputDetails
from Library import Install_Required_Python_Modules
from Library import Read_Excel
from Library import Validate_User_Input
from Library import Update_New_Excel

def main():
	inputFilePath = "Input_Details.txt"

	# Check if the input details file exists
	if not os.path.exists(inputFilePath):
		print(f"Error: Input details file '{inputFilePath}' not found.")
		return  # Program exits here

	# Read input details from file
	details = readInputDetails(inputFilePath)

	# Check if any key is missing
	requiredKeys = [
		"Path where excel sheet stored",
		"Name of final excel sheet (With extension)",
		"Column name for page/component name",
		"Column name for screenshot name",
		"path where screenshots folder located"
	]

	for key in requiredKeys:
		if key not in details:
			print(f"Missing key '{key}' in input file.")
			print("Exiting program.")
			return

	# Check for missing values
	missingValues = [key for key, value in details.items() if not value]
	if missingValues:
		for key in missingValues:
			print(f"Missing value for key '{key}' in input file.")
		print("Exiting program.")
		return

	mainDirectory = details.get("Path where excel sheet stored").strip('"').strip()
	finalExcelSheet = details.get("Name of final excel sheet (With extension)").strip()
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
