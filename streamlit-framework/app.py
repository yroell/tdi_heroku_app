import streamlit as st
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from alpha_vantage.timeseries import TimeSeries
from bokeh.plotting import figure
from datetime import datetime
	
ts = TimeSeries(key="")
page = st.sidebar.selectbox("Choose a page", ['GOOGL', 'AAPL'])
input_month = st.sidebar.text_input("Choose a month", 3)
input_year = st.sidebar.text_input("Choose a year", 2021)

if page == 'GOOGL':
	st.title('This is for GOOGLE')
	data, meta_data = ts.get_daily('GOOGL')
	df_close = []
	df_date = []
	year = []
	month = []
	day = []
	for cl in data:
		df_close.append(float(data[cl]['4. close']))
		df_date.append(cl)
		full_date = datetime.strptime(cl, '%Y-%m-%d')
		year.append(full_date.year)
		month.append(full_date.month)
		day.append(full_date.day)

if page == 'AAPL':
	st.title('This is for AAPL')
	data, meta_data = ts.get_daily('AAPL')
	df_close = []
	df_date = []
	year = []
	month = []
	day = []
	for cl in data:
		df_close.append(float(data[cl]['4. close']))
		df_date.append(cl)
		full_date = datetime.strptime(cl, '%Y-%m-%d')
		year.append(full_date.year)
		month.append(full_date.month)
		day.append(full_date.day)

df = pd.DataFrame(list(zip(year, month, day, df_close)), columns = ['year', 'month', 'day', 'closing'])
df_plot = df[(df['year'] == int(input_year)) & (df['month'] == int(input_month))]
		
fig, ax = plt.subplots()
ax.plot(df_plot['day'],df_plot['closing'])
st.pyplot(fig)