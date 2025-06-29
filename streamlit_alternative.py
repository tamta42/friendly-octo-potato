"""
Streamlit Alternative - Similar functionality to Taipy but often works better
Install with: pip install streamlit
Run with: streamlit run streamlit_alternative.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Page title
st.title("🎉 Interactive Data App")
st.markdown("Similar to Taipy but using Streamlit")

# Text input
name = st.text_input("Enter your name:", value="World")
st.write(f"Hello **{name}**!")

# Slider
slider_value = st.slider("Select a value:", 0, 100, 50)
st.write(f"Current value: **{slider_value}**")

# Generate data based on slider
np.random.seed(slider_value)
data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': np.random.randint(1000, 2500, 6),
    'Expenses': np.random.randint(500, 1500, 6)
})

# Chart
fig = px.bar(data, x='Month', y=['Sales', 'Expenses'], 
            title='Monthly Sales vs Expenses',
            barmode='group')
st.plotly_chart(fig)

# Data table
st.subheader("📋 Data Table")
st.dataframe(data)

st.markdown("""
---
### 🎮 Try This:
1. **Change your name** in the text field above
2. **Move the slider** to see the chart update with new data
3. **Everything updates automatically!**

*This shows similar interactive capabilities to Taipy*
""")