import os

# Function to check if the files in the issue screenshot path match with those in the DataFrame
def matchingFilesInIssueScreenshotPathWithIssueScreenshot(df, issueScreenshotPath):
    # Get a list of file names (without extension) in the issue screenshot path
    filesInIssueScreenshotPath = [os.path.splitext(f.lower().strip())[0] for f in os.listdir(issueScreenshotPath) if f.lower().endswith('.png')]

    # Extract the 'Issue Screenshot' column from the DataFrame, normalize it, and check if any matches exist
    issueScreenshot = df['Issue Screenshot'].str.lower().str.strip()
    return issueScreenshot.isin(filesInIssueScreenshotPath).map({True: 'Yes', False: 'No'})

