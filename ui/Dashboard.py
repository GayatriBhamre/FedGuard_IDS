import streamlit as st

def show_dashboard():
    st.title("🛡️ Federated IDS Dashboard")
    st.success("Real-Time Threat Detection Active ✅")
    st.metric(label="Detected Attacks", value="53", delta="+12")
    st.metric(label="False Positives", value="3")
    st.metric(label="Global Model Accuracy", value="97.2%")
