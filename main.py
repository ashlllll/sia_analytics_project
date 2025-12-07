# Author: Qian Zhu
# Main entry page for Singapore Airlines Analytics System

import streamlit as st
from PIL import Image

# Page config (title + layout)
st.set_page_config(
    page_title="SIA Analytics Dashboard",
    layout="wide"
)

# Main Title
st.title("Singapore Airlines Data Analytics System")
st.subheader("Enterprise Cloud-Based Analytics Platform")

# SIA Logo
logo = Image.open("assets/singapore_airlines_logo.png")
st.image(logo, width=200)


st.markdown("""
Welcome to the **Singapore Airlines Analytics System**, built using:

- **Python**
- **Streamlit Web Framework**
- **Cloud Execution**
- **Data-Driven Analytics**

Use the **left sidebar** to navigate between modules.
""")

st.markdown("---")

st.markdown("""
### 📊 Available Modules  

1. **Flight Performance Analytics**  
2. **Customer Experience Analytics**  
3. **Risk & Scenario Simulation**  
4. **Cloud-Enabled Real-Time Analytics**  

Each module is accessible from the navigation sidebar.
""")
