import streamlit as st
import seaborn as sns
import pandas as pd
import altair as alt
import plotly.express as px
df_iris = sns.load_dataset("iris")
int_plot = px.scatter_3d(df_iris, x='sepal_length', y='sepal_width', z='petal_width', color='species')
int_plot.show()