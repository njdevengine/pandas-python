# Import Dependencies
import pandas as pd

# Create a path to the csv and read it into a Pandas DataFrame
csv_path = "Resources/ted_talks.csv"
ted_df = pd.read_csv(csv_path)

ted_df.head()

# Figure out the minimum and maximum views for a TED Talk
minviews = ted_df["views"].min()
maxviews =ted_df["views"].max()
print(f"min views {minviews}")
print(f"max views {maxviews}")

# Create bins in which to place values based upon TED Talk views
bins = [100000,500000,1000000,5000000,10000000,99999999999999999999999]
group_names = ["Below100k","Below500k","Below1m","Below5m","Above10m"]
# Create labels for these bins

# Slice the data and place it into bins
binned= ted_df["viewbins"] = pd.cut(ted_df["views"], bins,labels=group_names)
ted_df.head(100)

# Create a GroupBy object based upon "View Group"

# Find how many rows fall into each bin

x =ted_df.groupby("viewbins")
x.count()
# Get the average of each column within the GroupBy object
x.mean()
