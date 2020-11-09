#load in a dataframe, do conditional formatting, autofit columns
import pandas as pd

# Create a Pandas Excel writer using XlsxWriter as the engine.

writer = pd.ExcelWriter('example.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Get the xlsxwriter objects from the dataframe writer object.
workbook  = writer.book
worksheet = writer.sheets['Sheet1']


for i, width in enumerate(get_col_widths(filtered)):
    worksheet.set_column(i, i, width)
    
    
# Light red fill with dark red text.
format1 = workbook.add_format({'bg_color':   '#FFC7CE',
                               'font_color': '#9C0006'})

# Light yellow fill with dark yellow text.
format2 = workbook.add_format({'bg_color':   '#FFEB9C',
                               'font_color': '#9C6500'})

# Green fill with dark green text.
format3 = workbook.add_format({'bg_color':   '#C6EFCE',
                               'font_color': '#006100'})

#GREEN between 21 and 30
worksheet.conditional_format('R2:R'+str(len(filtered)), {'type':     'cell',
                                       'criteria': 'between',
                                       'minimum':  21,
                                       'maximum':  30,
                                       'format':   format3})
#YELLOW between 11 and 20
worksheet.conditional_format('R2:R'+str(len(filtered)), {'type':     'cell',
                                       'criteria': 'between',
                                       'minimum':  11,
                                       'maximum':  20,
                                       'format':   format2})
#RED between 0 and 10
worksheet.conditional_format('R2:R'+str(len(filtered)), {'type':     'cell',
                                       'criteria': 'between',
                                       'minimum':  0,
                                       'maximum':  10,
                                       'format':   format1})


workbook.close()
