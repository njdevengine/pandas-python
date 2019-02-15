#grab text file
#remove punctuation, special characters etc.
#split by spaces create an array of words
#create 2 word phrases create an array of 2 word phrases
#create 3 word phrases create an array of 3 word phrases
#create a dataframe for each with headers as word/phrase/phrase and count
#group by count for each
#sort top 20 in each
#visualize data in bar graph for each

import pandas as pd
import matplotlib.pyplot as pt
import numpy as np
import re

with open('folder/file.txt', 'r') as myfile:
    string = myfile.read().replace('\n', ' ')
    string = string.lower()
    
regex = re.compile('[^a-zA-Z]')
string = regex.sub(' ', string)

words = string.split(" ")

for word in words:
    word.lower()

words = list(filter(None, words))
dfphrase1 = pd.DataFrame({"words" : words})
grouped1 = dfphrase1["words"].value_counts()
grouped1 = grouped1.to_frame()
grouped1.rename(columns={"words":"count"})
#grouped1.to_csv('g1.csv')

phrase = []
num = len(words)-1
for n in range(0,num):
        phrase.append(words[n]+" "+words[n+1])
dfphrase2 = pd.DataFrame({"phrase" : phrase})
grouped2 = dfphrase2["phrase"].value_counts()
grouped2 = grouped2.to_frame()
grouped2.rename(columns={"phrase":"count"})
#grouped2.to_csv('g2.csv')

phrase3 = []
num = len(words)-2
for n in range(0,num):
        phrase3.append(words[n]+" "+words[n+1]+" "+words[n+2])
      
dfphrase3 = pd.DataFrame({"phrase3" : phrase3})
grouped3 = dfphrase3["phrase3"].value_counts()
grouped3 = grouped3.to_frame()
grouped3.rename(columns={"phrase3":"count"})
#grouped3.to_csv('g3.csv')

#dfphrase1.head()
#dfphrase2.head()
#dfphrase3.head()

#grouped1.head()
#grouped2.head()
#grouped3.head()

writer = pd.ExcelWriter('analysis/output.xlsx', engine = 'xlsxwriter')
grouped1.to_excel(writer, sheet_name='grouped1')
grouped2.to_excel(writer, sheet_name='grouped2')
grouped3.to_excel(writer, sheet_name='grouped3')
writer.save()
