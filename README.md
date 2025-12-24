# Vehicle CO2 Emission Analysis: A Dual CFD & Machine Learning Approach

This project integrates **Computational Flow Dynamics (CFD)** and **Supervised Machine Learning** to analyze and predict vehicle CO2 emissions. It demonstrates a complete engineering workflow by combining high-temperature thermal simulations with predictive data science.

## 🚀 Live Demo
Access the interactive prediction app here: **[https://vehicle-emission-analysis-ml-cfd-ns9ha9hyzu7kramsv8tmjt.streamlit.app/]**

---

## 🛠️ Project Overview

### 1. Predictive Modeling (Machine Learning)
* **Algorithm**: Random Forest Regressor (1,000 Estimators).
* **Performance**: Achieved an accuracy of **97.23%**.
* **Features**: Engine Size, Cylinders, Fuel Consumption (City, Highway, Combined).
* **Deployment**: Interactive UI built using **Streamlit** for real-time predictions.

### 2. Thermal Analysis (CFD)
* **Software**: ANSYS Fluent 2025 R2 Student Edition.
* **Boundary Conditions**:
    * **Inlet Velocity**: 10 m/s.
    * **Inlet Temperature**: 925 K (BMW 2.0L Standard).
    * **Outlet**: Pressure-outlet (0 Gauge Pressure).
* **Key Results**:
    * **Mass Flow Conservation**: Net mass flow rate achieved is **0.1690188 kg/s**.
    * **Convergence**: Solution stabilized at 200 iterations with flat residuals.

---

## 🧪 Chemical Engineering Perspective
Applied core concepts of **Transport Phenomena**:
* **Fluid Mechanics**: Analyzed pressure drops and velocity magnitudes up to 57 m/s.
* **Heat Transfer**: Modeled thermal energy distribution across the manifold.
* **Mass Balance**: Verified conservation between 3 inlets and 1 outlet.

---

## 📈 Results & Visuals

### 1. Convergence Plot
The residuals for energy and velocity stabilized perfectly, ensuring a reliable numerical solution.


### 2. Temperature Contour
Visualized the thermal gradient from the 925 K inlets through the manifold body.


### 3. Velocity Pathlines
Pathlines illustrate how gases from the three inlets mix and exit through the single outlet.


---

## 🔧 Installation
1. Clone the repo: `git clone https://github.com/YourUsername/YourRepo.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `streamlit run Emission_app.py`

## 💡 Key Learnings
* Overcame the steep learning curve of **ANSYS mesh generation**.
* Handled outliers in the Kaggle dataset using **IQR** for better model reliability.
* Successfully bridged the gap between a hardware simulation (CFD) and software prediction (ML).
