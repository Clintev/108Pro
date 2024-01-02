import csv
import plotly.figure_factory as ff
import pandas as pd

reader = pd.read_csv("data.csv")
Ag = reader["Avg Rating"].tolist()

figure = ff.create_distplot([Ag], ["Average Rating"], show_hist=True)
figure.show()