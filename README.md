# 🛡️ Privacy-Preserving Intrusion Detection System using Federated Learning

## 📌 Project Overview
**FedGuard IDS** is a *Privacy-Preserving Intrusion Detection System* that uses **Federated Learning (FL)** to collaboratively train an AI-based detection model **without directly sharing raw data between clients**.  

This ensures:
- **Data Privacy**
- **Distributed Model Training**
- **Efficient Intrusion Detection** across multiple organizations or nodes  

The project leverages the **Flower Framework (flwr)** for federated learning and supports real-time intrusion detection using the **NSL-KDD dataset**.

---

##  Features
- **Federated Learning-based IDS**
- **Privacy-preserving model training**
- **Local & global model updates**
- **Support for multiple clients**
- **Easy to set up and run locally**

---

##  Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/GayatriBhamre/FedGuard_IDS.git
cd FedGuard_IDS
```

### 2️⃣ Create Virtual Environment & Activate
```bash
# Create venv
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🖥️ Running the Project

### Step 1: Start the Server
```bash
cd server
python server.py
```

### Step 2: Start the Clients  
*(Run in separate terminals for each client)*
```bash
cd client
python client.py
```


### Step 3: Launch the UI
```bash
cd ui
python ui.py
```

---

## 👥 Contributors
- **Gayatri Nitin Bhamre**  
- **Nikita Bhausaheb Gholap**  
- **Jaymala Chatur Desale**  
- **Gauri Anil Gosavi**  
