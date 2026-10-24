Titanic Survival Prediction

Overview

This project uses machine learning to predict whether a passenger survived the Titanic disaster. It includes data cleaning, exploratory visualization, model training, and evaluation using Python.

Objectives

- Explore and clean the Titanic dataset.
- Handle missing values.
- Encode categorical variables.
- Visualize passenger survival data.
- Train and compare classification models.

Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn
- Jupyter Notebook

Models and Results

The dataset was split into training and testing sets using an 80/20 split.

Model| Test Accuracy
Logistic Regression| 80.45%
Random Forest| 82.12%

Random Forest achieved higher accuracy on this test split. Additional validation would be needed to determine whether it performs consistently better.

Project Workflow

1. Data loading and exploration
2. Missing-value handling
3. Categorical encoding
4. Data visualization
5. Training and testing split
6. Logistic Regression training and evaluation
7. Random Forest training and evaluation
8. Model comparison

Project Files

- "titan_project.ipynb" — Jupyter Notebook containing the code and analysis
- "cleaned_titanic.csv" — cleaned dataset
- "titanic_survival_model.pkl" — trained Logistic Regression model
- "titanic_random_forest_model.pkl" — trained Random Forest model

Future Improvements

- Evaluate models using cross-validation.
- Tune model hyperparameters.
- Compare precision, recall, and F1-score.
- Explore additional visualizations and feature importance.

Disclaimer

This project is for educational purposes. Model predictions are not guaranteed to be accurate for individual passengers.
