import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set('notebook')
st.title('California Housing Data')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
price_filter = st.slider('Minimal Median housing price:', 0.0, 500001.0, 200000.0)  # min, max, default

# create a multi select
location_filter = st.sidebar.multiselect(
     'Location Selector',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# create a input form
income_level=st.sidebar.radio(
    'Select Income Level:', ('Low,Medium,High')
)


# filter by population
df = df[df.median_house_value >= price_filter]

# filter by capital
df = df[df.ocean_proximity.isin(location_filter)]

if price_filter!='ALL':
    df = df[df.median_house_value == price_filter]

# show on map
st.map(df)

# show dataframe
st.subheader('Housing Details:')
st.write(df[['median_house_value', 'latitude', 'longitude']])

# show the plot
st.subheader('California housing price level by location')
fig, ax = plt.subplots(figsize=(20, 5))
pop_sum = df.groupby('ocean_proximity')['median_house_value'].sum()
pop_sum.plot.bar(ax=ax)
st.pyplot(fig)