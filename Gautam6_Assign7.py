#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on 2020-03-01 by Asmita Gautam
Assignment 07: Graphical analysis with python

Graphical analysis for earthquake data for last 30 days
Modified to add header and comments on 2020-03-08
"""

"""
Importing the required module 
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import scipy.stats as stats

#data = np.genfromtxt('all_month.csv')
"""
 genfromtxt does not work as the data type (dtype) are different between the column
but data type within each column is same so the file can be read through pandas
"""

#Read the given data table
df = pd.read_table('all_month.csv', header=0, sep=',')

# Plot histogram of the magnitude of earthquakes
f1 = plt.figure()
plt.hist(df['mag'].dropna(), bins=10, range=[0,10])
plt.xlabel('Magnitude')
plt.ylabel('Probability')
f1.text(0.5, -0.05, "Fig 1. Histogram of the magnitude of earthquakes", fontsize=15, 
        ha="center", va="center")
plt.show()

## Plot histogram by changing the bin width
f1a =plt.figure()
f1a, (ax1,ax2,ax3) = plt.subplots(3, sharex=True)
ax1.hist(df["mag"], bins=5, range=[0,10])
ax2.hist(df["mag"], bins=50, range=[0,10]) # plots to show difference of bins
ax3.hist(df["mag"], bins=100, range=[0,10]) 
plt.xlabel('Magnitude')
plt.ylabel('Probability')
f1a.text(0.5, -0.05, "Fig 1A. Histogram changing the bin width", fontsize=15, 
        ha="center", va="center")
plt.show()

#KDE
f2=plt.figure()
mag=df["mag"].dropna()
kde = stats.gaussian_kde(df["mag"].dropna())
spacing = np.linspace(0,10, num=500) #start,stop, and the number of points/samples between them
kde.covariance_factor = lambda : .25 # bandwidth adjustment
kde._compute_covariance()
plt.plot(spacing,kde(spacing))
plt.xlabel('Magnitude')
plt.ylabel('Frequency')
f2.text(0.5, -0.05, "Fig 2. KDE plot of the earthquake", fontsize=15, 
        ha="center", va="center")
plt.show()

#latitude versus longitude for all earthquakes
f3=plt.figure()
plt.scatter(df['longitude'], 
            y=df['latitude'], 
            s=2, c='blue') #setting point size and color
plt.ylabel('Latitude')
plt.xlabel('Longitude')
f3.text(0.5, -0.05, "Fig 3. Earthquake distribution", fontsize=15, 
        ha="center", va="center")
plt.show()

# normalized cummulative distribution plot of earthquake depth 
f4=plt.figure()
sort_depth = np.sort(df['depth'].dropna())
prob = np.linspace(0,1,len(sort_depth))
plt.plot(sort_depth, prob)
plt.xlabel('Depth (km)')
plt.ylabel('Probability')
f4.text(0.5, -0.05, "Fig 4. CDF of Earthquake depth", fontsize=15, 
        ha="center", va="center")
plt.show()

# Scatter plot of earthquake mag vs depth
f5=plt.figure()
plt.scatter(df['mag'],df['depth'],s=5)
plt.xlabel('Magnitude')
plt.ylabel('Depth (km)')
f5.text(0.5, -0.05, "Fig 5. Earthquake Magnitude vs Depth", fontsize=15, 
        ha="center", va="center")
plt.show()

# Quantile plot of earthquake mag 
f6=plt.figure()
stats.probplot(df['mag'].dropna(), dist="norm", plot=plt)
plt.xlabel('Normal Quantiles')
plt.ylabel('Data Quantiles')
f6.text(0.5, -0.05, "Fig 6. Q-Q Plot of Earthquake Magnitudes", fontsize=15, 
        ha="center", va="center")
plt.show()
# analysis this question