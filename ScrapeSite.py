from bs4 import BeautifulSoup
import requests
import pandas as pd

# CREATE RESPONSE OBJECT
target_url = requests.get("https://probation.acgov.org/strategic-plan/goals-and-objectives.page")

# FEED RESPONSE OBJECT INTO BS4 HTML PARSER
soup = BeautifulSoup(target_url.content,'html.parser')

# CREATE DEPARTMENT LIST
departmentSoup = soup.findAll('div', attrs = {'division col-8 col-md-1 col-lg-1'}) 
department = []
for i in departmentSoup:
    if i.find("abbr"):
        department.append(i.find("abbr").text)

# CREATE TASK LIST
taskSoup = soup.findAll('div',attrs = {'class':"task col-12 col-md-4 col-lg-5"} ) 
tasks = [x.text for x in taskSoup if x.text != "Task"]

# CREATE START_DATE LIST
# CREATE END_DATE LIST
dateSoup = soup.findAll('div', attrs = {'class':"date col-8 col-md-1 col-lg-1"}) 
dates = []
for i in dateSoup:
    if i.text not in ('Start Date','End Date'):
        dates.append(i.text.strip()[3:])
start = dates[::2]
end = dates[1::2]

# CREATE COMPLETION % LIST
completionSoup = soup.findAll('div', attrs = {'class':"percentage col-12"} )
completion = []
for i in completionSoup:
    if i.text:
        completion.append(i.text)
    else:
        completion.append('0%')

# CREATE OVERALL STATUS LIST
statusSoup = soup.findAll('div', attrs = {'class':"all-status col-7 col-md-2 col-lg-2"} )
status = [x.text for x in statusSoup]

# CREATE PANDAS DATAFRAME
web = pd.DataFrame(
    {
        'DEPT' : department,
        'TASK' : tasks,
        'START' : start,
        'END' : end,
        'COMPLETION' : completion,
        'STATUS' : status
    }
)

# Export it as an Excel Sheet
# web.to_excel('WebsiteContents.xlsx',index=False)