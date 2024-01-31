from Library import Read_Excel
from Library import Update_New_Excel


def main():
    mainDirectory = r"D:\sandhya\TekVision\Sample"
    finalExcelSheet = "OneGoalGraduation_Accessibility_report_01-24-2024.xlsx"
    columnName = "Page Name"

    df = Read_Excel.mainDirectoryAndFinalExcelSheet(mainDirectory, finalExcelSheet)
    Update_New_Excel.updatingDFAndCreatingNewExcelSheet(df, mainDirectory, columnName)

if __name__ == "__main__":
    main()
