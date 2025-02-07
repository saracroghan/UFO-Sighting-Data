
# -------------------------------------------------------
# Insights:
# Visual 1:
# There is a clear, almost exponential increase of sightings
# starting in the 2000's. There are a couple factors that could,
# and almost certainly have contributed to this uptick. Primarily, the
# amount of air traffic has been (almost) equally and exponentially
# increasing the 1950s. The more traffic in the air, the mores eyes
# able to sight UFO's and report them.
# -------------------------------------------------------
# Visual 2:
# The states with the most UFO sightings since 1910 are also states that
# have some of the largest populations within the US. States with the most
# sightings (CA, FL, TX, NY, IL, PA) also appear on a list of the top 10 most
# populated states. This makes logical sense, the more people in the state,
# the more people that are able to see, identify and report UFO sightings.
# -------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

#PROCESS FILE AND CREATE DATA FRAME
file_name = "ufo_sightings.csv"

sightings_dataframe = pd.read_csv(file_name)

# VISUAL 1
# sort data frame by the value of the year sighted
sightings_df_by_year = sightings_dataframe.sort_values(["Dates.Sighted.Year"])
# count up the number of sighitngs per year
data_to_plot = sightings_df_by_year["Dates.Sighted.Year"].value_counts(sort=False)
#create a graphing window and set the title
fig, axs = plt.subplots(layout = "constrained")
fig.canvas.manager.set_window_title("UFO Sightings by Year")
# use the data_to_plot series as the data for the graph and create axes labels
data_to_plot.plot(xlabel= "Year", ylabel = "Number of UFO Sightings", \
                  title = "UFO Sightings from 1910 to 2014", color = "red")

# VISUAL 2
# create a series that has the counts of the number of sightings in each state
data_to_plot = sightings_dataframe["Location.State"].value_counts()
# create a second graphing window and set the title
fig2, axs2 = plt.subplots(layout = "constrained")
fig2.canvas.manager.set_window_title("UFO Sightings by State")
# use the data_to_plot series as the data for the graph and create axes labels
data_to_plot.plot(kind = "bar", ylabel = "Number of UFO Sightings", xlabel = "State",\
                  title = "UFO Sightings per State from 1910 to 2014", color = "blue")
#show the graphs
plt.show()
                           





