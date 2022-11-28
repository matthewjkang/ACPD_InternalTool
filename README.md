# ACPD Internal Tool 
## Tracker for finding Discrepancies between County WebPage and Quarterly Reports

My first week as an intern with the Alameda County Probation Department, I was tasked with tracking discrepancies between the goals listed on the website, 
https://probation.acgov.org/strategic-plan/goals-and-objectives.page
and goals listed on the quarterly reports. This clearly was going to take a lot of time, and my immediate reaction was to automate this using the BS4 and Pandas libraries in Python. 

The program can be split into three parts. 

#### Part 1 
Scrape the webpage, and extract its contents into an excel spreadshet. 

#### Part 2 
Aggregate all 4 quarterly reports into one excel spreadsheet. 

By now, you should have two spreadsheets. One with the contents of the website, and another with the contents of the quarterly reports. 

#### Part 3 
Algorithmically find discrepancies between the two. 
Create a Spreadsheet that shows all the tasks that are on the website, but not on the quarterly reports. (Or the wording has changed). 
Create a Spreadsheet that shows all the tasks that are on the quarterly reports, but not on the spreadsheet. (Or the wording has changed). 
Create a Spreadsheet that tracks all the tasks that have a mismatch in end date.  
Create a Spreadsheet that tracks all the tasks that have a mismatch in completion.


