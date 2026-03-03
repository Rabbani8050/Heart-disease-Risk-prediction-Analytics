#❤️ Heart Disease Risk Analytics

Machine Learning & Healthcare Data Analytics Project

#📌 Project Overview

Heart Disease Risk Analytics is an end-to-end healthcare analytics project that applies machine learning, exploratory data analysis, and interactive visualization to predict heart disease risk and support data-driven clinical decision-making.
The system focuses on risk prediction, population-level insights, and explainable analytics, making it suitable for real-world healthcare applications.

#🎯 Project Objectives

Predict heart disease risk using supervised machine learning models
Perform population-level exploratory data analysis (EDA)
Categorize patients into Low, Moderate, and High risk groups
Provide clinical decision support through interpretable analytics
Deliver insights via an interactive Streamlit dashboard

#📂 Dataset Description

The dataset contains demographic, lifestyle, and clinical attributes, including:
Age, gender, height, weight (BMI derived)
Blood pressure, cholesterol, blood sugar
Smoking status, physical activity, diet, stress level
Medical history (diabetes, hypertension, family history)
Target variable: Heart Disease (0 = No, 1 = Yes)
The dataset is well-suited for supervised classification and healthcare analytics.

#🧹 Data Preprocessing

Key preprocessing steps performed:
Encoding categorical variables into numerical format
Feature scaling using StandardScaler
Handling missing and invalid values
Train–test data preparation
These steps ensured data quality, model stability, and reliable predictions.

#🔍 Exploratory Data Analysis (EDA)

EDA was conducted using Pandas, Matplotlib, and Seaborn, including:
Heart disease prevalence analysis
Age vs heart disease distribution
Smoking status impact analysis
Feature correlation heatmaps
EDA helped uncover key risk patterns and relationships within the population.

#⚙️ Feature Engineering

BMI was derived from height and weight to capture obesity-related risk
Lifestyle and clinical indicators were encoded numerically
Feature selection focused on clinically relevant predictors to improve interpretability and performance

#🤖 Machine Learning Models

Two supervised learning models were implemented:
Logistic Regression
Provides probability-based risk prediction
Highly interpretable and suitable for clinical decision support
Outputs probabilities used for risk stratification
Random Forest Classifier
Ensemble model capturing non-linear relationships
Improves predictive accuracy and robustness
Provides feature importance for explainability

#📊 Model Evaluation

Model performance was evaluated using:
Accuracy, Precision, Recall, F1-score
ROC-AUC score
Probability-based risk thresholds
Instead of relying only on accuracy, predictions were categorized into:
Low Risk
Moderate Risk
High Risk
This approach aligns with clinical decision-making practices.

#🧠 Explainable AI (XAI)

Explainable AI techniques were applied to improve transparency:
Feature importance extracted from the Random Forest model
Visualization of top contributing risk factors
XAI ensures trust, accountability, and interpretability, which are critical in healthcare analytics.

#🖥️ Streamlit Application Architecture

The Streamlit application integrates:
User input collection for patient attributes
Real-time ML inference using trained models
Risk visualization with probability metrics and risk categories
Population-level analytics through interactive charts and filters

🔍 Authentication, email, and appointment booking modules were intentionally excluded from this report to maintain focus on analytics and ML.

📈 Visualization & Insights

Key visual components include:
Risk probability metrics
Heart disease distribution chart
Smoking vs heart disease analysis
Feature correlation heatmaps
These visuals support both clinical interpretation and management-level insights.

#💼 Business & Clinical Impact

Enables early detection of high-risk patients
Supports preventive care and clinical decision-making
Demonstrates scalable AI adoption in healthcare analytics
Highlights data-driven strategies to reduce long-term treatment costs

#🚀 Future Enhancements

Advanced models such as XGBoost
Explainability using SHAP values
Integration with real-time hospital systems and EHR data

#🛠️ Tools & Technologies

Programming: Python
Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
ML Models: Logistic Regression, Random Forest
Visualization: Streamlit, Power BI
Version Control: Git & GitHub

#📌 Author

Rabbani Holi
Data Analyst | Junior Data Scientist
Healthcare Analytics & Machine Learning Projects
