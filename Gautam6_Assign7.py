#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on 2020-03-01 by Asmita Gautam
Assignment 07: Graphical analysis with python

Graphical analysis for earthquake data for last 30 days
Modified to add header and comments on 2020-03-08
"""

"""
Importing the required module 
numpy
pandas
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#data = np.genfromtxt('all_month.csv')
"""
 genfromtxt does not work as the data type (dtype) are different between the column
but data type within each column is same so the file can be read through pandas
"""

# for "accurately" evaluate the CDF for depth
from matplotlib.ticker import (AutoMinorLocator)

df = pd.read_csv("all_month.csv") # create dataframe

#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax1 = fig.add_subplot(311)
#ax2 = fig.add_subplot(312)
#ax3 = fig.add_subplot(313)

### Histogram ###
# change of bin width result in a smoothier distribution, but there's a critical 
# point where too much bins will render the plot useless as we can see a trend 
# anymore and can make decision from it
f1, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)
ax1.hist(df["mag"], bins=10, range=[0,10]) # required plot
ax2.hist(df["mag"], bins=20, range=[0,10]) # plots to show difference of bins
ax3.hist(df["mag"], bins=100, range=[0,10])
f1.text(0.04, 0.5, "Frequency", ha="center", va="center", 
       rotation="vertical")
f1.text(0.5, 0.04, "Magnitude", ha="center", va="center")
f1.text(0.5, -0.05, "Fig 1. Effect of Bin Width Alteration", fontsize=15, 
        ha="center", va="center")

# smaller range result in a smoother distribution, but since range discard
# value outside of it, it should exercise with caution as not to lose
# data/information
f2, (ax1, ax2, ax3) = plt.subplots(3) # different x-axis
ax1.hist(df["mag"], bins=10, range=[0,10]) # required plot
ax2.hist(df["mag"], bins=10, range=[0,5]) # plots to show difference of range
ax3.hist(df["mag"], bins=10, range=[0,20])
f2.text(0.04, 0.5, "Frequency", ha="center", va="center", 
       rotation="vertical")
f2.text(0.5, 0.04, "Magnitude", ha="center", va="center")
f2.text(0.5, -0.05, "Fig 2. Effect of Range Alteration", fontsize=15, 
        ha="center", va="center")

## Looking at the required plot bin width 1 and range of 0 to 10, the 
# distribution looks lognormal to me

### KDE ###
f3 = plt.figure()
ax1 = f3.add_subplot(311)
ax2 = f3.add_subplot(312, sharex=ax1) # x-axis is the same after initial plots
ax3 = f3.add_subplot(313, sharex=ax1)
ax1.set_xlim([0,10]) # these three lines can be commented out to see the 
ax2.set_xlim([0,10]) # real shape without omitting "outlier"
ax3.set_xlim([0,10])
# increase bw_method smoothen distribution, 0.1 is the closest fit to the other
# two methods, width is left as default, a smaller width generates smoother 
# result 
df["mag"].plot.kde(bw_method=0.1, ax=ax1) 
df["mag"].plot.kde(bw_method="silverman", ax=ax2) # plot 1 and 2 can be merged
# to show the similarity
df["mag"].plot.kde(bw_method="scott", ax=ax3) # default, looks identical to
# silverman method
f3.text(0.5, 0.04, "Magnitude", ha="center", va="center")
f3.text(0.5, -0.05, "Fig 3. KDE Comparison", fontsize=15, 
        ha="center", va="center")
# Naturally, KDE plot bear resemblance to histogram since the same data was 
# used, similar distribution/shape can be observed, however, KDE is much 
# smoothier than histogram, at least when comparing the required plots (when 
# the range was reduce to 5, their similarity converges)

### Lat. vs Long. ###
f4 = plt.figure()
plt.scatter(df["longitude"], df["latitude"], s=3)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
f4.text(0.5, -0.05, "Fig 4. Earthquake Events Location", fontsize=15, 
        ha="center", va="center")
# the placement of Long on x and Lat on y is due to Lat value changes along 
# vertical axis and Long value changes along horizontal axis, just by looking
# at the map, it can be seen that most event occurs near shoreline where most
# of the Tectonic fault lines reside

