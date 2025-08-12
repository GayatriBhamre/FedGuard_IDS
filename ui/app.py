# Streamlit app entry point
import streamlit as st
from ui.Dashboard import show_dashboard

# Page Config
st.set_page_config(page_title="Privacy-Preserving IDS", layout="centered")

# Background Animation (simple gradient text)
st.markdown("""
    <div style='background:linear-gradient(to right,#111,#222);padding:50px;border-radius:10px;text-align:center'>
        <h1 style='color:#0ff;font-size:45px;'>Privacy-Preserving Intrusion Detection System</h1>
        <p style='color:white;font-size:20px;'>Secure. Detect. Defend. | Federated Learning-Based Approach</p>
    </div>
    """, unsafe_allow_html=True)

# Show dashboard
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🚀 Go to Dashboard"):
    show_dashboard()
