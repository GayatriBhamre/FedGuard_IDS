import streamlit as st
import numpy as np
import os

st.set_page_config(page_title="FedGuard IDS", layout="centered")

st.title("FedGuard: Federated Intrusion Detection System")
st.markdown(" Distributed FL IDS using NSL-KDD dataset")

if st.button("Show Preprocessed Client Data Info"):
    client_dir = "data/clients"
    if os.path.exists(client_dir):
        for i in range(1, 5):
            file_path = f"{client_dir}/client_{i}.npz"
            if os.path.exists(file_path):
                data = np.load(file_path)
                st.write(f"**Client {i}** ➤ Samples: {len(data['X'])}, Features: {data['X'].shape[1]}")
    else:
        st.error("Preprocessed data not found!")

st.markdown("---")
st.info("Start the server and clients separately to simulate training.")
