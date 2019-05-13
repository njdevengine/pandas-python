from pandas import ExcelWriter

output = '/directory/joined.xlsx'
def save_xls(list_dfs, xls_path):
    with ExcelWriter(xls_path) as writer:
        for n, df in enumerate(list_dfs):
            df.to_excel(writer,'sheet%s' % n)
        writer.save()
        
save_xls(dataframes,output)
