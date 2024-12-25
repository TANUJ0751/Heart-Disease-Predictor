import streamlit as st
from joblib import load
from sklearn.preprocessing import StandardScaler as sc


st.write("""
# Heart Disease Predictor Using Python and Machine Learning
This app uses a machine learning model to predict the likelihood of a patient having heart disease.
""")

model_options=["Random Forest","SVM","XG Boost","Logistic","Decision","KNeighbors"]
model_selection=st.sidebar.pills("Machine Learning Algorithm to Use :",model_options)
result=2
sex_options=["Male","Female"]
cp_options=['ASY' ,'ATA' ,'NAP' ,'TA']
recg=['LVH', 'Normal', 'ST']
ex=['Yes','No']
stsl=['Down' ,'Flat' ,'Up']
fbs=["N0","Yes"]
Age=st.sidebar.number_input("Enter Age of Patient :",min_value=0,max_value=100,step=1)
Sex=st.sidebar.pills("Select Sex of Patient :",sex_options)
ChestPain=st.sidebar.pills("Chest Pain :",cp_options)
FastingBS=st.sidebar.pills("Fasting BS :" ,fbs)
RestingBP=st.sidebar.number_input("Resting BP of Patient :",min_value=100,step=1)
Cholestrol=st.sidebar.number_input("Cholestrol of Patient",step=1)
RestingECG=st.sidebar.pills("Resting ECG of Patient",recg)
MaxHR=st.sidebar.number_input("Max Heart Rate of Patient",min_value=60,step=1)
Excercise=st.sidebar.pills("Excercise Angina of Patient :",ex)
Oldpeak=st.sidebar.number_input("Old Peak of the Patient :",min_value=-3.0,step=0.1)
ST_Slope=st.sidebar.pills("ST Slope of Patient :",stsl)
def preprocess_data(Sex,ChestPain,RestingECG,Excercise,FastingBS,ST_Slope):
    Sex=sex_options.index(Sex)
    ChestPain=cp_options.index(ChestPain)
    RestingECG=recg.index(RestingECG)
    Excercise=ex.index(Excercise)
    FastingBS=fbs.index(FastingBS)
    ST_Slope=stsl.index(ST_Slope)
    X = [[Age, Sex, ChestPain, RestingBP, Cholestrol, FastingBS, RestingECG, MaxHR, Excercise, Oldpeak, ST_Slope]]
    return X
if model_selection == "Random Forest":
    model = load("random_forest_model.joblib")
    X=preprocess_data(Sex,ChestPain,RestingECG,Excercise,FastingBS,ST_Slope)
    result=model.predict(X)
elif model_selection =="SVM":
      model = load("SVM_model.joblib")
      X=preprocess_data(Sex,ChestPain,RestingECG,Excercise,FastingBS,ST_Slope)
      result=model.predict(X)
elif model_selection=="XG Boost":
      model = load("XGB_model.joblib")
      X=preprocess_data(Sex,ChestPain,RestingECG,Excercise,FastingBS,ST_Slope)
      result=model.predict(X)
elif model_selection=="Logistic":
      model = load("logistic_Regression_model.joblib")
      X=preprocess_data(Sex,ChestPain,RestingECG,Excercise,FastingBS,ST_Slope)
      result=model.predict(X)
elif model_selection =="Decision":
      model = load("Decision_Tree_model.joblib")
      X=preprocess_data(Sex,ChestPain,RestingECG,Excercise,FastingBS,ST_Slope)
      result=model.predict(X)
elif model_selection=="KNeighbors":
      model = load("KNeighbors_model.joblib")
      X=preprocess_data(Sex,ChestPain,RestingECG,Excercise,FastingBS,ST_Slope)
      result=model.predict(X)
if result==[0]:
     st.write(" # The patient is not having a heart disease")
elif result==[1]:
     st.write(" # The patient is having a heart disease")
else:
    st.write("""# Enter All Inputs""")
