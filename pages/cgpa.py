import streamlit as st
import pandas as pd
from utils import *


def cgpa_page():
    marks_df = st.session_state.marks_df
    marks_df["Grade"] = [calculate_grade(x) for x in marks_df["Final CIE+SEE"]]
    marks_df["Grade Point"] = [calculate_grade_point(x) for x in marks_df["Final CIE+SEE"]]
    marks_df["Grade Point x Credits"] = marks_df["Credits"] * marks_df["Grade Point"]
    sgpa = marks_df["Grade Point x Credits"].sum() / marks_df["Credits"].sum()
    average_percentage = marks_df["Final CIE+SEE"].mean() / 100 * 100
    with st.container(border=True):
        sgpa_col, percentage_col = st.columns(2)
        with sgpa_col:
            with st.container(border=True):
                st.metric(label="SGPA", value=round(sgpa, 2))

        with percentage_col:
            with st.container(border=True):
                st.metric(label="Average Percentage", value=round(average_percentage, 2))

        st.dataframe(marks_df, use_container_width=True, hide_index=True)
        col1, col2, col3 = st.columns(3)
        with col2:
            marks_csv = convert_df(marks_df)
            st.download_button(label="Download table as CSV", data=marks_csv, file_name='FinalCGPA.csv',
                               mime='text/csv', use_container_width=True, type='primary')
    print(marks_df)
    print(sgpa)


