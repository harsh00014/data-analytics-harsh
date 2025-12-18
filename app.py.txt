import streamlit as st

st.set_page_config(page_title="Data Insights Pro", page_icon="📈", layout="wide")

# Sidebar for branding
st.sidebar.title("Navigation")
st.sidebar.info("Select a module above to explore the data.")

# Main Page Content
st.title("🚀 Data Analytics & Prediction Portal")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Welcome, Examiner!")
    st.write("""
    This project demonstrates a full-stack data science approach:
    * **Data Layer:** Python & Pandas for processing.
    * **Visual Layer:** JavaScript-powered interactive charts via Plotly.
    * **Intelligence Layer:** Machine Learning via Scikit-Learn.
    * **Deployment:** Continuous Integration/Deployment via GitHub & Streamlit.
    """)
    st.success("👈 Use the sidebar to navigate between 'Analytics' and 'Predictions'.")

with col2:
    st.metric(label="System Status", value="Online", delta="Active")
    st.metric(label="Data Refresh", value="Real-time")
