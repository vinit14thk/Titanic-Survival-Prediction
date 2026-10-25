import streamlit as st
import pandas as pd
import pickle

# Load the trained Random Forest model
with open("titanic_random_forest_model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(
    page_title="Titanic Survival Predictor",
    page_icon="🚢",
    layout="centered"
)

st.title("🚢 Titanic Survival Prediction")
st.write(
    "Enter passenger details to predict whether the passenger "
    "would have survived according to our trained model."
)

st.subheader("Passenger Details")

pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ["Female", "Male"])
age = st.slider("Age", 0, 80, 25)
sibsp = st.number_input(
    "Siblings / Spouses Aboard", min_value=0, max_value=10, value=0
)
parch = st.number_input(
    "Parents / Children Aboard", min_value=0, max_value=10, value=0
)
fare = st.number_input(
    "Ticket Fare", min_value=0.0, max_value=600.0, value=32.0
)
embarked = st.selectbox(
    "Port of Embarkation",
    ["Cherbourg (C)", "Queenstown (Q)", "Southampton (S)"]
)

if st.button("Predict Survival"):
    sex_value = 0 if sex == "Female" else 1

    embarked_c = 1 if embarked == "Cherbourg (C)" else 0
    embarked_q = 1 if embarked == "Queenstown (Q)" else 0
    embarked_s = 1 if embarked == "Southampton (S)" else 0

    passenger = pd.DataFrame([{
        "Pclass": pclass,
        "Sex": sex_value,
        "Age": age,
        "SibSp": sibsp,
        "Parch": parch,
        "Fare": fare,
        "Embarked_C": embarked_c,
        "Embarked_Q": embarked_q,
        "Embarked_S": embarked_s
    }])

    prediction = model.predict(passenger)[0]

    if prediction == 1:
        st.success("Prediction: The passenger is predicted to survive.")
    else:
        st.error("Prediction: The passenger is predicted not to survive.")

    st.caption(
        "This is a machine-learning prediction, not a guarantee "
        "of what would happen."
    )