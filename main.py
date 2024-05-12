import streamlit as st
import pandas as pd
import io

def handle_duplicates(df):
        
        duplicates = df.duplicated()

        num_duplicates = duplicates.sum()

        if num_duplicates == 0:

            st.success("You have no duplicates.")
        
        else:

            st.header("Would you like to remove duplicates?")

            st.write(f"The number of duplicates: {num_duplicates}")

            dup_decision = st.checkbox("Yes?", key = 1)

            if dup_decision:

                backup_df_1 = df.copy()  # Create a copy of the original DataFrame for backup

                df = df.drop_duplicates()  # Remove duplicate rows from the DataFrame

                st.success("Duplicate entries removed.")
                    
            else:
                st.info("No changes made to duplicates.")
        return df


def handle_null_values(df):
    
        
    na_counts = df.isnull().sum()

    if na_counts.any():  # Check if any value in na_counts is greater than 0
        st.header("Would you like to remove Null/NaN values?")
        st.write(f"The number of null values per attribute:\n{na_counts}")

        null_decision = st.checkbox("Yes?", key=2)

        if null_decision:
            backup_df_2 = df.copy()  # Create a copy of the original DataFrame for backup
            df = df.dropna()  # Remove rows with null values from the DataFrame
            st.write("Null values removed.")
        else:
            st.write("No changes made to null values.")
    else:
        st.success("You have no Null values.")

    return df
    #All code under this comment -- functionality of what is written needs to be shown after a table of data has been uploaded


def handle_column_removal(df):

    st.header("Would you like to remove columns?")

    list_columns = df.columns.tolist()

    decision = st.checkbox(f"Yes?", key = 3)

    if decision:
        st.write("Please select columns to discard")

        columns_del = st.multiselect("Column names available", options = list_columns)
        
        if columns_del:
            backup_df_3 = df.copy()

            df = df.drop(columns=columns_del)

            st.success(f"Columns removed:{columns_del}")
            # Display a button to revert changes

            if st.button("Revert Changes"):
                df = backup_df_3  # Revert to the original DataFrame
                st.success("Changes reverted.")


        else:
            st.info("No columns selected for removal.")
    
    return df


    #Output selection for the type of conversion that wants to happen to the dataframe

def handle_file_output(final_df):
    st.header("Select your output type:")

    user_selection = st.selectbox("Please select file output", ["Database", "Excel Spreadsheet", "CSV" ])

    if user_selection == "Excel Spreadsheet":
        file_name = st.text_input("Please name the file")

        if file_name is not None:
            buffer = io.BytesIO()

            with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                final_df.to_excel(writer, f"{file_name}.xlsx", index=False)

            st.download_button(
                data=buffer.getvalue(),
                label=f'Download {file_name}.xlsx',
                file_name=file_name+'.xlsx'
            )
        elif final_df.empty:
            st.warning("DataFrame is empty. Provide non-empty data for Excel export.")
        else:
            st.warning("Enter file name")


    elif user_selection == "Database":

        file_name = st.text_input("Please name the file")

        if file_name is not None:
            pass
        else:

            excel_down = final_df.to_excel(sheet_name=file_name)

            st.download_button(excel_down)

    elif user_selection == "CSV":
        file_name = st.text_input("Please name the file")

        csv_down = final_df.to_csv(index=False)

        st.download_button(data=csv_down,
                           label=f'Download {file_name}',
                           file_name=f'{file_name}')

def main():
    st.header("Data cleaner:")
    st.subheader("The intention of the program is to eliminate duplicates, empty values, and optionally remove columns")
    st.warning("This application currently only takes .CSV files")

    file_types = ['.csv']
    uploaded_file = st.file_uploader("Upload a file", type=file_types)

    if uploaded_file is None:
        st.write("Please select a CSV file to proceed.")
    else:
        df = pd.read_csv(uploaded_file)


        dataframe_select = st.selectbox("Select preview amount for data frame", options=[5, 10, 15], key = 4)

        #this presents head of the data sheet
        st.write("Preview data head")
        head = df.head(dataframe_select)
        st.dataframe(head)

        #this presents tail of the data sheet
        st.write("Preview data tail")
        tail = df.tail(dataframe_select)
        st.dataframe(tail)

        # ... (Execute the functions in the desired order)
        df = handle_duplicates(df)
        df = handle_null_values(df)
        df = handle_column_removal(df)

        final_df = df

        handle_file_output(final_df)


if __name__ == "__main__":
    main()