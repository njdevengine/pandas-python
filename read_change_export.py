# Import Dependencies
import pandas as pd
# Make a reference to the books.csv file path
path = "Resources/books.csv"
# Import the books.csv file as a DataFrame
booksdf = pd.read_csv(path,encoding = "UTF-8")
booksdf.drop(columns = ["column 1","column 2"])
booksdf.head()
renamed_df.to_csv("Output/books_clean.csv",encoding = "utf-8", index = False, header = True)
