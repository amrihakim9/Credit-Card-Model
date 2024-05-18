import streamlit as st
import pickle
import pandas as pd

# Define the run method for model prediction
def run():
    st.title("Predict Students' Dropout and Academic Success")

    # Open the models using pickle library
    with open('model.pkl', 'rb') as file_1:
        model=pickle.load(file_1)
    with open('preprocessor.pkl', 'rb') as file_2:
        preprocessor=pickle.load(file_2)

    # Creating a form
    with st.form("Form"):
        # Dictionary of options as per provided choices
        ms_enc = {
            "Single": 1,
            "Married": 2,
            "Widower": 3,
            "Divorced": 4,
            "Facto union": 5,
            "Legally separated": 6
        }

        am_enc = {
            "1st phase - general contingent": 1,
            "2nd phase - general contingent": 17,
            "3rd phase - general contingent": 18,
            "Holders of other higher courses": 7,
            "Over 23 years old": 39,
            "Transfer": 42,
            "Change of course": 43,
            "Technological specialization diploma holders": 44,
            "Others": 99
        }

        ao_enc = {
            "First choice": 1,
            "2nd choice": 2,
            "3rd choice": 3,
            "4th choice": 4,
            "5th choice": 5,
            "6th choice": 6,
            "7th choice": 7,
            "8th choice": 8,
            "Last choice": 9
        }

        c_enc = {
            "Nursing": 9500,
            "Management": 9147,
            "Social Service": 9238,
            "Veterinary Nursing": 9085,
            "Journalism and Communication": 9773,
            "Advertising and Marketing Management": 9670,
            "Management (evening attendance)": 9991,
            "Tourism": 9254,
            "Social Service (evening attendance)": 8014,
            "Animation and Multimedia Design": 171,
            "Communication Design": 9070,
            "Agronomy": 9003,
            "Basic Education": 9853,
            "Informatics Engineering": 9119,
            "Others": 99
        }

        dea_enc = {
            "Daytime": 1,
            "Evening": 0
        }

        pq_enc = {
            "Secondary Education": 1,
            "Higher Education - Degree": 3,
            "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.": 19,
            "Technological specialization course": 39,
            "Others": 99
        }

        mq_enc = {
            "Secondary Education - 12th Year of schooling or Equiv.": 1,
            "Basic Education 1st Cycle (4th/5th Year) or Equiv.": 37,
            "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.": 38,
            "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.": 19,
            "Higher Education - Degree": 3,
            "Unknown": 34,
            "Higher Education - Bachelor's Degree": 2,
            "Others": 99
        }

        fq_enc = {
            "Secondary Education - 12th Year of schooling or Equiv.": 1,
            "Basic Education 1st Cycle (4th/5th Year) or Equiv.": 37,
            "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.": 38,
            "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.": 19,
            "Higher Education - Degree": 3,
            "Unknown": 34,
            "Higher Education - Bachelor's Degree": 2,
            "Others": 99
        }

        mo_enc = {
            "Student": 0,
            "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers": 1,
            "Specialists in Intellectual and Scientific Activities": 2,
            "Intermediate Level Technicians and Professions": 3,
            "Administrative staff": 4,
            "Personal Services, Security and Safety Workers and Sellers": 5,
            "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry": 6,
            "Skilled Workers in Industry, Construction and Craftsmen": 7,
            "Unskilled Workers": 9,
            "Others": 99
        }

        fo_enc = {
            "Student": 0,
            "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers": 1,
            "Specialists in Intellectual and Scientific Activities": 2,
            "Intermediate Level Technicians and Professions": 3,
            "Administrative staff": 4,
            "Personal Services, Security and Safety Workers and Sellers": 5,
            "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry": 6,
            "Skilled Workers in Industry, Construction and Craftsmen": 7,
            "Installation and Machine Operators and Assembly Workers": 8,
            "Unskilled Workers": 9,
            "Armed Forces Professions": 10,
            "Others": 99
        }

        dis_enc = {
            "Yes": 1,
            "No": 0
        }

        deb_enc = {
            "Yes": 1,
            "No": 0
        }

        tfu_enc = {
            "Yes": 1,
            "No": 0
        }

        g_enc = {
            "Male": 1,
            "Female": 0
        }

        sh_enc = {
            "Yes": 1,
            "No": 0
        }

        # Getting user input using radio button for categorical and input number for numerical
        ms_uc = st.radio("Choose Marital Status:", list(ms_enc.keys()))
        am_uc = st.radio("Choose Application Mode:", list(am_enc.keys()))
        ao_uc = st.radio("Choose Application Order:", list(ao_enc.keys()))
        c_uc = st.radio("Choose Course:", list(c_enc.keys()))
        dea_uc = st.radio("Choose Daytime/Evening Attendance:", list(dea_enc.keys()))
        pq_uc = st.radio("Choose Previous Qualification:", list(pq_enc.keys()))
        mq_uc = st.radio("Choose Mother's Qualification:", list(mq_enc.keys()))
        fq_uc = st.radio("Choose Father's Qualification:", list(fq_enc.keys()))
        mo_uc = st.radio("Choose Mother's Occupation:", list(mo_enc.keys()))
        fo_uc = st.radio("Choose Father's Occupation:", list(fo_enc.keys()))
        dis_uc = st.radio("Choose Displaced:", list(dis_enc.keys()))
        deb_uc = st.radio("Choose Debtor:", list(deb_enc.keys()))
        tfu_uc = st.radio("Choose Tuition Fees Up To Date:", list(tfu_enc.keys()))
        g_uc = st.radio("Choose Gender:", list(g_enc.keys()))
        sh_uc = st.radio("Choose Scholarsip Holder:", list(sh_enc.keys()))
        pqg = st.number_input('Choose Previous Qualification Grade (0-200):', min_value=0, max_value=200)
        ag = st.number_input('Choose Admission Grade (0-200):', min_value=0, max_value=200)
        age = st.number_input('Choose Age at Enrollment:', min_value=17, max_value=70)
        en1 = st.number_input('Choose Curricular units 1st sem (enrolled):', min_value=0, max_value=30)
        ev1 = st.number_input('Choose Curricular units 1st sem (evaluations):', min_value=0, max_value=50)
        ap1 = st.number_input('Choose Curricular units 1st sem (approved):', min_value=0, max_value=30)
        gr1 = st.number_input('Choose Curricular units 1st sem (grade: 0-20):', min_value=0, max_value=20)
        en2 = st.number_input('Choose Curricular units 2nd sem (enrolled):', min_value=0, max_value=30)
        ev2 = st.number_input('Choose Curricular units 2nd sem (evaluations):', min_value=0, max_value=50)
        ap2 = st.number_input('Choose Curricular units 2nd sem (approved):', min_value=0, max_value=30)
        gr2 = st.number_input('Choose Curricular units 2nd sem (grade: 0-20):', min_value=0, max_value=20)

        # Displaying the chosen option
        st.write("Marital Status:", ms_uc)
        st.write("Application Mode:", am_uc)
        st.write("Application Order:", ao_uc)
        st.write("Course:", c_uc)
        st.write("Daytime/Evening Attendance:", dea_uc)
        st.write("Previous Qualification:", pq_uc)
        st.write("Mother's Qualification:", mq_uc)
        st.write("Father's Qualification:", fq_uc)
        st.write("Mother's Occupation:", mo_uc)
        st.write("Father's Occupation:", fo_uc)
        st.write("Displaced:", dis_uc)
        st.write("Debtor:", deb_uc)
        st.write("Tuition Fees Up To Date:", tfu_uc)
        st.write("Gender:", g_uc)
        st.write("Scholarsip Holder:", sh_uc)
        st.write('Previous Qualification Grade', pqg)
        st.write('Admission Grade', ag)
        st.write('Age at Enrollment', age)
        st.write('Curricular units 1st sem (enrolled)', en1)
        st.write('Curricular units 1st sem (evaluations)', ev1)
        st.write('Curricular units 1st sem (approved)', ap1)
        st.write('Curricular units 1st sem (grade)', gr1)
        st.write('Curricular units 2nd sem (enrolled)', en2)
        st.write('Curricular units 2nd sem (evaluations)', ev2)
        st.write('Curricular units 2nd sem (approved)', ap2)
        st.write('Curricular units 2nd sem (grade)', gr2)

        # Submitting the form
        sub = st.form_submit_button("Submit")
    
    # Create new dataframe by retrieving the input data from earlier
    feat_values = {
        "Marital status":ms_enc[ms_uc],
        "Application mode":am_enc[am_uc],
        "Application order":ao_enc[ao_uc],
        "Course":c_enc[c_uc],
        "Daytime/evening attendance":dea_enc[dea_uc],
        "Previous qualification":pq_enc[pq_uc],
        "Mother's qualification" : mq_enc[mq_uc],
        "Father's qualification" : fq_enc[fq_uc],
        "Mother's occupation" : mo_enc[mo_uc],
        "Father's occupation" : fo_enc[fo_uc],
        "Displaced" : dis_enc[dis_uc],
        "Debtor" : deb_enc[deb_uc],
        "Tuition fees up to date" : tfu_enc[tfu_uc],
        "Gender" : g_enc[g_uc],
        "Scholarship holder" : sh_enc[sh_uc],
        "Previous qualification (grade)" : [pqg],
        "Admission grade" : [ag],
        "Age at enrollment" : [age],
        "Curricular units 1st sem (enrolled)" : [en1],
        "Curricular units 1st sem (evaluations)" : [ev1],
        "Curricular units 1st sem (approved)" : [ap1],
        "Curricular units 1st sem (grade)" : [gr1],
        "Curricular units 2nd sem (enrolled)" : [en2],
        "Curricular units 2nd sem (evaluations)" : [ev2],
        "Curricular units 2nd sem (approved)" : [ap2],
        "Curricular units 2nd sem (grade)" : [gr2]
    }

    new_df = pd.DataFrame(feat_values)

    # Prediction
    if sub:
        prep = preprocessor.transform(new_df)
        predictions = model.predict(prep)
        if predictions == 'Dropout':
            st.write("Students may DROPOUT!")
        elif predictions == 'Graduate':
            st.write("Students may GRADUATE!")
        else:
            st.write("Students may ENROLL!")