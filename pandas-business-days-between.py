import pandas as pd

#read data from an excel tab
xlsx = pd.ExcelFile('path_to_file.xlsx')
df = pd.read_excel(xlsx, 'sheetname')

#drop first 2 rows
df.columns = df.iloc[1]
df = df.reindex(df.index.drop(0))
df = df.reindex(df.index.drop(1))
df.head()

reps = ["insert","reps","here"]
execs = ["insert","excecs","here"]

#create a dataframe from the excel sheet dataframe with these headers
sales = df[["Start Date","End Date","Sales Rep"]]
sales = sales.dropna()
import datetime

#rename headers
sales = sales.rename(columns={'Start Date': 'start',
                               'End Date': 'end',
                              'Sales Rep': 'rep'})
                              
#convert to datetime                              
sales['start'] = pd.to_datetime(sales['start'])
sales['end'] = pd.to_datetime(sales['end'])

#set start and end dates
start_date = "2018-07-01"
end_date = "2019-07-31"
mask = (sales['start'] >= start_date) & (sales['start'] <= end_date)
sales = sales.loc[mask]

#create a year month column
sales['YearMonth'] = sales['start'].map(lambda x: 100*x.year + x.month)

#find business day count between a and b
#set it to be new column called days
import numpy as np
a = sales['start'].values.astype('datetime64[D]')
b = sales['end'].values.astype('datetime64[D]')
sales['days'] = np.busday_count(a,b)

