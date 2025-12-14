# ✈️ Singapore Airlines Data Analytics System

### CN6001 Enterprise Application & Cloud Computing – Coursework Project

- **Team Leader:** Qian Zhu  
- **Team Members:** Charles, Philippe, Ruitao He  

---

## 📌 1. Project Overview

This project implements a **cloud-based data analytics platform for Singapore Airlines (SIA)** using Python and Streamlit.  
The system demonstrates how an airline can leverage **enterprise application architecture and cloud computing concepts** to analyse operational performance, customer experience, and risk scenarios.

Because real Singapore Airlines operational data is confidential, the system uses a **synthetic dataset** (`train.csv`) to simulate realistic airline operations and demonstrate an end-to-end analytics pipeline.

Where certain operational metrics (e.g. fuel consumption) are not available in the dataset, **controlled simulation models** are applied using realistic assumptions. All simulated values are clearly documented and used strictly for academic purposes.

The system:

- Runs in a browser with an interactive **Streamlit dashboard**
- Supports a secondary **Command-Line Interface (CLI)** mode
- Demonstrates enterprise and cloud computing concepts taught in **CN6001**

---

## 📌 2. System Features

The platform provides **four major analytics modules**, all accessible from the main **Dashboard**.

### **1️⃣ Flight Performance Analytics**

- Flight distance distribution and operational profiling  
- Departure and arrival delay analysis  
- **Estimated fuel consumption trends (distance-based simulation)**  
- Crew service performance evaluation  

> **Note:**  
> Fuel consumption is **synthetically estimated** based on flight distance due to the absence of real fuel data.  
> This approach is implemented for academic demonstration and cost-awareness analytics only.

---

### **2️⃣ Customer Experience Analytics**

- Passenger satisfaction score distribution  
- Inflight and ground service rating analysis  
- Behaviour-based insights into passenger experience  
- Identification of service improvement opportunities  

---

### **3️⃣ Risk & Scenario Simulation**

- Monte-Carlo simulation of operational risks  
- Delay and disruption scenario modelling  
- Analysis of uncertainty and resilience in airline operations  

---

### **4️⃣ Cloud Analytics**

- Cloud-style data loading and processing demonstrations  
- Illustration of scalable analytics concepts  
- Discussion of batch vs real-time processing in cloud environments  

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
```

### ✔ Clean Modular Design

- **`Dashboard.py`** – Front controller  
  - Streamlit homepage with SIA-themed UI  
  - CLI menu router (`python3 Dashboard.py cli`)
- **`services/`** – Reusable business logic and shared computation
- **`pages/`** – Analytics modules supporting UI and CLI execution
- **`assets/`** – Synthetic dataset and static resources

This architecture supports **clarity, scalability, and team collaboration**, and aligns with enterprise application design principles.

---

## 📌 4. Installation & Local Setup

### **Step 1 — Clone the Repository**

```bash
git clone https://github.com/ashlllll/sia_analytics_project.git
cd sia_analytics_project
```

### **Step 2 — Create Virtual Environment (Optional)**

```bash
python3 -m venv venv
source venv/bin/activate      # macOS / Linux
# .\venv\Scripts\activate     # Windows (PowerShell)
```

### **Step 3 — Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## 📌 5. Running the System

### 5.1 Streamlit Web UI (Recommended)

```bash
streamlit run Dashboard.py
```

By default, Streamlit will open the application at:

```text
http://localhost:8501
```

The dashboard provides:

- A Singapore Airlines–styled homepage
- Navigation cards to all analytics modules
- Sidebar-based multi-page navigation

---

### 5.2 Command-Line Interface (CLI) Mode

The system also provides a **menu-driven CLI interface** for lightweight, non-visual analytics.

```bash
python3 Dashboard.py cli
```

Example menu:

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

The CLI mode is designed for:

- Quick operational summaries
- Numerical performance indicators
- Demonstration of menu-driven enterprise systems

> **Note:**  
> Modules that rely heavily on visualization (e.g. Risk Simulation and Cloud Analytics) are primarily accessed via the Streamlit UI.

---

## 📌 6. Cloud Deployment (Streamlit Cloud)

This project is designed to run in a **cloud environment** to meet CN6001 coursework requirements.

### Deployment Steps

1. Visit **https://streamlit.io/cloud**
2. Log in and click **“New app”**
3. Select the GitHub repository:
   ```text
   ashlllll/sia_analytics_project
   ```
4. Set **`Dashboard.py`** as the entry script
5. Click **Deploy**

Streamlit Cloud will automatically:

- Install dependencies from `requirements.txt`
- Build and deploy the application
- Provide a public URL for demonstration and assessment

---

## 📌 7. Dataset

The system uses a **synthetic dataset**:

- **File:** `assets/train.csv`
- **Purpose:** Academic simulation only

The dataset simulates:

- Passenger profiles
- Service rating attributes (1–5 scale)
- Satisfaction labels
- Flight distances and delays
- Operational performance indicators

### Dataset Characteristics

- Flight distance distribution is **right-skewed**
- Sparse values beyond **4000–5000 km** represent long-haul flight caps
- Clustering near upper bounds reflects **controlled dataset generation**, not data quality issues

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

```bash
git checkout -b feature/your_module_name
git add .
git commit -m "Implement <feature/module name>"
git push origin feature/your_module_name
```

Create a **Pull Request** to merge changes into the main branch.

---

## 📌 10. License

This project is developed **exclusively for academic use** under the  
**CN6001 Enterprise Application & Cloud Computing** module.

- Commercial use is **not permitted**
- All trademarks and brand references (e.g. Singapore Airlines) are used for **educational demonstration only**

---

## 📌 11. Acknowledgements

- Singapore Airlines (conceptual inspiration only)
- Streamlit open-source community

---

⭐ **Thank you for reviewing our project.**

This system demonstrates how a modern airline can leverage **enterprise architecture, cloud computing, and data analytics** to support operational performance, customer experience, and risk-aware decision-making.
