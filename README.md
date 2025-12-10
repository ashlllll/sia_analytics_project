````markdown
# ✈️ Singapore Airlines Data Analytics System

### CN6001 Enterprise Application & Cloud Computing – Coursework Project

- **Team Leader:** Qian Zhu  
- **Team Members:** Charles, Philippe, Ruitao He  

---

## 📌 1. Project Overview

This project implements a **cloud-based data analytics platform for Singapore Airlines (SIA)**, built using:

- **Python**
- **Streamlit Web Framework**
- **Modular, service-oriented architecture**
- **Cloud execution via Streamlit Cloud**
- **Interactive visual analytics dashboards**

Because real SIA operational data is confidential, the system uses a **synthetic dataset** (`train.csv`) to simulate realistic airline operations and demonstrate an end-to-end analytics pipeline.

The system:

- Runs in a browser with an interactive Streamlit UI  
- Supports a secondary Command-Line Interface (CLI) mode  
- Demonstrates key enterprise/cloud concepts taught in **CN6001**

---

## 📌 2. System Features

The platform provides **four major analytics modules**, all accessible from the main **Dashboard**:

### **1️⃣ Flight Performance Analytics**

- Fuel consumption trends  
- Delay and operational performance metrics  
- Flight efficiency indicators  
- Crew performance evaluation  

### **2️⃣ Customer Experience Analytics**

- Passenger satisfaction score distribution  
- Service rating analysis  
- Behaviour-based segmentation  
- Experience improvement insights  

### **3️⃣ Risk & Scenario Simulation**

- Monte-Carlo risk modelling  
- Delay and disruption simulation  
- Operational uncertainty analysis  

### **4️⃣ Cloud Analytics**

- Cloud-style data processing demonstrations  
- Scalable analytics concepts (batch vs. real-time)  
- High-level cloud architecture illustration  

Each module is implemented as a separate Streamlit page under the `pages/` directory.

---

## 📌 3. System Architecture

```text
sia_analytics_project/
│
├── Dashboard.py                     # Main entry (Homepage UI + CLI router)
│
├── assets/
│   ├── train.csv                    # Synthetic dataset
│   └── singapore_airlines_logo.png  # Branding asset (optional)
│
├── pages/
│   ├── Module1_Flight_Performance.py
│   ├── Module2_Customer_Experience.py
│   ├── Module3_Risk_Simulation.py
│   └── Module4_Cloud_Analytics.py
│
├── services/
│   ├── ui_service.py                # Global SIA-themed UI styles & components
│   └── data_service.py              # Shared data loading & helper utilities
│
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
````

### ✔ Clean Modular Design

* **`Dashboard.py`** – Front controller:

  * Streamlit homepage (SIA-styled dashboard)
  * CLI menu router (`python3 Dashboard.py cli`)
* **`services/`** – Reusable business logic and UI helpers
* **`pages/`** – Per-module analytics pages (Streamlit multi-page design)
* **`assets/`** – Dataset and static assets

This architecture supports **clarity, scalability, and team collaboration**.

---

## 📌 4. Installation & Local Setup

### **Step 1 — Clone the Repository**

```bash
git clone https://github.com/ashlllll/sia_analytics_project.git
cd sia_analytics_project
```

### **Step 2 — Create Virtual Environment (optional but recommended)**

```bash
python3 -m venv venv
source venv/bin/activate      # On macOS / Linux
# .\venv\Scripts\activate     # On Windows (PowerShell)
```

### **Step 3 — Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## 📌 5. Running the System

### 5.1 Streamlit Web UI (Recommended)

To launch the full interactive dashboard:

```bash
streamlit run Dashboard.py
```

By default, Streamlit will open the app in your browser at:

```text
http://localhost:8501
```

You will see:

* A SIA-branded hero banner
* Navigation cards to all analytics modules
* Streamlit sidebar listing: `Dashboard`, `Module1`, `Module2`, `Module3`, `Module4`

---

### 5.2 Command-Line Interface (CLI) Mode

The system also provides a terminal-based analytics menu.

Run:

```bash
python3 Dashboard.py cli
```

You will see a menu similar to:

```text
===========================================
 Singapore Airlines Analytics System (CLI)
===========================================

1. Flight Performance Analytics
2. Customer Experience Analytics
3. Risk & Scenario Simulation
4. Cloud Analytics
5. Exit
```

You can select a module by entering `1–5`.

#### Important Notes

* Use:

  * `streamlit run Dashboard.py` → **Web UI mode**
  * `python3 Dashboard.py cli` → **CLI mode**
* Do **not** run `python3 Dashboard.py` without `cli` in this project, as the Streamlit UI should always be started via `streamlit run`.

---

## 📌 6. Cloud Deployment (Streamlit Cloud)

This project is designed to run in a **cloud environment** to meet CN6001 coursework requirements.

### Deployment Steps

1. Go to **[https://streamlit.io/cloud](https://streamlit.io/cloud)**

2. Log in and click **“New app”**

3. Select the GitHub repository:

   ```text
   ashlllll/sia_analytics_project
   ```

4. Set **`Dashboard.py`** as the entry script

5. Click **Deploy**

Streamlit Cloud will:

* Build the app from `requirements.txt`
* Host the dashboard
* Provide a public URL for instructors and stakeholders

---

## 📌 7. Dataset

The system uses a **synthetic dataset**:

* File: `assets/train.csv`
* Content simulates:

  * Passenger profiles
  * Service rating attributes (1–5 scale)
  * Satisfaction labels
  * Flight distance and delays
  * Operational performance indicators

The dataset is purely for academic purposes and does **not** contain real Singapore Airlines data.

---

## 📌 8. Team & Responsibilities

| Member                | Responsibility                                                            |
| --------------------- | ------------------------------------------------------------------------- |
| **Qian Zhu (Leader)** | System architecture, Dashboard design, CLI integration, Git & cloud setup |
| **Charles**           | Module 1 – Flight Performance Analytics                                   |
| **Ruitao He**         | Module 2 – Customer Experience Analytics & UI refinement                  |
| **Philippe**          | Module 3 – Risk Simulation & Module 4 – Cloud Analytics                   |

---

## 📌 9. Development Workflow

To work on a feature or module:

```bash
git checkout -b feature/your_module_name
```

After changes:

```bash
git add .
git commit -m "Implement <feature/module name>"
git push origin feature/your_module_name
```

Then open a **Pull Request** for code review and merging into the main branch.

---

## 📌 10. License

This project is developed **exclusively for academic use** under the CN6001 Enterprise Application & Cloud Computing module.

* Commercial use is **not permitted**.
* All trademarks and brand references (e.g., Singapore Airlines) are used for educational demonstration only.

---

## 📌 11. Acknowledgements

* Singapore Airlines (conceptual inspiration only)
* Streamlit open-source community
---

⭐ **Thank you for reviewing our project.**
The system demonstrates how a modern airline can leverage cloud-based analytics for performance, customer experience, and risk management.

```
