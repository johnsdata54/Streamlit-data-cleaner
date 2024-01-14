import streamlit as st
import pandas as pd
import random


st.header("Data cleaner:")
st.subheader("The intention of the program is to eliminate duplicates, emtpty values, and optional remove columns")

# sample data generated from chatgpt to test functionality
# Sample data
names = ['Alice', 'Bob', 'Charlie', 'David', 'Thomas', 'Tatum', 'Kayla', 'Simone', 'Jack']
ages = [random.randint(20, 30) for _ in range(len(names))]
scores = [random.uniform(60, 100) for _ in range(len(names))]

# Creating a DataFrame
data = {'Name': names, 'Age': ages, 'Score': scores}
df = pd.DataFrame(data)

uploaded_file = st.file_uploader("Upload a file")

if uploaded_file is not None:
    pass
else:


    #count of nan values per column

    #Check yes or no if person would like to remove NA/NAN values

    #if yes save df to new variable, else pass orgginal to new variable

    dataframe_select = st.selectbox("Select preview amount for data frame", options = [5, 10, 15])

    #saving data to dataframe
    df = pd.DataFrame(data)

    #this presents head of the data sheet
    st.write("Preview data head")
    head = df.head(dataframe_select)
    st.dataframe(head)

    #this presents tail of the data sheet
    st.write("Preview data tail")
    tail = df.tail(dataframe_select)
    st.dataframe(tail)



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