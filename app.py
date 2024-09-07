import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Change Name & Logo
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️")

# Hiding Streamlit ad-ons
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Loading the saved models
diabetes_model = pickle.load(open('Models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('Models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('Models/parkinsons_model.sav', 'rb'))
lungs_disease_model = pickle.load(open('Models/lungs_disease_model.sav', 'rb'))
thyroid_model = pickle.load(open('Models/Thyroid_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 'Lungs Cancer Prediction', 'Hypo-Thyroid Prediction'],
                           icons=['activity', 'heart', 'person', 'brightness-high', 'droplet-half'],
                           default_index=0)

# Function to safely convert input to float
def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return None

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = convert_to_float(st.text_input('Number of Pregnancies'))
    with col2:
        Glucose = convert_to_float(st.text_input('Glucose Level'))
    with col3:
        BloodPressure = convert_to_float(st.text_input('Blood Pressure value'))
    with col1:
        SkinThickness = convert_to_float(st.text_input('Skin Thickness value'))
    with col2:
        Insulin = convert_to_float(st.text_input('Insulin Level'))
    with col3:
        BMI = convert_to_float(st.text_input('BMI value'))
    with col1:
        DiabetesPedigreeFunction = convert_to_float(st.text_input('Diabetes Pedigree Function value'))
    with col2:
        Age = convert_to_float(st.text_input('Age of the Person'))

    if st.button('Diabetes Test Result'):
        if all(v is not None for v in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]):
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
            st.success(diab_diagnosis)
        else:
            st.error("Please provide valid input values.")

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        age = convert_to_float(st.text_input('Age'))
    with col2:
        sex = convert_to_float(st.text_input('Sex'))
    with col3:
        cp = convert_to_float(st.text_input('Chest Pain types'))
    with col1:
        trestbps = convert_to_float(st.text_input('Resting Blood Pressure'))
    with col2:
        chol = convert_to_float(st.text_input('Serum Cholestoral in mg/dl'))
    with col3:
        fbs = convert_to_float(st.text_input('Fasting Blood Sugar > 120 mg/dl'))
    with col1:
        restecg = convert_to_float(st.text_input('Resting Electrocardiographic results'))
    with col2:
        thalach = convert_to_float(st.text_input('Maximum Heart Rate achieved'))
    with col3:
        exang = convert_to_float(st.text_input('Exercise Induced Angina'))
    with col1:
        oldpeak = convert_to_float(st.text_input('ST depression induced by exercise'))
    with col2:
        slope = convert_to_float(st.text_input('Slope of the peak exercise ST segment'))
    with col3:
        ca = convert_to_float(st.text_input('Major vessels colored by flourosopy'))
    with col1:
        thal = convert_to_float(st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect'))

    if st.button('Heart Disease Test Result'):
        if all(v is not None for v in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]):
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'
            st.success(heart_diagnosis)
        else:
            st.error("Please provide valid input values.")

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = convert_to_float(st.text_input('MDVP:Fo(Hz)'))
    with col2:
        fhi = convert_to_float(st.text_input('MDVP:Fhi(Hz)'))
    with col3:
        flo = convert_to_float(st.text_input('MDVP:Flo(Hz)'))
    with col4:
        Jitter_percent = convert_to_float(st.text_input('MDVP:Jitter(%)'))
    with col5:
        Jitter_Abs = convert_to_float(st.text_input('MDVP:Jitter(Abs)'))
    with col1:
        RAP = convert_to_float(st.text_input('MDVP:RAP'))
    with col2:
        PPQ = convert_to_float(st.text_input('MDVP:PPQ'))
    with col3:
        DDP = convert_to_float(st.text_input('Jitter:DDP'))
    with col4:
        Shimmer = convert_to_float(st.text_input('MDVP:Shimmer'))
    with col5:
        Shimmer_dB = convert_to_float(st.text_input('MDVP:Shimmer(dB)'))
    with col1:
        APQ3 = convert_to_float(st.text_input('Shimmer:APQ3'))
    with col2:
        APQ5 = convert_to_float(st.text_input('Shimmer:APQ5'))
    with col3:
        APQ = convert_to_float(st.text_input('MDVP:APQ'))
    with col4:
        DDA = convert_to_float(st.text_input('Shimmer:DDA'))
    with col5:
        NHR = convert_to_float(st.text_input('NHR'))
    with col1:
        HNR = convert_to_float(st.text_input('HNR'))
    with col2:
        RPDE = convert_to_float(st.text_input('RPDE'))
    with col3:
        DFA = convert_to_float(st.text_input('DFA'))
    with col4:
        spread1 = convert_to_float(st.text_input('spread1'))
    with col5:
        spread2 = convert_to_float(st.text_input('spread2'))
    with col1:
        D2 = convert_to_float(st.text_input('D2'))
    with col2:
        PPE = convert_to_float(st.text_input('PPE'))

    if st.button("Parkinson's Test Result"):
        if all(v is not None for v in [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]):
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
            parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
            st.success(parkinsons_diagnosis)
        else:
            st.error("Please provide valid input values.")

# Lungs Cancer Prediction Page
if selected == "Lungs Cancer Prediction":
    st.title("Lungs Cancer Disease Prediction using ML")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        GENDER = st.text_input('Gender')
    with col2:
        AGE = convert_to_float(st.text_input('Age'))
    with col3:
        SMOKING = st.text_input('Smoking')
    with col4:
        YELLOW_FINGERS = st.text_input('Yellow Finger')
    with col1:
        ANXIETY = st.text_input('Anxiety')
    with col2:
        PEER_PRESSURE = st.text_input('Peer Pressure')
    with col3:
        CHRONIC_DISEASE = st.text_input('Chronic Disease')
    with col4:
        FATIGUE = st.text_input('Fatigue')
    with col1:
        ALLERGY = st.text_input('Allergy')
    with col2:
        WHEEZING = st.text_input('Wheezing')
    with col3:
        ALCOHOL_CONSUMING = st.text_input('Alcohol Consuming')
    with col4:
        COUGHING = st.text_input('Coughing')
    with col1:
        SHORTNESS_OF_BREATH = st.text_input('Shortness Of Breath')
    with col2:
        SWALLOWING_DIFFICULTY = st.text_input('Swallowing Difficulty')
    with col3:
        CHEST_PAIN = st.text_input('Chest Pain')

    if st.button("Lung's Test Result"):
        if all(v is not None for v in [AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]):
            lungs_prediction = lungs_disease_model.predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
            lungs_diagnosis = "The person has lungs cancer disease" if lungs_prediction[0] == 1 else "The person does not have lungs cancer disease"
            st.success(lungs_diagnosis)
        else:
            st.error("Please provide valid input values.")

# Hypo-Thyroid Prediction Page
if selected == "Hypo-Thyroid Prediction":
    st.title("Hypo-Thyroid Prediction using ML")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = convert_to_float(st.text_input('Age'))
    with col2:
        sex = st.text_input('Sex')
    with col3:
        on_thyroxine = st.text_input('On Thyroxine')
    with col1:
        tsh = convert_to_float(st.text_input('TSH'))
    with col2:
        t3_measured = convert_to_float(st.text_input('T3 Measured'))
    with col3:
        t3 = convert_to_float(st.text_input('T3'))
    with col1:
        tt4 = convert_to_float(st.text_input('TT4'))

    if st.button("Thyroid's Test Result"):
        if all(v is not None for v in [age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]):
            thyroid_prediction = thyroid_model.predict([[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]])
            thyroid_diagnosis = "The person has Hypo Thyroid disease" if thyroid_prediction[0] == 1 else "The person does not have Hypo Thyroid disease"
            st.success(thyroid_diagnosis)
        else:
            st.error("Please provide valid input values.")
