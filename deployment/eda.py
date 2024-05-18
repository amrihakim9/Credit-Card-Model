import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Define the run method for EDA
def run():
    st.title('Exploratory Data Analysis (EDA)')

    # Load a picture
    a = Image.open('university.png')
    st.image(a, caption='College', use_column_width="always")

    # Load dataset
    st.write('Dataset')
    df = pd.read_csv('data.csv', sep=';')
    st.write(df)

    # Data visualization using scatter plot
    st.write('Visualization')
    option1 = st.selectbox(
        'Feature 1',
        ('Previous qualification (grade)', 'Admission grade', 'Age at enrollment', 'Curricular units 1st sem (credited)', 'Curricular units 1st sem (enrolled)', 'Curricular units 1st sem (evaluations)', 'Curricular units 1st sem (approved)', 'Curricular units 1st sem (grade)', 'Curricular units 1st sem (without evaluations)', 'Curricular units 2nd sem (credited)','Curricular units 2nd sem (enrolled)', 'Curricular units 2nd sem (evaluations)', 'Curricular units 2nd sem (approved)', 'Curricular units 2nd sem (grade)', 'Curricular units 2nd sem (without evaluations)', 'Unemployment rate', 'Inflation rate', 'GDP')
    )

    option2 = st.selectbox(
        'Feature 2',
        ('Previous qualification (grade)', 'Admission grade', 'Age at enrollment', 'Curricular units 1st sem (credited)', 'Curricular units 1st sem (enrolled)', 'Curricular units 1st sem (evaluations)', 'Curricular units 1st sem (approved)', 'Curricular units 1st sem (grade)', 'Curricular units 1st sem (without evaluations)', 'Curricular units 2nd sem (credited)','Curricular units 2nd sem (enrolled)', 'Curricular units 2nd sem (evaluations)', 'Curricular units 2nd sem (approved)', 'Curricular units 2nd sem (grade)', 'Curricular units 2nd sem (without evaluations)', 'Unemployment rate', 'Inflation rate', 'GDP')
    )

    st.write('You selected:', option1, ' and ', option2)

    fig, ax = plt.subplots()
    ax.scatter(df[option1], df[option2])
    st.pyplot(fig)