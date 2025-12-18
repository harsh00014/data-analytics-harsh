import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 Global Distribution Map")
st.write("Visualizing data density across different world regions.")

# Sample geographic data
geo_data = pd.DataFrame({
    'Country': ['USA', 'India', 'UK', 'Canada', 'Germany', 'Brazil', 'Japan'],
    'Users': [5000, 4500, 1200, 800, 2000, 1500, 3000],
    'iso_alpha': ['USA', 'IND', 'GBR', 'CAN', 'DEU', 'BRA', 'JPN']
})

fig = px.choropleth(geo_data, locations="iso_alpha", color="Users",
                    hover_name="Country", projection="natural earth",
                    color_continuous_scale=px.colors.sequential.Plasma)

st.plotly_chart(fig, use_container_width=True)
