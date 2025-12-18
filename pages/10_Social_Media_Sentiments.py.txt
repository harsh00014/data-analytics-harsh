import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.title("🛒 E-Commerce Sales Performance")

df = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet", "Watch", "Headphones"],
    "Price": [1200, 800, 400, 250, 150],
    "Units_Sold": [50, 120, 80, 200, 300],
    "Profit": [6000, 9600, 3200, 5000, 4500]
})

fig = px.scatter(df, x="Price", y="Units_Sold", size="Profit", color="Product",
                 hover_name="Product", log_x=True, size_max=60)
st.plotly_chart(fig, use_container_width=True)
