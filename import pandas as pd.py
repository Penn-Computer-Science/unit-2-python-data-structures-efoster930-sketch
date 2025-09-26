import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

#load our data frame
df = pd.read_csv("pennData.csv")
pennData = pd.DataFrame(df)

print("-_"*20)
print("Head of the data frame") #Prints the first five rows of the data frame
print(pennData.head())

print("-_"*20)
print("Tail of the data frame") #Prints the final five rows of the data frame
print(pennData.tail())

print("-_"*20)
print("Summary of the data frame") #Gives a summary of the data frame
print(pennData.info())

print("-_"*20)
print("Statisitical Analysis") #Gives the mean, count, min, std, 25%, 50%, and 75%.
print(round(pennData.describe()))

print("-_"*20)
print("Count of Students in Pathway") #Shows students in each pathway
print(pennData["Pathway"].value_counts())

print("-_"*20)
print("Average GPA Per Year") #Gives you the average GPA of each year.
print(pennData.groupby('Year')['GPA'].mean())

print("-_"*20)
print("Top 3 Students by GPA") #Shows the top students 
print(pennData.sort_values(by ='GPA', ascending=False).head(3))

print("-_"*20)
print("Students with GPA > 3.5") #
print(pennData[pennData['GPA']>3.5])

print("-_"*20)
print("First Student Data") #
print(pennData.iloc[0])