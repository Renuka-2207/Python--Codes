import os 
import pandas as pd

from Library import Find_Path
from Library import Match_Screenshot

# Function to update the DataFrame with screenshot status and save it to a new Excel file
def updatingDFAndCreatingNewExcelSheet(df, mainDirectory, columnNameForPageName, screenshotsPath, columnNameForScreenshotName):
	# Specify the path for the text file
	txtFilePath = os.path.join(mainDirectory, "Extra_Screenshots.txt")
	# Open the text file in write mode
	with open(txtFilePath, 'w') as txtFile:
		# Iterate over unique page names in the DataFrame
		for pageName in df[columnNameForPageName].str.strip().str.lower().unique():
			# Filter rows for the current page name
			pageRows = df[df[columnNameForPageName].str.strip().str.lower() == pageName]
			# Find the path for the current page name by calling findPath... function.
			issueScreenshotPath = Find_Path.findPathForTheValueOfPageNameColumn(pageRows, mainDirectory, columnNameForPageName, screenshotsPath)
			# Check for matching files in the issue screenshot path with those in the DataFrame 
			# By calling matchingScreenshot... function
			screenshotStatus = Match_Screenshot.matchingFilesInIssueScreenshotPathWithIssueScreenshot(pageRows, issueScreenshotPath, columnNameForScreenshotName)

			df.loc[pageRows.index, "Screenshot status"] = screenshotStatus
			
			# Get the list of screenshots present in the directory for this page
			screenshotsInDirectory = [os.path.splitext(f)[0].lower() for f in os.listdir(issueScreenshotPath) if f.lower().endswith('.png')]

			# Get the list of screenshots mentioned in the DataFrame for this page
			screenshotsInDF = pageRows[columnNameForScreenshotName].str.strip().str.lower().tolist()
			
			# Calculate extra screenshots
			extraScreenshots = [screenshot for screenshot in screenshotsInDirectory if screenshot not in screenshotsInDF]

			# Write extra screenshots to the text file
			if extraScreenshots:
				txtFile.write(f"Page Name: {pageName}, Extra Screenshots Count: {len(extraScreenshots)} \n")
				for screenshot in extraScreenshots:
					txtFile.write(f"\t{screenshot}\n")  
			# Print the count of extra screenshots for this page
			print(f"Page Name: {pageName}, Extra Screenshots Count: {len(extraScreenshots)}")

	print("Extra_Screenshots text file is created")
 
	# Specify the path for the new Excel file with the added columns
	newExcelFilePath = os.path.join(mainDirectory, "Screenshot_verification.xlsx")
	# Check if the file exists
	if os.path.exists(newExcelFilePath):
		# If the file exists, load it, update with the new DataFrame, and save it back
		existing_df = pd.read_excel(newExcelFilePath)
		existing_df.update(df)
		existing_df.to_excel(newExcelFilePath, index=False)
		print(f"Existing 'Screenshot_verification.xlsx' file updated.")
	else:
		# If the file doesn't exist, save the DataFrame to a new file
		df.to_excel(newExcelFilePath, sheet_name="Audit Issues", index=False)
		print(f"New 'Screenshot_verification.xlsx' file created.")  
