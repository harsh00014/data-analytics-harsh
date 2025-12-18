import streamlit as st

st.title("🧠 Research Methodology & Logic")

st.markdown("""
### 1. Data Ingestion Layer
The application utilizes **Synthetic Data Generation** via NumPy and Pandas. This approach was chosen to demonstrate system capabilities without compromising real-world data privacy. 

### 2. Processing Framework
* **Vectorization:** We use NumPy's vectorized operations for high-speed mathematical calculations.
* **Data Cleaning:** Pandas is used to handle missing values and normalize data formats before visualization.

### 3. Visualization Engine
The frontend integrates **Plotly.js**. Unlike static libraries, this allows for a 'Client-Side' rendering experience, where the browser handles zooming and filtering, reducing the load on our Python server.

### 4. Machine Learning Implementation
We implemented a **Linear Regression model** using Scikit-Learn. The model follows the standard ML pipeline:
1. Feature selection (Input Variables).
2. Model Training (Fitting the line).
3. Inference (Generating real-time predictions based on user-slider input).
""")

st.info("Technical Note: The system architecture follows a 'Decoupled' design, separating data logic from the presentation layer.")
