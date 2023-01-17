# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 16:03:37 2023

@author: Sri Charan
"""



#Importing required libraries
import pandas as pnds_
import matplotlib.pyplot as mat_plt
from matplotlib.figure import Figure
import numpy as nmpi


#loading the file contatining data of crime 

crime = pnds_.read_csv("Calderdale Recorded Crime 2015-16 to 2021-22.csv")


crime


# # Data Cleaning


#unnecessary columns have been dropped
crime = crime.drop(columns = ["Force Name", "CSP Name","Offence Description","OffenceCode"])
#checking if the dataset contains null values
crime.isnull().sum()


#generating information of this dataset
crime.info()


#dropping an unnecessary row containing the sum of all crimes
crime=crime.iloc[:-1, :]
crime


# # Line Plot

# Defining a function to plot line chart
def line_plotting(data,x,y1,y2):
    """This function plots a multiple line plot. It takes various arguments like dataframe, column for x-axis, 
    column 1 to be plotted on y-axis and column 2 to be plotted on y-axis."""
    x_data = data[x]
    y1_data = data[y1]
    y2_data = data[y2]
    mat_plt.plot(x_data, y1_data, color = 'r')
    mat_plt.plot(x_data, y2_data, color ='b', linestyle='dotted')
    mat_plt.xticks(rotation=90)
    mat_plt.title("Number of cases depending on {}".format(x), fontsize=20)
    mat_plt.legend(title="Years", labels=["{}".format(y1),"{}".format(y2)], bbox_to_anchor=(1.50, 1.0))
    mat_plt.xlabel("{}".format(x),fontsize=15)
    mat_plt.ylabel("Number of cases", fontsize=15)
    mat_plt.show()


#Calling line_plotting function
line_plotting(crime,"Offence Subgroup","2015/16","2021/22")


# # Pie Chart


#getting unique values from offence group column
crime["Offence Group"].unique()
Offence_groups = ['Criminal damage and arson', 'Drug offences','Miscellaneous crimes', 'Possession of weapons offences','Public order offences', 'Robbery', 'Sexual offences','Theft offences', 'Violence against the person']


#function to plot a pie chart
def pie_plotting(data_frame):
    """This function creates a pie chart by taking in dataframe as the argument."""
    axs, figr = mat_plt.subplots(figsize =(10,10))
    #plotting the sum of all the cases grouped by offence group column
    mat_plt.pie(data_frame.groupby(["Offence Group"])["2021/22"].sum(), labels = Offence_groups, startangle = 90, autopct='%1.2f%%')
    #setting the legend
    axs.legend(title="Type of Offences", labels=Offence_groups, loc ="upper right",  bbox_to_anchor=(1.50, 1.0), fontsize=15)
    #title for the plot
    figr.set_title("Total cases based on offences in the year 2021-22", fontsize = 25)


#calling the function to plot a pie chart
pie_plotting(crime)


# # Scatter Plot


#taking the values of offence group as unique values into a new dataframe
crime_offence = pnds_.DataFrame({'Offence Group': pnds_.Series(dtype='str')})
crime_offence.loc[:,'Offence Group'] = Offence_groups
crime_offence


#Defining a function to plot a scatter chart
def scatter_plotting(data, c1,c2):
    """This function plots a scatter chart. It takes arguments which include dataset, column 1 to be plotted on x-axis 
    and column 2 to be plotted on y-axis."""
    #taking the sum of cases by grouping the data in accordance with the offence group
    x = data.groupby(["Offence Group"])[c1].sum()
    y = data.groupby(["Offence Group"])[c2].sum()
    mat_plt.figure(figsize=(14,10))
    #changing the scale used on x-axis and y-axis
    ax=mat_plt.gca()
    ax.locator_params('y', nbins=20)
    mat_plt.locator_params('x', nbins=20)
    #plotting the data
    scatter = mat_plt.scatter(x, y,c=crime_offence["Offence Group"].astype('category').cat.codes)
    #setting legend, xlabel, ylabel and title
    mat_plt.legend(handles=scatter.legend_elements()[0], labels=Offence_groups, title="Offences", fontsize='12', bbox_to_anchor=(1.50, 1.0))
    mat_plt.xlabel("Number of cases in {}".format(c1), fontsize='18')
    mat_plt.ylabel("Number of cases in {}".format(c2), fontsize='18')
    mat_plt.title("Number of cases depending on offence groups", fontsize='23')
    mat_plt.show()


#Calling the scatter_plotting function here to plot a scatter chart
scatter_plotting(crime, "2021/22", "2018/19")



#creating a new scatter plot which plots number of cases based on offence subgroups for any particular year
x=crime["Offence Subgroup"].unique()
y=crime.groupby(["Offence Subgroup"])["2019/20"].sum()
#plotting by setting the marker to be a star
mat_plt.scatter(x, y, c ="blue", marker="*")
#setting xticks, xlabel, ylabel, title, legend
mat_plt.xticks(rotation=90)
mat_plt.title("Number of cases based on offence subgroups", fontsize=20)
mat_plt.xlabel("Offence Subgroups", fontsize=18)
mat_plt.ylabel("Number of cases", fontsize=18)
mat_plt.legend(title ="Year", labels =["2019/20"])

