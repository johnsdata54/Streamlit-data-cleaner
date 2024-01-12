import streamlit as st
import pandas as pd
import random


st.header("Data cleaner:")
st.subheader("The intention of the program is to eliminate duplicates, emtpty values, and optional remove columns")

# sample data generated from chatgpt to test functionality
# Sample data
names = ['Alice', 'Bob', 'Charlie', 'David']
ages = [random.randint(20, 30) for _ in range(len(names))]
scores = [random.uniform(60, 100) for _ in range(len(names))]

# Creating a DataFrame
data = {'Name': names, 'Age': ages, 'Score': scores}
df = pd.DataFrame(data)

uploaded_file = st.file_uploader("Upload a file")

if uploaded_file is None:
    pass
else:

    df_type = st.selectbox("Please select file input", ["SQL Database", "Excel Spreadsheet", "CSV" ])

    if df_type == "SQL Database":
        st.write("1")
    elif df_type == "Excel Spreadsheet":
        st.write("2")
    elif df_type == "CSV":
        st.write("3")

    #All code under this comment -- functionality of what is written needs to be shown after a table of data has been uploaded


    list_columns = []

    for columns in df.columns:
        list_columns.append(columns)

    st.write("Please select columns to discard")

    st.multiselect("Column names available", options = list_columns)

    #All code under this comment -- functionality of what is written needs to be shown after a table of data has been uploaded


    output = st.selectbox("Please select file output", ["SQL Database", "Excel Spreadsheet", "CSV" ])



    #st.download_button(label = f"Click to {output}", data = None)