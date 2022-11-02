from AggregateReports import agg
from ScrapeSite import web

col_web = [i[0:20] for i in web['TASK']]
col_agg = [i[0:20] for i in agg['TASK']]

onWeb_notOnReports = []
for i in col_web:
    if i not in col_agg:
        onWeb_notOnReports.append(i)

print(onWeb_notOnReports)

onRep_NotOnWeb = []
for i in col_agg:
    if i not in col_web:
        onRep_NotOnWeb.append(i)

print(onRep_NotOnWeb)

