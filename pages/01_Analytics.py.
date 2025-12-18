import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Deep Dive Analytics", layout="wide")
st.title("📊 Multi-Dimensional Analytics")

# Generate Sample Data
data = pd.DataFrame({
    'Category': np.repeat(['Tech', 'Finance', 'Health', 'Education'], 25),
    'Performance': np.random.randint(50, 100, 100),
    'Growth': np.random.uniform(1, 10, 100),
    'Region': np.tile(['North', 'South', 'East', 'West', 'Central'], 20)
})

# 1. Row of KPI Cards
m1, m2, m3 = st.columns(3)
m1.metric("Total Records", len(data))
m2.metric("Avg Performance", f"{data['Performance'].mean():.1f}%")
m3.metric("Top Sector", "Tech")

st.markdown("---")

# 2. Advanced Comparison Charts
col1, col2 = st.columns(2)

with col1:
    st.write("#### Performance by Category & Region")
    # This bar chart allows the examiner to click categories to filter
    fig1 = px.bar(data, x='Category', y='Performance', color='Region', 
                  barmode='group', template='plotly_dark')
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.write("#### Growth vs Performance Correlation")
    # Interactive scatter plot with JS hover effects
    fig2 = px.scatter(data, x='Growth', y='Performance', color='Category',
                     size='Performance', hover_data=['Region'])
    st.plotly_chart(fig2, use_container_width=True)

# 3. Data Inspection Table
with st.expander("Click to View Raw Data Source"):
    st.dataframe(data, use_container_width=True)
