import os
import pandas as pd

from Library import Find_Path
from Library import Match_Screenshot

# Function to update the DataFrame with screenshot status and save it to a new Excel file
def updatingDFAndCreatingNewExcelSheet(df, mainDirectory, columnName):
    # Iterate over unique page names in the DataFrame
    for pageName in df[columnName].str.strip().str.lower().unique():
        # Filter rows for the current page name
        pageRows = df[df[columnName].str.strip().str.lower() == pageName]
        # Find the path for the current page name by calling findPath... function.
        issueScreenshotPath = Find_Path.findPathForTheValueOfPageNameColumn(pageRows, mainDirectory,columnName)
        # Check for matching files in the issue screenshot path with those in the DataFrame 
        #By calling matchingScreenshot... function
        screenshotStatus = Match_Screenshot.matchingFilesInIssueScreenshotPathWithIssueScreenshot(pageRows, issueScreenshotPath)

        df.loc[pageRows.index, "Screenshot status"] = screenshotStatus

    # Specify the path for the new Excel file with the added column
    newExcelFilePath = os.path.join(r"D:\sandhya\TekVision\Sample", "Reports", "Screenshot_verification.xlsx")
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

