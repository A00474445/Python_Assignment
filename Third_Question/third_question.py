import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

st.title('Question 3 - Python')
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")


if uploaded_file is not None:
    
    df = pd.read_csv(uploaded_file)

    if 'Age' in df.columns and 'Name' in df.columns:
        st.write("Histogram of Ages:")
        fig, ax = plt.subplots()

        ax.hist(df['Age'], bins=100, edgecolor='black')
        ax.set_xlabel('Age')
        ax.set_ylabel('Frequency')
        ax.set_title('Histogram of Ages')
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))

        st.pyplot(fig)
        
    else:
        st.error("Invalid File Format")
