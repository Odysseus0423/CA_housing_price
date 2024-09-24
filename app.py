import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set('notebook')

df = pd.read_csv('housing.csv')

st.title('California Housing Data (1990) By Mingzhe Liu')

price_filter = st.slider('Minimal Median Housing Price:', 0, 500001, 200000)

location_filter = st.sidebar.multiselect(
     'Location Selector',
     df.ocean_proximity.unique(),  
     df.ocean_proximity.unique())  

income_level = st.sidebar.radio(
    'Select Income Level:', ['Low', 'Medium', 'High']
)

df = df[df.ocean_proximity.isin(location_filter)]

if income_level == 'Low':
    df = df[df.median_income <= 2.5]
elif income_level == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
elif income_level == 'High':
    df = df[df.median_income >= 4.5]

df = df[df.median_house_value >= price_filter]

st.subheader("Housing Locations on the Map")

st.map(df[['latitude', 'longitude']])

st.subheader('Housing Details:')

st.write(df[['median_house_value', 'latitude', 'longitude']])

st.subheader('California Housing Price Levels by Location')

fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(df['median_house_value'],bins=30)
ax.set_ylabel("Median House Value")
ax.set_xlabel("Frequency")
st.pyplot(fig)
