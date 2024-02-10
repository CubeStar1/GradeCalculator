import streamlit as st
import math
from utils import *
import pandas as pd


def marks_entry_page():
    with st.container(border=True):
        with st.container(border=True, height=500):
            st.subheader("4-credit courses")

            math_col, chem_col = st.columns(2)

            with math_col:
                with st.container(border=True):
                    st.subheader("Fundamentals of Linear Algebra, Calculus and Statistics - 22MA11C")
                    with st.expander("CIE Marks", expanded=False):
                        test1_math = st.number_input("Test 1", min_value=0, max_value=50, value=0, key="test1_math")
                        test2_math = st.number_input("Test 2", min_value=0, max_value=50, value=0, key="test2_math")
                        test_3_math = st.number_input("Test 3", min_value=0, max_value=50, value=0, key="test3_math")
                        quiz1_math = st.number_input("Quiz 1", min_value=0, max_value=10, value=0, key="quiz1_math")
                        quiz2_math = st.number_input("Quiz 2", min_value=0, max_value=10, value=0, key="quiz2_math")
                        quiz_3_math = st.number_input("Quiz 3", min_value=0, max_value=10, value=0, key="quiz3_math")
                        matlab_math = st.number_input("MATLAB", min_value=0, max_value=100, value=0, key="matlab_math")
                        el_math = st.number_input("EL", min_value=0, max_value=20, value=0, key="el_math")
                        test_marks_math = [test1_math, test2_math, test_3_math]
                        quiz_marks_math = [quiz1_math, quiz2_math, quiz_3_math]
                        matlab_marks_math = [matlab_math]
                        el_marks_math = [el_math]
                        final_cie_math = math.ceil(
                            calculate_math_cie_marks(test_marks_math, quiz_marks_math, matlab_marks_math, el_marks_math))
                    with st.container(border=True):
                        final_cie_math = st.number_input("Final CIE", min_value=0, max_value=100, value=final_cie_math,
                                                         key="cie_math")

                    with st.container(border=True):
                        final_see_math = st.number_input("Final SEE", min_value=0, max_value=100, value=0, key="see_math")

            with chem_col:
                with st.container(border=True):
                    st.subheader("Chemistry of Smart Materials and Devices - 22CHY12A")
                    with st.expander("CIE Marks", expanded=False):
                        test1_chem = st.number_input("Test 1", min_value=0, max_value=50, value=0, key="test1_chem")
                        test2_chem = st.number_input("Test 2", min_value=0, max_value=50, value=0, key="test2_chem")
                        test_3_chem = st.number_input("Test 3", min_value=0, max_value=50, value=0, key="test3_chem")
                        quiz1_chem = st.number_input("Quiz 1", min_value=0, max_value=10, value=0, key="quiz1_chem")
                        quiz2_chem = st.number_input("Quiz 2", min_value=0, max_value=10, value=0, key="quiz2_chem")
                        quiz_3_chem = st.number_input("Quiz 3", min_value=0, max_value=10, value=0, key="quiz3_chem")
                        lab_chem = st.number_input("Lab", min_value=0, max_value=30, value=0, key="lab_chem")
                        el_chem = st.number_input("EL", min_value=0, max_value=30, value=0, key="el_chem")
                        test_marks_chem = [test1_chem, test2_chem, test_3_chem]
                        quiz_marks_chem = [quiz1_chem, quiz2_chem, quiz_3_chem]
                        lab_marks_chem = [lab_chem]
                        el_marks_chem = [el_chem]
                        final_cie_chem = math.ceil(
                            calculate_chem_cie_marks(test_marks_chem, quiz_marks_chem, lab_marks_chem, el_marks_chem))
                    with st.container(border=True):
                        final_cie_chem = st.number_input("Final CIE", min_value=0, max_value=100, value=final_cie_chem,
                                                         key="cie_chem")

                    with st.container(border=True):
                        final_see_chem = st.number_input("Final SEE", min_value=0, max_value=100, value=0, key="see_chem")

        with st.container(border=True, height=500):
            st.subheader("3-credit courses")

            esc_col, plc_col, caeg_col = st.columns(3)

            with esc_col:
                with st.container(border=True):
                    st.subheader("ESC")
                    with st.expander(label="CIE Marks", expanded=False):
                        test1_esc = st.number_input("Test 1", min_value=0, max_value=50, value=0, key="test1_esc")
                        test2_esc = st.number_input("Test 2", min_value=0, max_value=50, value=0, key="test2_esc")
                        test_3_esc = st.number_input("Test 3", min_value=0, max_value=50, value=0, key="test3_esc")
                        quiz1_esc = st.number_input("Quiz 1", min_value=0, max_value=10, value=0, key="quiz1_esc")
                        quiz2_esc = st.number_input("Quiz 2", min_value=0, max_value=10, value=0, key="quiz2_esc")
                        quiz_3_esc = st.number_input("Quiz 3", min_value=0, max_value=10, value=0, key="quiz3_esc")
                        el_esc = st.number_input("EL", min_value=0, max_value=40, value=0, key="el_esc")
                        test_marks_esc = [test1_esc, test2_esc, test_3_esc]
                        quiz_marks_esc = [quiz1_esc, quiz2_esc, quiz_3_esc]
                        el_marks_esc = [el_esc]
                        final_cie_esc = math.ceil(calculate_esc_cie_marks(test_marks_esc, quiz_marks_esc, el_marks_esc))
                    with st.container(border=True):
                        final_cie_esc = st.number_input("Final CIE", min_value=0, max_value=100, value=final_cie_esc,
                                                        key="cie_esc")

                    with st.container(border=True):
                        final_see_esc = st.number_input("Final SEE", min_value=0, max_value=100, value=0, key="see_esc")

            with plc_col:
                with st.container(border=True):
                    st.subheader("PLC")
                    with st.expander(label="CIE Marks", expanded=False):
                        test1_plc = st.number_input("Test 1", min_value=0, max_value=50, value=0, key="test1_plc")
                        test2_plc = st.number_input("Test 2", min_value=0, max_value=50, value=0, key="test2_plc")
                        test_3_plc = st.number_input("Test 3", min_value=0, max_value=50, value=0, key="test3_plc")
                        quiz1_plc = st.number_input("Quiz 1", min_value=0, max_value=10, value=0, key="quiz1_plc")
                        quiz2_plc = st.number_input("Quiz 2", min_value=0, max_value=10, value=0, key="quiz2_plc")
                        quiz_3_plc = st.number_input("Quiz 3", min_value=0, max_value=10, value=0, key="quiz3_plc")
                        lab_plc = st.number_input("Lab", min_value=0, max_value=30, value=0, key="lab_plc")
                        el_plc = st.number_input("EL", min_value=0, max_value=100, value=0, key="el_plc")
                        test_marks_plc = [test1_plc, test2_plc, test_3_plc]
                        quiz_marks_plc = [quiz1_plc, quiz2_plc, quiz_3_plc]
                        lab_marks_plc = [lab_plc]
                        el_marks_plc = [el_plc]
                        final_cie_plc = math.ceil(
                            calculate_plc_cie_marks(test_marks_plc, quiz_marks_plc, lab_marks_plc, el_marks_plc))
                    with st.container(border=True):
                        final_cie_plc = st.number_input("Final CIE", min_value=0, max_value=100, value=final_cie_plc,
                                                        key="cie_plc")

                    with st.container(border=True):
                        final_see_plc = st.number_input("Final SEE", min_value=0, max_value=100, value=0, key="see_plc")

            with caeg_col:
                with st.container(border=True):
                    st.subheader("CAEG")
                    with st.expander(label="CIE Marks", expanded=False):
                        test1_caeg = st.number_input("Test 1", min_value=0, max_value=50, value=0, key="test1_caeg")
                        test2_caeg = st.number_input("Test 2", min_value=0, max_value=50, value=0, key="test2_caeg")
                        test_3_caeg = st.number_input("Test 3", min_value=0, max_value=50, value=0, key="test3_caeg")
                        lab_caeg = st.number_input("Lab", min_value=0, max_value=30, value=0, key="lab_caeg")
                        el_caeg = st.number_input("EL", min_value=0, max_value=100, value=0, key="el_caeg")
                        test_marks_caeg = [test1_caeg, test2_caeg, test_3_caeg]
                        lab_marks_caeg = [lab_caeg]
                        el_marks_caeg = [el_caeg]
                        final_cie_caeg = math.ceil(calculate_caeg_cie_marks(test_marks_caeg, lab_marks_caeg, el_marks_caeg))
                    with st.container(border=True):
                        final_cie_caeg = st.number_input("Final CIE", min_value=0, max_value=50, value=final_cie_caeg,
                                                         key="cie_caeg")

                    with st.container(border=True):
                        final_see_caeg = st.number_input("Final SEE", min_value=0, max_value=50, value=0, key="see_caeg")

        with st.container(border=True, height=500):
            st.subheader("1-credit courses")

            english, indian_const, yoga = st.columns(3)

            with english:
                with st.container(border=True):
                    st.subheader("Communicative English")
                    with st.expander(label="CIE Marks", expanded=False):
                        test1_eng = st.number_input("Test 1", min_value=0, max_value=50, value=0, key="test1_eng")
                        test2_eng = st.number_input("Test 2", min_value=0, max_value=50, value=0, key="test2_eng")
                        el_eng = st.number_input("EL", min_value=0, max_value=100, value=0, key="el_eng")

                        test_marks_eng = [test1_eng, test2_eng]
                        el_marks_eng = [el_eng]
                        final_cie_eng = math.ceil(calculate_english_cie_marks(test_marks_eng, el_marks_eng))
                    with st.container(border=True):
                        final_cie_eng = st.number_input("Final CIE", min_value=0, max_value=50, value=final_cie_eng,
                                                        key="cie_eng")

                    with st.container(border=True):
                        final_see_eng = st.number_input("Final SEE", min_value=0, max_value=50, value=0, key="see_eng")

            with indian_const:
                with st.container(border=True):
                    st.subheader("Indian Constitution")
                    with st.expander(label="CIE Marks", expanded=False):
                        test_1_ic = st.number_input("Test 1", min_value=0, max_value=50, value=0, key="test1_ic")
                        test_2_ic = st.number_input("Test 2", min_value=0, max_value=50, value=0, key="test2_ic")
                        test_3_ic = st.number_input("Test 3", min_value=0, max_value=50, value=0, key="test3_ic")
                        quiz_1_ic = st.number_input("Quiz 1", min_value=0, max_value=10, value=0, key="quiz1_ic")
                        quiz_2_ic = st.number_input("Quiz 2", min_value=0, max_value=10, value=0, key="quiz2_ic")
                        quiz_3_ic = st.number_input("Quiz 3", min_value=0, max_value=10, value=0, key="quiz3_ic")
                        el_ic = st.number_input("EL", min_value=0, max_value=10, value=0, key="el_ic")
                        test_marks_ic = [test_1_ic, test_2_ic, test_3_ic]
                        quiz_marks_ic = [quiz_1_ic, quiz_2_ic, quiz_3_ic]
                        el_marks_ic = [el_ic]
                        final_cie_ic = math.ceil(calculate_ic_cie_marks(test_marks_ic, quiz_marks_ic, el_marks_ic))
                    with st.container(border=True):
                        final_cie_ic = st.number_input("Final CIE", min_value=0, max_value=50, value=final_cie_ic,
                                                       key="cie_ic")

                    with st.container(border=True):
                        final_see_ic = st.number_input("Final SEE", min_value=0, max_value=50, value=0, key="see_ic")

            with yoga:
                with st.container(border=True):
                    st.subheader("Yoga")
                    with st.expander(label="CIE Marks", expanded=False):
                        test_1_yoga = st.number_input("Quiz 1", min_value=0, max_value=20, value=0, key="quiz1_yoga")
                        lab_test_yoga = st.number_input("Lab Test", min_value=0, max_value=50, value=0, key="lab_test_yoga")
                        el_yoga = st.number_input("EL", min_value=0, max_value=10, value=0, key="el_yoga")
                        quiz_marks_yoga = [test_1_yoga]
                        lab_test_marks_yoga = [lab_test_yoga]
                        el_marks_yoga = [el_yoga]
                        final_cie_yoga = math.ceil(
                            calculate_yoga_cie_marks(quiz_marks_yoga, lab_test_marks_yoga, el_marks_yoga))
                    with st.container(border=True):
                        final_cie_yoga = st.number_input("Final CIE", min_value=0, max_value=50, value=final_cie_yoga,
                                                         key="cie_yoga")

                    with st.container(border=True):
                        final_see_yoga = st.number_input("Final SEE", min_value=0, max_value=50, value=0, key="see_yoga")

        col1, col2, col3 = st.columns(3)

        with col2:
            calclulate_button = st.button("Calculate CGPA", use_container_width=True, type="primary")

        if calclulate_button:
            st.session_state.calculate_button = True
            marks_df = pd.DataFrame({
                "Credits": [4, 4, 3, 3, 3, 1, 1, 1],
                "Course Name": ["22MA11C", "22CHY12A", "ESC", "PLC", "CAEG", "Communicative English", "Indian Constitution",
                                "Yoga"],
                "Final CIE": [final_cie_math, final_cie_chem, final_cie_esc, final_cie_plc, final_cie_caeg, final_cie_eng,
                              final_cie_ic, final_cie_yoga],
                "Final SEE": [final_see_math, final_see_chem, final_see_esc, final_see_plc, final_see_caeg, final_see_eng,
                              final_see_ic, final_see_yoga],
                "Final CIE+SEE": [(final_cie_math + final_see_math) / 2, (final_cie_chem + final_see_chem) / 2,
                                  (final_cie_esc + final_see_esc) / 2, (final_cie_plc + final_see_plc) / 2,
                                  final_cie_caeg + final_see_caeg, final_cie_eng + final_see_eng,
                                  final_cie_ic + final_see_ic,
                                  final_cie_yoga + final_see_yoga]
            })
            st.session_state.marks_df = marks_df
            print(marks_df)


marks_entry_page()
