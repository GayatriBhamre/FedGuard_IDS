# 🛡️ Privacy-Preserving Intrusion Detection System using Federated Learning (FedGuard IDS)

## 📌 Project Overview
FedGuard IDS is a **Privacy-Preserving Intrusion Detection System** that uses **Federated Learning (FL)** to collaboratively train an AI-based detection model without directly sharing raw data between clients.  
This approach ensures **data privacy**, **distributed model training**, and **efficient intrusion detection** across multiple organizations or nodes.  

The project leverages **Flower Framework (flwr)** for federated learning and supports real-time intrusion detection based on the **NSL-KDD dataset**.

---

## 🚀 Features
- **Federated Learning-based IDS** 
- **Privacy-preserving model training**
- **Local & global model updates**
- **Support for multiple clients**
- **Easy to set up and run locally**

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

git clone https://github.com/GayatriBhamre/FedGuard_IDS.git
cd FedGuard_IDS

2️⃣ Create Virtual Environment & Activate
  # Create venv
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

## Running the Project
Step 1: Start the Server
cd server
python server.py

Step 2: Start the Clients
cd client
python client.py
 run all 4 clients 

 Step 3: Launch the UI
 cd ui
python ui.py



👥 Contributors
Gayatri Nitin Bhamre

Nikita Bhausaheb Gholap

Jaymala Chatur Desale

Gauri Anil Gosavi

