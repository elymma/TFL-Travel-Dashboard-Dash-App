import pandas as pd
import itertools
from datetime import datetime

df = pd.read_excel("cleaned_tfl_dataset_EDIT.xlsx")

# create lists of travel modes and dates
df.transport_list = df["Travel Mode"].unique().tolist()
# df.periods_list = df["Period ending"].tolist()

print(df.transport_list)
# print(df.periods_list)

# group dataset by year
df.by_year = df.groupby(df["Period ending"].map(lambda x: x.year))
# sum the number of journeys for each year
df.by_year_sums = df.by_year.sum()
# convert index ("Period ending") to a column
df.by_year_sums.reset_index(level=0, inplace=True)
# create a list of the years
df.years_list = df.by_year_sums["Period ending"].tolist()

print(df.years_list)


# reference
# https://stackoverflow.com/questions/33440640/python-pandas-pandas-core-groupby-dataframegroupby-object-at
# https://stackoverflow.com/questions/20461165/how-to-convert-index-of-a-pandas-dataframe-into-a-column