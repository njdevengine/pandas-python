import pandas as pd
myarray=["ABC","DEF","GHI"]
array_length = len(myarray)
path = "sourcefile.csv"
for i in range(0,array_length):
    df = pd.read_csv(path,encoding = "UTF-8")
    #only saves values that match your array member, can be switched to !=
    df = df[df.headertobefiltered == myarray[i]]
    df.to_csv(str(myarray[i])+".csv",encoding = "utf-8", index =False, header = True)
