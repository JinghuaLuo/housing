import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

df = pd.read_csv('housing.csv')

# title
st.title('California Housing(1990) Data by Jinghua Luo')

# substitle
st.subheader('See more filters in the sidebar')

# add a slider
price_slider = st.slider('Median House Price', 0, 500001)

# filter the dataframe
df = df[df.median_house_value >= price_slider]

# sidebars: filter location type
location_filter = st.sidebar.multiselect(
    'Choose the location type',
    df.ocean_proximity.unique(),
    df.ocean_proximity.unique())
df = df[df.ocean_proximity.isin(location_filter)]

# radio button: filter income level
income_filter = st.sidebar.radio(
    'Choose income level',
    ('Low', 'Median', 'High')
)
if income_filter == 'Low':
    df = df[df.median_income < 2.5]
elif income_filter == 'High':
    df = df[df.median_income > 4.5]
elif income_filter == 'Median':
    df = df[(df.median_income >= 2.5) & (df.median_income <= 4.5)]

# show the map
st.map(df)

# produce median_house_value hist
st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots(figsize=(10,5))
price_value = df.median_house_value
price_value.hist(bins=30)
st.pyplot(fig)

# show the df
st.write(df)






