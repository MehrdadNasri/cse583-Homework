# Homework 1 : Bicycle Data Analysis - Mehrdad 
import pandas as pd
import matplotlib.pyplot as plt

#Step1: Read the data from csv file and store it in a dataframe.
data = pd.read_csv("bicycle_data.csv") 
#The first columns in the dataframe includes "Date" which contains the date and time of each hourly observations. It is currently stored as object, but we expect it to be a Datetime type. 
#The second column contains the total number of counted cyclists on both sidewalks of the fremont bridge. 
# The third column contains the number of counted cyclists on the west sidewalk and the fourth column is the number of counted cyclists on the east sidewalk. 
# All of these three count columns are currently stored as float64 type. These counts can be also stored as integers.

#Step2: Convert the "Date" column to a Datetime type and the three count columns to Int64 type.

data['Date'] = pd.to_datetime(
    data['Date'], format='%m/%d/%Y %I:%M:%S %p'
)

data['Fremont Bridge Sidewalks, south of N 34th St Total'] = (
    data['Fremont Bridge Sidewalks, south of N 34th St Total'].astype('Int64')
)

data['Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk'] = (
    data['Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk'].astype('Int64')
)

data['Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk'] = (
    data['Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk'].astype('Int64')
)

#Step3: Add new columns 
data['Total'] = data['Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk'] + data['Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk']
data['Hour'] = data['Date'].dt.hour
data['Year'] = data['Date'].dt.year

#Step4: Create a subset of data for 2016
data_subset = data[data['Year'] == 2016]

#Step5: Taking care of missing values in the subset data
missing_rows = data_subset.isna().any(axis=1)
print("Number of missing time points:", missing_rows.sum()) 
# We have 1 time point with missing bike count data in 2016. I am removing that time point because missing data does not mean that no cyclists crossed the bridge at that time, so we cannot replace taht with 0 or any other value. 
data_subset = data_subset.dropna()

#Step6: Plot the coutssby hour
counts_by_hour = data_subset.groupby('Hour')['Total'].sum()
counts_by_hour.plot(kind='bar')
plt.title('Total Cyclist Counts Crossing by Hour - Fremont Bridge, 2016')
plt.xlabel('Hour of the Day')
plt.ylabel('Total Cyclist Counts')
plt.tight_layout()
plt.savefig('counts_by_hour.png')

#Step7: Find the hour with the highest total cyclist counts
average_by_hour = data_subset.groupby('Hour')['Total'].mean()
busiest_hour = average_by_hour.idxmax()
print("The hour with the highest total cyclist counts in 2016 is:", busiest_hour)
#The busiest hour is 17, meaning 5 PM to 6 PM.

