# Import Dependencies
import pandas as pd

raw_data = {
    'Class': ['Oct', 'Oct', 'Jan', 'Jan', 'Oct', 'Jan'], 
    'Name': ["Cyndy", "Logan", "Laci", "Elmer", "Crystle", "Emmie"], 
    'Test Score': [90, 56, 72, 88, 98, 67]}
df = pd.DataFrame(raw_data)
df

bins = [0,60,70,80,90,100]
group_names = ["F","D","C","B","A"]

df["Test Score Summary"] = pd.cut(df["Test Score"], bins,labels=group_names)
df.head()
