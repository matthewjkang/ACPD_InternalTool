import os
from openpyxl import load_workbook
import pandas as pd 
import re

reports_list =  os.listdir(".\ReportsQ4")
reports_list = ["ReportsQ4"+os.sep+x for x in reports_list]

adm_path = reports_list[0]
afs_path = reports_list[1]
jfac_path = reports_list[2]
jfs_path = reports_list[3]
 
def create_excel(path): # This function will create a pandas dataframe from an excel spreadsheet.
    # INPUT : File path to a spreadsheet
    # OUTPUT : Pandas dataframe containing key information extracted from spreadsheet.

    sh = load_workbook(path, data_only = True).active

    real_rows = []
    for i in sh['B']:
        if type(i.value) == int:
            real_rows.append(1)
        else:
            real_rows.append(0)

    # ITERATE THROUGH A NUMERICAL RANGE AND APPEND INTO YOUR LIST IF THE ROW IS VALID
    tasks = []
    start = []
    end = []
    status = []
    completion = [] # This will initially hold a tuple w/ 4 values. 
    for i in range(len(real_rows)):
        if real_rows[i]:

            single_task = sh['D'][i].value
            tasks.append(single_task)

            start_date = sh['F'][i].value
            start.append(start_date)

            end_date = sh['G'][i].value
            end.append(end_date)

            quarters = (
                sh['H'][i].fill.start_color.index, # Hex color of the 25% box
                sh['I'][i].fill.start_color.index, # Hex color of the 50% box
                sh['J'][i].fill.start_color.index, # Hex color of the 75% box
                sh['K'][i].fill.start_color.index) # Hex color of the 100% box
            completion.append(quarters)

            stat = sh['L'][i].value
            status.append(stat)

    completion = [str(i.count('FF0070C0')*25)+"%" for i in completion] #Here, we are turning the completion tuple into a string, representing percentage

    # EXTRACT THE ACTUAL START DATE FROM THE LIST OF PREVIOUS AND CURRENT START DATES
    temp = []
    for i in start:
        splitstring = i.split()
        if splitstring[-1].isdigit():
            mon_year = " ".join(splitstring[-2:])
            temp.append(mon_year)
        else:
            temp.append(splitstring[-1])
    start = temp

    # EXTRACT THE ACTUAL END DATE FROM THE LIST OF PREVIOUS AND CURRENT END DATES
    temp = []
    for i in end:
        splitstring = i.split()
        if splitstring[-1].isdigit():
            mon_year = " ".join(splitstring[-2:])
            temp.append(mon_year)
        else:
            temp.append(splitstring[-1])
    end = temp

    # CREATE YOUR DATAFRAME
        # Create a regex expression that matches name of the excel spreadsheet.
        # Used to create the DEPT column of the dataframe
    match = re.search(r'.*?\\(.*)\..*', path).group(1) # Match any substring that is between "\" and "."

    df = pd.DataFrame(
        {
            'DEPT':[match]*len(tasks),
            'TASK':tasks,
            'START':start,
            'END':end,
            'COMPLETION' : completion,
            'STATUS':status
        }
    )
    return df

adm = create_excel(adm_path)
afs = create_excel(afs_path)
jfs = create_excel(jfs_path)
jfac = create_excel(jfac_path)

# Merge all 4 into one
agg = pd.concat([adm,afs,jfac,jfs],ignore_index=True)

# Create Excel Spreadsheet
agg.to_excel('AggregatedReports.xlsx', index=False)