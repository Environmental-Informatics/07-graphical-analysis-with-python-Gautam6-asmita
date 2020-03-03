# Environmental Informatics

## Assignment 07 - Graphical Analysis with Python

### Lab Objectives

On completion of this lab, students will be able to:

1. Use pandas DataFrames to conduct a graphical analysis of a dataset.
2. Generate a variety of figures as part of a graphical analysis of a new dataset.
3. Embed those figures into a test document, and write descriptive captions.

### Reading Assignment

Data Analysis with Open Source Tools:

- Chapter 1: Introduction
- Chapter 2: A single variable: Shape and distribution
- Chapter 3: Two Variables: Establishing Relationships

### The Lab Assignment

Start by downloading the data for this assignment as follows:

- Go to the [USGS earthquake hazards web site](http://earthquake.usgs.gov/earthquakes/feed/) and download data on recent activity in the "Spreadsheet Format" to get data in a CSV file. 

- Select "All Earthquakes" for the past "30 days". 

- Save It will be a CSV file, and its contents are described at the site (5 pts, submitted with your final program). 

- You will need to document this process (including date and time of download) for your metadata file.

Next, write a Python script to complete the following tasks (note the percentages below reflect the break-down of scoring within the "program running" category):

1. Open and read the contents of the file into Python.

   - You will quickly find that the numpyfunction genfromtxt() will not work with this data file.  Why not?

   - The best option for reading this file will be to make use of the [read_table()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_table.html) method within the pandas module.  The read_table() method is the most general, while the similar modules read_csv() and read_fwf() are for more specific file structures - comma separated variables and fixed width files, respectively.

   - For a tutorial introducing features of pandas and its dataframe data type work through the tutorial material as [10 minutes to pandas](see http://pandas.pydata.org/pandas-docs/stable/10min.html).

   - Much of what you learned for working with numpy arrays last week will apply to dataframes as well, but there is a difference in how you index and slice them (an improvement over numpy structured arrays).

   - Don't worry about understanding date and time in pandas (or Python for that matter), we will focus on date and time concepts in an upcoming lab assignment.

   - The pandas dataframe is built to handle heterogeneous data (data that is not all the same), as opposed to numpy, which is designed for homogeneous data (data that is all the same).  It brings back more of the flexibility of Python lists, but is built relying on the more powerful numpyarray data type.  Conceptually, it is similar to the dataframes used within the R statistics package (for example, see the [R Tutorial page on Data Frames](http://www.r-tutor.com/r-introduction/data-frame)).

3. Using matplotlib conduct the following graphical analysis of the data:
   - Generate a histogram of earthquake magnitude, using a bin width of 1 and a range of 0 to 10. (hint: how does the selction of bin size and range affect what the historgram displays?  what does the histogram suggest about the distribution of the data?)
   - Generate a KDE plot for the same data. (hint: indicate selections for the kernel type and kernel width, and comment on similarities and differences between the histogram and the KDE plot)
   - Plot latitude versus longitude for all earthquakes.  (hint: comment on the distribution of those points.  be sure that you put longitude on the x-axis and latitude on the y-axis, why?)
   - Generate a normalized cumulative distribution plot of earthquake depths. (hint: comment on what this plot indicates about the distribution of earthquake depths)
   - Generate a scatter plot of earthquake magnitude (x-axis) with depth (y-axis). (hint: comment on how depth and magnitude are related)
   - Generate a quantile or Q-Q plot of the earthquake magnitudes.  (hint: what statistical distribution does your Q-Q plot assume? does your data comply with that distribution?)

4. Be sure that the script has a complete header comment block, appropriate in-line comments, and runs without intervention.

#### What to turn in...

The following should be included in your GitHub repository:

1. The data file downloaded from the [USGS earthquake hazards web site](http://earthquake.usgs.gov/earthquakes/feed/).

2. A working program called **program-07.py**.

5. A metadata file called **Metadata.pdf**:
   - Use Word or similar word processing program (Open Office, `openoffice.org`, is available on all of the clusters and does many of the same things as Microsoft Office).
   - Describe the source and format of the input data (not more than half a page),
   - Describe the types of analysis conducted by your script (not more than half a page),
   - Import the graphical analysis figures your developed in the previous section, and write a caption that describes the figure and addresses the hints provided for each figure.
   - Captions should be consecutively numbered.
   - Convert the Metadata file into a PDF file prior to submission.

7. Put your input file, processing script and metadata file in the assignment repository and push to GitHub to submit.

#### Grading Rubric (50 pts Total)

| Question | Description | Score |
| -------- | ----------- | ----- |
| 1. | Provide a copy of the original earthquake data file | 4 pts |
| 2. | Working Program ||
| 2.1. | Use pandas read_table() (or similar) to read file | 2 pts |
| 2.2. | Plot histogram of earthquake magnitude | 4 pts |
| 2.3. | KDE plot of earthquake magnitude - indicate kernel type and width | 6 pts |
| 2.4. | Plot latitude versus longitude for all earthquakes | 4 pts |
| 2.5. | Normalized CDFof earthquake depths - comment on distribution | 4 pts |
| 2.6. | Scatterplot of earthquake magniture (X-axis) with depth (y-axis) - comment on in metadata | 4 pts |
| 2.7. | Q-Q plot of earthquake magnitudes - what distribution does your plot use? does your data comply with that distribution? | 4 pts |
| 2.8. | Program runs | 2 pts |
| 2.9. | Program has complete header and adequate in-line comments | 2 pts |
| 3. | Metadata | |
| 3.1. | Includes provenance of earthquake data | 2 pts |
| 3.2. | Discuss why genfromtxt() will not work with this data file | 2 pts |
| 3.3. | Includes all figures generated by the program | 2 pts |
| 3.4. | Each figure includes a numbered caption that describes the figure and addresses the hints provided for each figure | 6 pts |
| 3.5. | Metadata is provided as a PDF | 2 pts |
