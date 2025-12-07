#Author: Charles
# Date:
# Description:
# Flight Performance Analytics page for Singapore Airlines project.
# This page analyzes operational metrics such as fuel usage and punctuality.

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Page Title
st.title("✈️ Flight Performance Analytics")

st.write("""
This section provides flight operational metrics including:
- Fuel efficiency  
- On-time performance  
- Aircraft utilization
- Crew efficiency   
""")

