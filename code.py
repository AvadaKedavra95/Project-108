import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv("data.csv")
df_list = list(df["Avg_Rating"])
print(df_list)
fig = ff.create_distplot([df_list], ["Avg_Rating"], show_hist=True)
fig.show()
