# COMP0034 Coursework 1

[Elymma's repository](https://github.com/elymma/Coursework-1.git)

## TFL Travel Dashboard

### Overall design

The design choices made for this dashboard were inspired by Alberto Cairo's work on graphics lies misleading visuals 
and aimed to recreate the simple and clean layout of websites such as the Google homepage and the Apple website homepage.

### Visualisation design

#### Visualisation 1: Travel Mode Usage Over Time
##### Target audience: 
* TFL Associated Employee: As the manager responsible for hiring bus drivers for TfL (TfL Associated Employee), I want 
to know when in the year bus usage is the lowest so that I can reduce the number of new hires in these periods. [User 
story 03]
##### Question answered: 
* How does usage of TFL services vary over a chosen time period?
##### Data needed:
* TFL usage data for all time periods and all travel modes.
##### Type of chart: 
* Line graph
##### Visual design aspects:
* Colour coded lines to distinguish between travel modes.
* Title describing what aspect of the data is being visualised, in this case travel mode usage over time.
* Subtitle indicating what time periods are currently displayed on the figure.
* The gradient of the lines gives a clear visual indication of the rate at which usage changes 
for each travel mode over time and how overall usage varies between each travel mode.
* The data set contains 12 years of TFL usage data and displaying this all at once could obscure important aspects of
the data as yearly trends would be harder to recognise. The choice choose how many years of data can be displayed at a 
time allows the data to be viewed in more detail by the user. 
* The minimum time period that can be displayed is one year. This is as this is it displays the yearly variation in usage, 
an important aspect to consider when making a judgement based on TFL usage.
* There are no additional chart elements shown beyond the title, years displayed, axis labels and key. This keeps the
focus on the actual data and not unnecessary chartjunk.
##### Evaluation 
##### Did it meet the design choices?
Yes, this chart allows the user to see the variation in usage for each travel mode over a chosen time period.
##### Strengths and weaknesses?
* Strengths: the user can choose to display between one and 12 years of data and can compare usage between different 
travel modes.
* Weakness: when multiple non-consecutive years are chosen to be displayed (e.g. 2010, 2014 and 2018), they are joined 
by a straight line that does not accurately represent the usage over the unselected time period. This could be improved 
by only allowing the user to select consecutive time periods e.g. 2010, 2011 and 2013 but not 2010, 2013 and 2017.
* Weakness: the user cannot isolate data according to travel mode. This would be usfeul for TFL Associated Employees 
only interested in specific travel modes. This could be improved by adding a checklist with a callback to select data 
for individual travel modes.


#### Visualisation 2: Statistics Panel
##### Target audience:
* TFL Associated Employee: As a licenced TfL busker (TfL Associated Employee), I want to know when in the year the usage 
of London Underground peaks so that I can apply for performance slots that will expose me to the highest number of 
people. [User story 02]
##### Question answered:
* In which recording period and for what travel mode did TFL usage peak over a chosen time period?
##### Data needed:
* TFL Data for all travel modes and recording periods.
##### Type of chart:
* N/A
##### Visual design aspects:
* The data from the data frame was formatted to be more readable. E.g. the datetime format was converted to a d/m/y 
format and the number of journeys was rounded to 1 decimal place. This made the data easier to understand as it is in a
format that is familiar to most people.
##### Evaluation 
##### Did it meet the design choices?
Partially yes, the panel shows very basic stats from the data, the busiest and quietest recording periods out of all the
travel modes.
##### Strengths and weaknesses?
* Strength: the panel gives an easy-to-read summary of the data from the charts, allowing the user to find the highest
and lowest periods without having to deeply study the data points from the charts.
* Weakness: the statistics do not show much more than what can be deducted from the other charts, making it somewhat 
redundant. To improve the use of the stats panel, the data could be manipulated. E.g. the highest and lowest recording
period could be displayed for each travel mode and compared to the values of the year before.

#### Visualisation 3: Variation in Travel Modes
##### Target audience:
* TFL Associated Employee: As a TFL Associated Employee I would like to know how much the usage of each travel mode 
varies over a chosen time period so that I can decide how the distribution of emplyees will likely need to be adjusted 
over that time period according how much the number of journeys varies. [New user story]
##### Question answered:
* How much variation is there in TFL usage for each travel mode over a chosen time period?
##### Data needed:
* TFL usage data for all recording periods and all travel modes.
##### Type of chart:
* Box-whisker chart
##### Visual design aspects:
* Colour coded lines to distinguish between travel modes.
* Title describing what aspect of the data is being visualised, in this case variation in TFL usage over a certain time 
period for each travel mode.
* Subtitle indicating what time periods are currently displayed on the figure.
* Width of boxes gives a clear visual display of the comparative degree of variation for each travel mode without the 
need for the use of numbers.
* The data set contains 12 years of TFL usage data and displaying this all at once could obscure important aspects of
the data as yearly trends would be harder to recognise. The choice choose how many years of data can be displayed at a 
time allows the data to be viewed in more detail by the user. 
* The minimum time period that can be displayed is one year. This is as this is it displays the yearly variation in usage, 
an important aspect to consider when making a judgement based on TFL usage.
* There are no additional chart elements shown beyond the title, years displayed, axis labels and key. This keeps the
focus on the actual data and not unnecessary chartjunk.
##### Evaluation 
##### Did it meet the design choices?
Yes, the chart clearly indicates how much the data for each recording period varied for a chosen time period for each 
travel mode.
##### Strengths and weaknesses?
* Strength: the area of each box indicates the amount of variation which makes comparisons between each travel mode
easy to see at a first glance.
* Weakness: the user cannot isolate data according to travel mode. This would be usfeul for TFL Associated Employees 
only interested in specific travel modes. This could be improved by adding a checklist with a callback to select data 
for individual travel modes.
* Weakness: there is no indication of how the variation in users varies over time. This could be improved by adding a 
statistics panel to display the percentage change compared to the year before.

#### Visualisation 4: Distribution of Travel Modes
##### Target audience:
* TFL Associated Employee: As an TfL Associated Employee, I want to be able to visualise the distribution of users 
across the TfL transport network for a chosen period so that I can appropriately distribute workers across the service 
according to the number of current users. [User story 01]
##### Question answered:
* How is usage of TFL services distributed between each travel mode for a chosen time period?
##### Data needed:
* TFL usage data for all time periods and all travel modes.
##### Type of chart:
* Pie chart
##### Visual design aspects:
* Colour coded areas to distinguish between travel modes.
* Title describing what aspect of the data is being visualised, in this case the proportion each travel mode takes of
the total TFL usage.
* Subtitle indicating what time periods are currently displayed on the figure.
* The comparative areas of each travel mode and the displayed percentages clearly show the proportion of each travel 
mode.
* The data set contains 12 years of TFL usage data and displaying this all at once could obscure important aspects of
the data as yearly trends would be harder to recognise. The choice choose how many years of data can be displayed at a 
time allows the data to be viewed in more detail by the user. 
* The minimum time period that can be displayed is one year. This is as this is it displays the yearly variation in 
usage, an important aspect to consider when making a judgement based on TFL usage.
* There are no additional chart elements shown beyond the title, years displayed, axis labels and key. This keeps the
focus on the actual data and not unnecessary chartjunk.
##### Evaluation 
##### Did it meet the design choices?
Yes, the chart clearly show the proportion that each travel mode takes of the total TFL usage.
##### Strengths and weaknesses?
* Strength: the use of coloured area to represent the proportion of a circle makes the data easier to understand at 
first glance and the percentage labels give a more accurate indication of the proportions.
* Weakness: there is no indication of how the proportions in users changes over time. This could be improved by adding a 
statistics panel to display the percentage change compared to the year before or by another chart type such as a stacked
bar chart which would display the proportions and how they change over time.


### References

https://faculty.ucmerced.edu/jvevea/classes/Spark/readings/Cairo2015_Chapter_GraphicsLiesMisleadingVisuals.pdf
https://stackoverflow.com/questions/33440640/python-pandas-pandas-core-groupby-dataframegroupby-object-at
https://stackoverflow.com/questions/20461165/how-to-convert-index-of-a-pandas-dataframe-into-a-column
https://medium.com/analytics-vidhya/valueerror-lengths-must-match-to-compare-when-adding-more-than-2-options-in-dropdown-3b4e0a5c77d4