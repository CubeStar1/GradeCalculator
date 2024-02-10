import streamlit as st
import math
from utils import *
import pandas as pd
import streamlit_antd_components as sac

st.set_page_config(page_title="CGPA Calculator", page_icon="📚", layout="wide")
st.title("CGPA Calculator")
st.write("This is a simple web app to calculate your CGPA. Please enter your marks in the fields below and click on the 'Calculate CGPA' button to get your CGPA.")
st.markdown("---")

if 'marks_df' not in st.session_state:
    st.session_state.marks_df = pd.DataFrame({
            "Credits": [4, 4, 3, 3, 3, 1, 1, 1],
            "Course Name": ["22MA11C", "22CHY12A", "ESC", "PLC", "CAEG", "Communicative English", "Indian Constitution", "Yoga"],
            "Final CIE": [0, 0, 0, 0, 0, 0, 0, 0],
            "Final SEE": [0, 0, 0, 0, 0, 0, 0, 0],
            "Final CIE+SEE": [0, 0, 0, 0, 0, 0, 0, 0],
            "Grade": ["", "", "", "", "", "", "", ""],
            "Grade Point": [0, 0, 0, 0, 0, 0, 0, 0],
            "Grade Point x Credits": [0, 0, 0, 0, 0, 0, 0, 0]
        })

if 'calculate_button' not in st.session_state:
    st.session_state.calculate_button = False

from pages.cgpa import cgpa_page
from pages.marks import marks_entry_page

marks_entry_page()
st.markdown("---")
if st.session_state.calculate_button:
    cgpa_page()

# def page_selection():
#     selected = sac.segmented(
#     items=[
#         sac.SegmentedItem(label='Marks', icon='edit',),
#         sac.SegmentedItem(icon='CGPA', label='CGPA', ),
#     ], label='', align='center', use_container_width=True,
#     )
#
#     if selected == 'Marks':
#         marks_entry_page()
#     elif selected == 'CGPA':
#         cgpa_page()
#
# page_selection()