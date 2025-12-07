# ✈️ Singapore Airlines Data Analytics System

### **CN6001 Enterprise Application & Cloud Computing – Coursework Project**

* **Team Leader:** Qian Zhu
* **Team Members:** Charles, Philippe, Ruitao He

---

## 📌 1. Project Overview

This project implements a **cloud-based data analytics platform for Singapore Airlines**, built using:

* **Python**
* **Streamlit Web Framework**
* **Modular Microservice Architecture**
* **Cloud Execution (Streamlit Cloud)**
* **Interactive Visual Analytics**

Because real SIA operational data is confidential, the system uses a synthetic dataset (`train.csv`) to simulate real airline operations and demonstrate end-to-end analytics.

This system:

* Runs fully online
* Requires no local installation
* Demonstrates enterprise cloud analytics concepts taught in **CN6001**

---

## 📌 2. System Features

The platform provides **four major analytics modules**:

### **1️⃣ Flight Performance Analytics**

* Fuel consumption trends
* Operational metrics visualisation
* Flight efficiency indicators
* Crew performance evaluation

### **2️⃣ Customer Experience Analytics**

* Passenger rating distribution
* Satisfaction modelling
* Customer segmentation
* Experience improvement insights

### **3️⃣ Risk & Scenario Simulation**

* Monte-Carlo risk modelling
* Delay simulation
* Operational uncertainty analysis

### **4️⃣ Cloud-Based Real-Time Analytics**

* Real-time processing
* Serverless cloud execution
* Scalability demonstration

Each module is fully interactive and implemented under the `pages/` directory using Streamlit’s multi-page design.

---

## 📌 3. System Architecture

```
sia_analytics_project/
│
├── main.py                    # Main Homepage (UI + CLI Router)
│
├── assets/
│   ├── train.csv              # Synthetic dataset
│   └── singapore_airlines_logo.png
│
├── pages/
│   ├── 1_Flight_Performance.py
│   ├── 2_Customer_Experience.py
│   ├── 3_Risk_Simulation.py
│   └── 4_Cloud_Analytics.py
│
├── services/
│   ├── data_service.py        # Unified data loading
│   └── simulation_service.py  # Risk & simulation utilities
│
└── requirements.txt
```

### ✔️ Clean Modular Design

* **main.py** – Front controller (routes UI / CLI)
* **services/** – Business logic layer
* **pages/** – Presentation layer
* **assets/** – Data + static files

This architecture ensures **clarity, scalability, and easy collaboration**.

---

## 📌 4. Installation & Running Locally

### **Step 1 — Clone the Repository**

```
git clone https://github.com/ashlllll/sia_analytics_project.git
cd sia_analytics_project
```

### **Step 2 — Install Dependencies**

```
pip install -r requirements.txt
```

---

## 📌 4.1 Running the Streamlit Web UI (Recommended)

Start the cloud dashboard:

```
streamlit run main.py
```

The application will automatically open at:

```
http://localhost:8501
```

This runs the **full interactive analytics system**.

---

## 📌 4.2 Optional: Run the Command-Line Interface (CLI)

The system includes a secondary **CLI mode** for terminal-based execution.

### Run the CLI:

```
python3 main.py cli
```

You will see:

```
===========================================
 Singapore Airlines Analytics System (CLI)
===========================================
1. Flight Performance Analytics
2. Customer Experience Analytics
3. Risk & Scenario Simulation
4. Cloud Analytics
5. Exit
```

### ⚠️ Important Notes

* Do **NOT** run the app using `python3 main.py`
  This will enter Streamlit **bare mode**, and the UI will not appear.
* Correct usage:

  * `streamlit run main.py` → Web UI
  * `python3 main.py cli` → CLI Mode

---

## 📌 5. Cloud Deployment (Streamlit Cloud)

This project satisfies the coursework requirement:

> “The system must run in a cloud environment (e.g., AWS, Google Colab, Streamlit Cloud).”

### Deployment Steps

1. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Click **New App**
3. Select the repo:

```
ashlllll/sia_analytics_project
```

4. Set **main.py** as the entry script
5. Deploy

Streamlit Cloud will generate a **public URL** for instructors and stakeholders.

---

## 📌 6. Team Members & Responsibilities

| Member                | Responsibility                                                                |
| --------------------- | ----------------------------------------------------------------------------- |
| **Qian Zhu (Leader)** | System architecture, main UI, CLI integration, GitHub setup, cloud deployment |
| **Charles**           | Flight Performance Analytics module                                           |
| **Ruitao He**         | Customer Experience Analytics module                                          |
| **Philippe**          | Risk Simulation & Cloud Analytics modules                                     |

---

## 📌 7. Dataset Information

The dataset used (`train.csv`) is **synthetic**, containing features that simulate:

* Fuel consumption
* Delay time
* Passenger satisfaction
* Onboard services
* Risk indicators
* Operational KPIs

This ensures no confidential airline data is used.

---

## 📌 8. Contribution Workflow

To develop your module:

```
git checkout -b feature/your_module
```

After editing:

```
git add .
git commit -m "Add my module"
git push origin feature/your_module
```

Then submit a Pull Request for review.

---

## 📌 9. License

This project is for **academic use only** under CN6001 course requirements.
Commercial usage is strictly prohibited.

---

## 📌 10. Acknowledgements

* Singapore Airlines (concept only)
* Streamlit Development Team
* NTU CN6001 Module Lecturers

---

⭐ **Thank you for reviewing our project!**
