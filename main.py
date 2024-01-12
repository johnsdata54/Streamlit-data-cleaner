import streamlit as st
import pandas as pd

st.write("TEST")
st.write("TEST")
st.write("TEST")




df_type = st.selectbox("Please select file input", ["SQL Database", "Excel Spreadsheet", "CSV" ])

if df_type == "SQL Database":
    st.write("1")
elif df_type == "Excel Spreadsheet":
    st.write("2")
elif df_type == "CSV":
    st.write("3")




#All code under this comment -- functionality of what is written needs to be shown after a table of data has been uploaded


output = st.selectbox("Please select file output", ["SQL Database", "Excel Spreadsheet", "CSV" ])



#st.download_button(label = f"Click to {output}", data = None)