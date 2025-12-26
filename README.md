# 🚗 Vehicle Emissions: Physics (CFD) + Data Science (ML)

This project is an end-to-end engineering workflow. I wanted to bridge the gap between **hardware simulation** (how gas actually moves) and **software prediction** (predicting CO2 based on vehicle specs). 

### 🔗 [Check out the Live Predictor App here!](https://vehicle-emission-analysis-ml-cfd-ns9ha9hyzu7kramsv8tmjt.streamlit.app/)

---

## 🛠️ The Tech Stack
* **Physics:** ANSYS Fluent 2025 R2 (CFD)
* **Machine Learning:** Python (Scikit-learn, Pandas)
* **Deployment:** Streamlit
* **Dataset:** Vehicle CO2 Emissions (Kaggle)

---

## 🧠 Part 1: Predictive Modeling (ML)
I built a **Random Forest Regressor** to predict CO2 emissions. 

* **The Struggle:** The raw data was noisy. I had to use the **Interquartile Range (IQR) method** to strip out outliers that were skewing the results. 
* **Results:** Hit **97.23% accuracy** across 1,000 estimators. 
* **Features:** Engine Displacement, Cylinders, and Fuel Consumption (City/Hwy/Combined).

## 💨 Part 2: Thermal Simulation (CFD)
I modeled a **BMW 2.0L Exhaust Manifold** to understand the "why" behind the heat.

* **Boundary Conditions:** 3 inlets at **925 K** (standard engine temp) and **10 m/s** velocity.
* **The Math:** Mass flow rate stabilized at **0.169 kg/s**. I verified the mass balance manually to make sure the simulation wasn't "leaking" air.
* **Convergence:** Took about 200 iterations for the velocity and energy residuals to go flat.

---

## 🧪 Chemical Engineering Lens
I treated the manifold as a **Transport Phenomena** problem:
1.  **Fluid Mechanics:** Tracked pressure drops and velocity spikes (maxing at 57 m/s). 🌊
2.  **Heat Transfer:** Visualized the thermal gradient from the 925 K source through the manifold body. 🌡️
3.  **Mass Balance:** Verified $Inlets = Outlet$ to ensure physical conservation. ⚖️

---

## 📊 Visuals & Results

### 🔗 [Check out the PDF!](https://drive.google.com/file/d/1lRNSuAa8AQotasq1_9pgicawBCcaUUlF/view?usp=drivesdk)


## 💡 What I actually learned (The "Real" Version)
* **ANSYS Meshing:** I spent 80% of my time fixing the mesh and 20% actually running the simulation. If the mesh is bad, the physics is garbage. 🏗️
* **Data Cleaning > Hyperparameters:** You can tune a model forever, but removing the outliers with IQR was what actually fixed my accuracy. 🧹
* **Full Picture:** Engineering isn't just one niche. Combining CFD with ML gives you a much better "macro" view of how a vehicle performs.

---

## ⚙️ Setup & Installation
1. `git clone https://github.com/YourUsername/YourRepo.git`
2. `pip install -r requirements.txt`
3. `streamlit run Emission_app.py`
