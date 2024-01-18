import streamlit as st
import pandas as pd
import os


st.header("Data cleaner:")
st.subheader("The intention of the program is to eliminate duplicates, empty values, and optionally remove columns")
st.warning("This application currently only takes .CSV files")

file_dict = {1:"csv", 2:"sql", 3:"xlsx", 4:"xls"}

file_types = []

uploaded_file = st.file_uploader("Upload a file")


if uploaded_file is None:

    st.write("Please select a CSV file to proceed.")
else:

    file_name, file_ext = os.path.splitext(uploaded_file.name)
    # Append the file extension to the list
    file_types.append(file_ext)
    # Print the list
    

    df = pd.read_csv(uploaded_file)

    dataframe_select = st.selectbox("Select preview amount for data frame", options = [5, 10, 15])

        #this presents head of the data sheet
    st.write("Preview data head")
    head = df.head(dataframe_select)
    st.dataframe(head)

    #this presents tail of the data sheet
    st.write("Preview data tail")
    tail = df.tail(dataframe_select)
    st.dataframe(tail)

    duplicates = df.duplicated()

    num_duplicates = duplicates.sum()

    if num_duplicates == 0:

        st.success("You have no duplicates.")
        pass
    else:

        st.header("Would you like to remove duplicates?")

        st.write(f"The number of duplicates: {num_duplicates}")

        dup_decision = st.checkbox("Yes?", key = 1)

        if dup_decision:
                
            if num_duplicates == 1:
                decision = None
            else:

                decision = st.checkbox(f"Would you like to remove the duplicated entries from the data set")

                backup_df_1 = df

                if decision:
                    df = df.drop_duplicates()
                else:
                    df = backup_df_1
        else:
            pass

    #na_counts = df.groupby('Name')['value'].apply(lambda x: x.isna().sum())
        
    na_counts = 0

    if na_counts == 0:

        st.success("You have no Null values.")
    else:
        st.header("Would you like to remove Null/NaN values?")
        
        #na_counts = df.groupby('Name')['value'].apply(lambda x: x.isna().sum())

        st.write(f"The number of null values per attribute: {num_duplicates} ")

    
    st.header("Would you like to remove columns?")


    #All code under this comment -- functionality of what is written needs to be shown after a table of data has been uploaded

    list_columns = []

    for columns in df.columns:
        list_columns.append(columns)

    decision = st.checkbox(f"Yes?", key = 2)

    if decision:
        st.write("Please select columns to discard")

        columns_del = st.multiselect("Column names available", options = list_columns)

        del_list_columns = []
        
        for i in range(len(columns_del)):

            del_list_columns.append(columns_del[i])

        if len(del_list_columns) > 0:

            st.write(del_list_columns)

    else:
        pass


    final_df = df
    
    #Output selection for the type of conversion that wants to happen to the dataframe

    output = st.selectbox("Please select file output", ["Database", "Excel Spreadsheet", "CSV" ])

    if output == "Excel Spreadsheet":



        file_name = st.text_input("Please name the file")

        excel_down = final_df.to_excel(f"{file_name}.xlsx")

        st.download_button(data=excel_down)
    elif output == "Database":



        file_name = st.text_input("Please name the file")

        if file_name is None:
            pass
        else:

            excel_down = final_df.to_excel(sheet_name=file_name)

            st.download_button(excel_down)

    elif output == "CSV":



        file_name = st.text_input("Please name the file")

        excel_down = final_df.to_excel(sheet_name=file_name)

        st.download_button(excel_down)


 
    #st.download_button(label = f"Click to {output}", data = None)