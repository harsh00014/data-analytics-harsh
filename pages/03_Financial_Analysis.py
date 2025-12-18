import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("📈 Financial Trend Analysis")
st.write("This page simulates market data trends over a 30-day period.")

# Create time-series data
df = pd.DataFrame({
    'Date': pd.date_range(start='2025-01-01', periods=30),
    'Revenue': np.random.randint(1000, 5000, 30).cumsum(),
    'Expenses': np.random.randint(800, 4000, 30).cumsum()
})

# Area Chart
fig = px.area(df, x='Date', y=['Revenue', 'Expenses'], 
              title="Cumulative Revenue vs Expenses",
              color_discrete_sequence=['#00CC96', '#EF553B'])
st.plotly_chart(fig, use_container_width=True)
