import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime
	
ts = TimeSeries(key="")
page = st.sidebar.text_input("Choose a company", 'GOOGL')
input_month = st.sidebar.text_input("Choose a month", 3)
input_year = st.sidebar.text_input("Choose a year", 2021)

data, meta_data = ts.get_daily(page)
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

month_dict = {'1':'January', '2':'February', '3':'March', '4':'April', '5':'May', '6':'June', '7':'July', '8':'August', '9':'September', '10':'October', '11':'November', '12':'December'}
st.title('Company stock prices')
st.write('Available dates to pick from: ', month_dict[str(df.month.iloc[-1])], str(df.year.iloc[-1]), 'to', month_dict[str(df.month.iloc[0])], str(df.year.iloc[0]))
st.write('The stock ticker picked: ', page)
st.write('The month picked: ', month_dict[input_month])
st.write('The year picked: ', input_year)

fig, ax = plt.subplots()
ax.plot(df_plot['day'], df_plot['closing'])
ax.set(xlabel = 'Day in ' + month_dict[str(input_month)], ylabel = "Closing Price")
st.pyplot(fig)