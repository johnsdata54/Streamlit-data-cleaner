import streamlit as st
import pandas as pd
import random


st.header("Data cleaner:")
st.subheader("The intention of the program is to eliminate duplicates, empty values, and optionally remove columns")

# sample data generated from chatgpt to test functionality

# Sample data
names = ['Alice', 'Bob', 'Charlie', 'David', 'David', 'Tatum', 'Kayla', 'Simone', 'Jack']
ages = [random.randint(20, 30) for _ in range(len(names))]
scores = [random.uniform(60, 100) for _ in range(len(names))]

# Creating a DataFrame
data = {'Name': names, 'Age': ages, 'Score': scores}

df = pd.DataFrame(data)

uploaded_file = st.file_uploader("Upload a file")

data = pd.read_csv(uploaded_file)

df = pd.DataFrame(data)

if uploaded_file is None:
    pass
else:

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

    st.header("Would you like to remove duplicates?")

    duplicates = df.duplicated()

    num_duplicates = duplicates.sum()

    st.write(f"The number of duplicates: {num_duplicates}")

   
    if num_duplicates == 0:
        decision = None
    else:

        decision = st.checkbox(f"Would you like to remove the duplicated entries from the data set")

        backup_df_1 = df

        if decision:
            df = df.drop_duplicates()
        else:
            df = backup_df_1

    st.header("Would you like to remove Null/NaN values?")

    #na_counts = df.groupby('Name')['value'].apply(lambda x: x.isna().sum())

    st.write("The number of null values per attribute: {} ")

    st.header("Would you like to remove columns?")

    

    #All code under this comment -- functionality of what is written needs to be shown after a table of data has been uploaded

    list_columns = []

    for columns in df.columns:
        list_columns.append(columns)

    st.write("Please select columns to discard")

    columns_del = st.multiselect("Column names available", options = list_columns)

    st.write(columns_del)
    #All code under this comment -- functionality of what is written needs to be shown after a table of data has been uploaded

    output = st.selectbox("Please select file output", ["SQL Database", "Excel Spreadsheet", "CSV" ])

    #st.download_button(label = f"Click to {output}", data = None)