### Normalized CDF of Earthquake Depth ###
depth = df["depth"]
'''
# I realized after the whole block of code, maybe the cumulative need to be 
# normalized, this is kept here in case this is what was asked for
depth_normalized = (depth-min(depth))/(max(depth)-min(depth)) # min-max scaling
depth_normalized2 = (depth-depth.mean())/depth.std() # standardization scaling
# evaluate the histogram
bin_selection = (max(depth)-min(depth))*(len(depth)**(1/3))/(3.49*depth.std())
# just one method by scott 1979, same if use other two normalized data
values, base = np.histogram(depth_normalized, bins=int(bin_selection))
# evaluate the cumulative
cumulative = np.cumsum(values)
values2, base2 = np.histogram(depth_normalized2, bins=int(bin_selection))
cumulative2 = np.cumsum(values2)
#f5, (ax1, ax2) = plt.subplot(2)
f5 = plt.figure()
ax1 = f5.add_subplot(211)
ax2 = f5.add_subplot(212)
ax1.plot(base[:-1], cumulative)
ax2.plot(base2[:-1], cumulative2)
f5.text(0.5, 0.04, "Normalized Depth", ha="center", va="center") # unitless
f5.text(0.02, 0.5, "Counts", ha="center", va="center", 
       rotation="vertical")
f5.text(0.5, -0.05, "Fig 5. Normalized CDF of Earthquakes Depth", fontsize=15, 
        ha="center", va="center")
# notice due to different method of normalization, the x-axes are different
'''
# evaluate the histogram
bin_selection = (max(depth)-min(depth))*(len(depth)**(1/3))/(3.49*depth.std())
# just one method by scott 1979, same if use other two normalized data
values, base = np.histogram(depth, bins=int(bin_selection))
cumulative = np.cumsum(values)
cumulative_normalized = cumulative/sum(values)
f5, ax = plt.subplots()
ax.plot(base[:-1], cumulative_normalized)
ax.grid(which="both")
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(which="minor", color="r")
f5.text(0.5, 0.04, "Depth (km)", ha="center", va="center") # unitless
f5.text(0.02, 0.5, "Cumulative Probability", ha="center", va="center", 
       rotation="vertical")
f5.text(0.5, -0.05, "Fig 5. Normalized CDF of Earthquakes Depth", fontsize=15, 
        ha="center", va="center")
# the plot (though very cluttered), shows 80% of the earthquake event happened
# has a depth lower than 10 km

### Mag. vs Dep. ###
f6, ax = plt.subplots()
ax.scatter(df["mag"], depth, s=0.5)
ax.set_xlabel("Magnitude")
ax.set_ylabel("Depth (km)")
f6.text(0.5, -0.05, "Fig 6. Relation between Earthquake Magnitude and Depth", 
        fontsize=15, ha="center", va="center")
# Higher Magnitude has a positive relation to depth, especially for large value
# (mag > 4), however, there are much more occurrence of various magnitude 
# associated with low depth

### Q-Q plot for Magnitude ###
''' 
method 1 on same plot
#import scipy.stats as stats
#f7 = plt.figure()
#stats.probplot(df["mag"], dist="norm", plot=plt, fit=True)
#plt.plot([-4, 3],[-4, 3], color='r', linewidth=2)
#stats.probplot(np.log(df["mag"]), dist="norm", plot=plt)
'''
# method 2
import statsmodels.api as sm
f7 = plt.figure()
ax1 = f7.add_subplot(211)
ax2 = f7.add_subplot(212)
sm.qqplot(df["mag"], line="45", ax=ax1) # normal dist
sm.qqplot(np.log(df["mag"]), line="45", ax=ax2) # lognormal dist
f7.text(0.5, -0.05, "Fig 7. Q-Q Plots for Earthquake Magnitude", fontsize=15, 
        ha="center", va="center")
# both normal and lognormal are tested , lognormal fit decently for larger 
# values while normal fit ok overall with a shift of location parameter (mean)
# perhaps a normality test of shapiro-wilk test could be conducted to further
# analysis this question