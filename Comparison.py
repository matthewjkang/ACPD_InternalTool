from AggregateReport import agg
from ScrapeSite import web
import pandas as pd
import os
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

aggFlat = agg.values.tolist()
webFlat = web.values.tolist()

for i in webFlat:
    temp = i[0]+" "+i[1]
    i.pop(0)
    i.pop(0)
    i.insert(0,temp)

for i in aggFlat:
    temp = i[2]+" "+i[3]
    i.pop(2)
    i.pop(2)
    i.insert(2,temp)

aggdf = pd.DataFrame(aggFlat, columns = ['GOAL','OBJ','ID', 'START','END','COMPLETION','STATUS'])
webdf = pd.DataFrame(webFlat, columns = ['ID', 'START','END','COMPLETION','STATUS'])

web2aggDf = pd.merge(webdf,aggdf,on='ID',suffixes=(' (Website)', ' (Reports)'), how='left')
naDF = web2aggDf[web2aggDf['GOAL'].isna()]
naDF.to_excel(os.path.join('Sheets', 'OnWebsiteButNotOnReportsOrWordingChange.xlsx'),index=False)

agg2webDf = pd.merge(aggdf,webdf,on='ID',suffixes=(' (Reports)', ' (Website)'), how='left')
aggNaDF = agg2webDf[agg2webDf['START (Website)'].isna()]
aggNaDF.to_excel(os.path.join('Sheets', 'OnReportsButNotOnWebsiteOrWordingChange.xlsx'),index=False)

finaldf = agg2webDf.dropna()

endMismatch = finaldf[finaldf['END (Reports)'] != finaldf['END (Website)']]
endMismatch.to_excel(os.path.join('Sheets', 'EndDateMismatch.xlsx'),index=False)


completionMismatch = finaldf[finaldf['COMPLETION (Website)'] != finaldf['COMPLETION (Reports)']]
completionMismatch.to_excel(os.path.join('Sheets', 'CompletionMismatch.xlsx'),index=False)