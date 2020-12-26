import plotly.graph_objects as go
import pandas as pd
import csv

df = pd.read_csv('data.csv')
student_df = df.groupby("level")["attempt"].mean()

fig = go.Figure(go.Bar(
    x = student_df,
    y = ['Level 1','Level 2','Level 3','Level 4'],orientation = 'h'
))
fig.show()