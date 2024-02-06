import os
import pandas as pd

# Validation function for main directory
def validateMainDirectory(mainDirectory):
	if not os.path.exists(mainDirectory):
		print(f"Error: The specified path to excel sheet '{mainDirectory}' does not exist.")
		return False
	return True


# Validation function for final excel sheet
def validateFinalExcelSheet(mainDirectory, finalExcelSheet):
	excelFilePath = os.path.join(mainDirectory, finalExcelSheet + ".xlsx")
	if not os.path.isfile(excelFilePath):
		print(f"Error: The specified Excel sheet '{finalExcelSheet}' does not exist in the directory.")
		return False
	return True

# Validation function for page name column
def validateColumnNameForPageName(df, columnNameForPageName):
	if columnNameForPageName not in df.columns:
		print(f"Error: The column '{columnNameForPageName}' does not exist in the DataFrame.")
		return False
	return True

#Validation function for screenshots folder path 
def validateScreenshotFolderPath(screenshotsPath):
	if not os.path.exists(screenshotsPath):
		print(f"Error: The specified path to screenshot folder '{screenshotsPath}' does not exist.")
		return False
	return True


# Validation function for screenshot name column
def validateColumnNameForScreenshotName(df, columnNameForScreenshotName):
	if columnNameForScreenshotName not in df.columns:
		print(f"Error: The column '{columnNameForScreenshotName}' does not exist in the DataFrame.")
		return False
	return True
