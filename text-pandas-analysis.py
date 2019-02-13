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
dfwords = pd.DataFrame({"words" : words})
grouped = dfwords["words"].value_counts()
grouped = grouped.to_frame()
grouped.rename(columns={"words":"count"})

phrase = []
num = len(words)-1
for n in range(0,num):
        phrase.append(words[n]+" "+words[n+1])
dfphrase = pd.DataFrame({"phrase" : phrase})
grouped = dfphrase["phrase"].value_counts()
grouped = grouped.to_frame()
grouped.rename(columns={"phrase":"count"})

phrase3 = []
num = len(words)-2
for n in range(0,num):
        phrase3.append(words[n]+" "+words[n+1]+" "+words[n+2])
      
dfphrase3 = pd.DataFrame({"phrase3" : phrase3})
grouped = dfphrase3["phrase3"].value_counts()
grouped = grouped.to_frame()
grouped.rename(columns={"phrase3":"count"})
