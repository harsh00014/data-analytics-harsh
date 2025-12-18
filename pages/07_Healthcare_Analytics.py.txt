import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("🏥 Healthcare Data Insights")
st.write("Analysis of patient recovery rates and vital sign distributions.")

# Create medical data
df = pd.DataFrame({
    'Age': np.random.randint(20, 80, 100),
    'Recovery_Rate': np.random.uniform(60, 99, 100),
    'Treatment': np.random.choice(['Type A', 'Type B', 'Type C'], 100)
})

col1, col2 = st.columns(2)

with col1:
    st.write("#### Age vs Recovery Correlation")
    fig1 = px.density_heatmap(df, x="Age", y="Recovery_Rate", nbinsx=10, nbinsy=10, color_continuous_scale="Viridis")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.write("#### Treatment Effectiveness")
    fig2 = px.histogram(df, x="Recovery_Rate", color="Treatment", marginal="box")
    st.plotly_chart(fig2, use_container_width=True)
