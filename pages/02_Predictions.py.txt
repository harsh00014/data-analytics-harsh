import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import plotly.graph_objects as go

st.title("🤖 Predictive Engine")
st.write("Adjust the parameters to see how the Machine Learning model predicts results.")

# 1. Create Linear Data
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1) # Hours
y = np.array([40, 45, 52, 58, 70, 72, 81, 85, 93, 97])       # Score

model = LinearRegression()
model.fit(X, y)

# 2. User Input
user_val = st.slider("Select Study Hours (Input Variable):", 1, 15, 5)
prediction = model.predict([[user_val]])[0]

# 3. Visualize Prediction
st.markdown(f"### Predicted Score: `{prediction:.2f}%`")

# Create a trend line chart
fig = go.Figure()
fig.add_trace(go.Scatter(x=X.flatten(), y=y, mode='markers', name='Actual Data'))
fig.add_trace(go.Scatter(x=[user_val], y=[prediction], mode='markers', 
                         marker=dict(size=15, color='red'), name='Your Prediction'))
fig.update_layout(title="Linear Regression Trend", template="plotly_dark")
st.plotly_chart(fig, use_container_width=True)
