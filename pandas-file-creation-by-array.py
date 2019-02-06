import pandas as pd
myarray=["ABC","DEF","GHI"]
array_length = len(myarray)
path = "headerfile.csv"
for i in range(array_length):
    mydf = pd.read_csv(path,encoding = "UTF-8")
    mydf.to_csv(str(myarray[i])+".csv",encoding = "utf-8", index =False, header = True)
