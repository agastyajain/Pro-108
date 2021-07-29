import random
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import csv

df = pd.read_csv("data.csv")
weight = df["Weight(Pounds)"].tolist()
index = df["Index"].tolist()

#data=[]
#y_data = []

"""for n in range(0,100):
    int1 = random.randint(1,6)
    int2 = random.randint(1,6)
    sum = int1 + int2
    data.append(sum)
    y_data.append(n)
print(y_data)"""

fig = ff.create_distplot([weight],["weight"],show_hist=False)
fig.show()
