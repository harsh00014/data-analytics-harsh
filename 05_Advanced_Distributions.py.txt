import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd

st.title("🧪 Statistical Distributions")

# Generate data for groups
df = pd.DataFrame({
    'Batch': np.repeat(['Batch A', 'Batch B', 'Batch C'], 50),
    'Score': np.append(np.random.normal(70, 10, 50), 
                      [np.random.normal(60, 15, 50), np.random.normal(80, 5, 50)])
})

col1, col2 = st.columns(2)

with col1:
    st.write("#### Data Spread (Box Plot)")
    fig1 = px.box(df, x="Batch", y="Score", color="Batch")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.write("#### Composition (Pie Chart)")
    # Sample proportions
    pie_df = pd.DataFrame({'Label': ['Success', 'Fail', 'Pending'], 'Value': [75, 15, 10]})
    fig2 = px.pie(pie_df, values='Value', names='Label', hole=0.4)
    st.plotly_chart(fig2, use_container_width=True)
