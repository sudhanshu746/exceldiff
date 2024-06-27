import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
import io


def compare_sheets(sheet1: tuple, sheet2: tuple, unique_identifier: list) -> any:
    # Merge the two DataFrames on the 'Name' column
    df1 = pd.read_excel(sheet1[0], sheet_name=sheet1[1])
    df2 = pd.read_excel(sheet2[0], sheet_name=sheet2[1])
    suffixes=('_df1', '_df2')
    merged_df = df1.merge(df2, on=unique_identifier, how='outer', suffixes=suffixes)
    # Function to check if values are different
    def is_different(row):
        return row[0] if row[0] == row[1] else f'"{row[0]}"| "{row[1]}"'
    # unique_identifier_suffixes = [f'{iden}{suf}' for iden, suf in zip(unique_identifier, list(suffixes))]
    # Apply the function across the rows for selected columns
    for col in set(df1.columns).difference(set(unique_identifier)):
        merged_df[col] = merged_df[[f'{col}_df1', f'{col}_df2']].apply(is_different, axis=1)
        merged_df.drop([f'{col}_df1', f'{col}_df2'], axis=1, inplace=True)

    # Define a styling function to highlight differences
    def highlight_diffs(val):
        if '|' in str(val):
            return f'color: red;'
            
        else:
            return f'background-color: #f5f5f5;' 

    # Apply the styling
    styles = merged_df.style.applymap(highlight_diffs)
    return styles


# Other parts of your Streamlit app should work as before ...

# Set up the Streamlit app layout
st.title('Excel Sheet Comparator')

# File upload section for the two Excel files
uploaded_file_1 = st.file_uploader("Choose first Excel file", type=['xlsx'])
if uploaded_file_1 is not None:
    sheet_names_1 = pd.ExcelFile(uploaded_file_1).sheet_names
    sheet_name_1 = st.selectbox('Select a sheet:', sheet_names_1)
    unique_identifiers = list(pd.read_excel(uploaded_file_1, sheet_name_1).columns)
    if sheet_name_1 is not None:
        try:
            selected_join = st.multiselect('Select unique common column(s) for join field:', unique_identifiers, key='file_1')
        except Exception as e:
            st.error(f'Please select common column(s) in the files')

try:
    uploaded_file_2 = st.file_uploader("Choose second Excel file", type=['xlsx'])
    if uploaded_file_2 is not None:
        sheet_names_2 = pd.ExcelFile(uploaded_file_2).sheet_names
        sheet_name_2 = st.selectbox('Select a sheet:', sheet_names_2, key='file_2')
except Exception as e:
    #sheet_name_2 = sheet_name_1
    st.error(f'Please upload another file')
    


# Button to trigger the comparison
if st.button('Compare Sheets'):
    # Check if the files were uploaded and sheet names were provided
    if uploaded_file_1 is not None and uploaded_file_2 is not None and sheet_name_1 and sheet_name_2:
        try:
            # Perform the comparison
            result = compare_sheets((uploaded_file_1, sheet_name_1), (uploaded_file_2, sheet_name_2), selected_join)
            styled_html = result.to_html()
            # Display the differences
            st.write('Differences (Light Red: Content differs seperated by (|), light Green: content match:')
            # components.html(styled_html, width=1000, height=600, scrolling=True)
            st.dataframe(result)
            output = io.BytesIO()
            writer = pd.ExcelWriter(output, engine="openpyxl")
            result.to_excel(writer, index=False, sheet_name="sheet1")
            writer.close()
            data_bytes = output.getvalue()
            #writer = pd.ExcelWriter('comparison_result.xlsx', engine='openpyxl')
            #result_xlsx = result.to_excel(writer, sheet_name='comparison_result', startrow=0 , startcol=0, index=False)
            st.download_button(label='Download Comparison Excel', data=data_bytes, file_name='comparison_result.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        except Exception as e:
            st.error(f'An error occurred: {e}')
    else:
        st.error('Please upload both Excel files and provide corresponding sheet names.')