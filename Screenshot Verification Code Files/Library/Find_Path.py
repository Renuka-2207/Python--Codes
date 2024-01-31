import os

# Function to find the path for the value of the 'Page Name' column in the DataFrame
def findPathForTheValueOfPageNameColumn(df, mainDirectory, columnName):
    # Construct the folder path for screenshots
    screenshotFolderPath = os.path.join(mainDirectory, "Screenshots")
    issueScreenshotPath = None  # Initialize with a default value
    # Iterate over unique page names in the DataFrame
    for pageName in df[columnName].str.strip().str.lower().unique():
        # Construct the full path to the page's folder within the screenshots folder
        pageFolderPath = os.path.join(screenshotFolderPath, pageName)
        # Check if the folder for the page exists
        if os.path.exists(pageFolderPath):
            issueScreenshotPath = pageFolderPath
            break  # Exit loop once page folder is found
        else:
            # If the folder doesn't exist, search within subdirectories
            listOfDirectoriesInScreenshotFolder = os.listdir(screenshotFolderPath)
            # Iterate over each directory within the screenshots folder
            for subdir in listOfDirectoriesInScreenshotFolder:
                # Construct the full path to the page's folder within a subdirectory
                subFolderPath = os.path.join(screenshotFolderPath, subdir, pageName)
                # Check if the page folder exists within the subdirectory
                if os.path.exists(subFolderPath):
                    issueScreenshotPath = subFolderPath
                    break  # Exit loop once page folder is found

            # Check if issueScreenshotPath is still None after searching subdirectories
            if issueScreenshotPath is None:
                print(f"Alert!: No path found for page '{pageName}'.")
    return issueScreenshotPath

