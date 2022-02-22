import pandas as pd
import plotly.express as px


df = pd.read_excel("cleaned_tfl_dataset_EDIT.xlsx")

# create lists of travel modes and dates
df.transport_list = df["Travel Mode"].unique().tolist()
df.periods_list = df["Period ending"].tolist()

# print(df.transport_list)
# print(df.periods_list)

year = [2020, 2021]

# df.chosen_year = df.copy()

# select data for chosen year
# df.chosen_year = df[df["Period ending"].dt.year == year[0]]
# fig_box = px.box(df.chosen_year, x="Travel Mode", y="Journeys (m)", color="Travel Mode", title="Variation in Travel Modes for {}".format(year))
# fig_box.show()

if type(year) != int:
    # when there is a list of year values
    df.chosen_year = df.chosen_year[df.chosen_year["Period ending"].dt.year.isin(year)]
else:
    # when there is only on year value
    df.chosen_year = df.chosen_year[df.chosen_year["Period ending"].dt.year == year]

print(df.chosen_year)


travel = "Bus"

df.chosen_travel = df[df["Travel Mode"].str.contains(travel)]

#print(df.chosen_travel)


# dates_2017 = list(filter(lambda x: x.year == 2017, df.periods_list))

# print(dates_2017)


# group dataset by year
df.by_year = df.groupby(df["Period ending"].map(lambda x: x.year))
# sum the number of journeys for each year
df.by_year_sums = df.by_year.sum()
# convert index ("Period ending") to a column
df.by_year_sums.reset_index(level=0, inplace=True)
# create a list of the years
df.years_list = df.by_year_sums["Period ending"].tolist()

# print(df.years_list)

# print(df.by_year_sums)

# reference
# https://stackoverflow.com/questions/33440640/python-pandas-pandas-core-groupby-dataframegroupby-object-at
# https://stackoverflow.com/questions/20461165/how-to-convert-index-of-a-pandas-dataframe-into-a-column
# https://medium.com/analytics-vidhya/valueerror-lengths-must-match-to-compare-when-adding-more-than-2-options-in-dropdown-3b4e0a5c77d4