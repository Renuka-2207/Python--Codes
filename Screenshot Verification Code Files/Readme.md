# Read Me

## 1. What the code does:

The provided code is a Python script designed to automate the process of verifying screenshot references in an Excel sheet against the actual screenshots stored in a specified folder directory. The script performs the following tasks:
- Reads input details from a text file, including paths, filenames, and column names.
- Validates user input to ensure necessary files and directories exist.
- Installs required Python modules if not already installed.
- Reads an Excel file containing the "Audit Issues" sheet.
- Matches the issue screenshots listed in the Excel sheet with actual screenshot files in the specified directory.
- The script creates a new Excel sheet with an additional column ('Screenshot Status') if no sheet with that column exists. If an Excel sheet with the 'Screenshot Status' column is already present from a previous run, the script updates the existing sheet with any new data.
- Generates a text file listing any extra screenshots found in the directory compared to those listed in the Excel sheet.

## 2. What all to install:

The script requires the installation of Python. If Python is not already installed on your system, you can download and install it from the official Python website: [Python.org](https://www.python.org).

Additionally, the script requires the following Python module:
- pandas

The script includes a function to automatically install the required Python module (pandas) if it is not already installed.

## 3. Dependencies:

The script relies on the following external libraries and modules:
- pandas: For data manipulation and analysis.
- os: For interacting with the operating system (e.g., file paths).
- subprocess: For executing shell commands to install Python modules.
- sys: For system-specific parameters and functions.

## 4. How to execute:

To execute the script, follow these steps:

A. Ensure Python is installed on your system.
B. Clone or download the script files to your local machine.
C. Open the 'Input_Details.txt' file located in the script project.
D. Provide the necessary input details following the format specified in the file. Ensure not to delete the ":-" delimiter used to separate user inputs from the script's queries. This delimiter is crucial for the script to correctly parse and interpret the input details provided by the user.
E. Save the changes to the 'Input_Details.txt' file.
F. Open a terminal or command prompt and navigate to the directory containing the script files.
G. Run the script by executing the command: `python main.py`

## 5. Known issues:

- None reported at this time.
