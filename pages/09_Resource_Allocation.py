import streamlit as st
import plotly.express as px
import pandas as pd

st.title("🏗️ Resource Allocation")

# Hierarchical data
df = pd.DataFrame([
    dict(Project="Build A", Department="Design", Cost=400),
    dict(Project="Build A", Department="Legal", Cost=200),
    dict(Project="Build B", Department="Design", Cost=300),
    dict(Project="Build B", Department="Admin", Cost=500),
    dict(Project="Build C", Department="Legal", Cost=100),
    dict(Project="Build C", Department="Design", Cost=600),
])

st.write("#### Budget Split by Project and Department")
fig = px.sunburst(df, path=['Project', 'Department'], values='Cost',
                  color='Cost', color_continuous_scale='RdBu')
st.plotly_chart(fig, use_container_width=True)
