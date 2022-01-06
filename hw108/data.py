import pandas as pd
import csv
import plotly.figure_factory as ff
df=pd.read_csv("data.csv")
fig=ff.create_distplot([df["Avg Rating"].tolist()],["avgRating"],show_hist=False)
#fig=ff.create_distplot([df["Height(Inches)"].tolist()],["height"],show_hist=False)
fig.show()