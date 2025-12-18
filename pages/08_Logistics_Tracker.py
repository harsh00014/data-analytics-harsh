import streamlit as st
import plotly.express as px
import pandas as pd

st.title("📦 Logistics & Supply Chain")
st.write("Monitoring the efficiency of the delivery funnel.")

# Funnel Data
data = dict(
    number=[1000, 800, 600, 400, 200],
    stage=["Order Placed", "Processed", "Shipped", "In Transit", "Delivered"]
)
fig = px.funnel(data, x='number', y='stage', title="Delivery Conversion Funnel")
st.plotly_chart(fig, use_container_width=True)

st.info("💡 Insight: The largest drop-off occurs between 'Shipped' and 'In Transit'.")
