import streamlit as st
def calculate_sgpa(total_credits: int, total_gp: int):
    return total_gp / total_credits

def calculate_gp_credits(grade_point: int, credits: int):
    return grade_point * credits

def calculate_grade(marks: int):
    if marks >= 90:
        return 'O'
    elif 80 <= marks < 90:
        return 'A+'
    elif 70 <= marks < 80:
        return 'A'
    elif 60 <= marks < 70:
        return 'B+'
    elif 55 <= marks < 60:
        return 'B'
    elif 50 <= marks < 55:
        return 'C'
    elif 40 <= marks < 50:
        return 'P'
    else:
        return 'F'
def calculate_grade_point(marks: int):
    if marks >= 90:
        return 10
    elif 80 <= marks < 90:
        return 9
    elif 70 <= marks < 80:
        return 8
    elif 60 <= marks < 70:
        return 7
    elif 55 <= marks < 60:
        return 6
    elif 50 <= marks < 55:
        return 5
    elif 40 <= marks < 50:
        return 4
    else:
        return 0





def calculate_math_cie_marks(test_marks: list, quiz_marks: list, matlab_marks: list, el_marks: list):
    best_2_test_marks = sorted(test_marks, reverse=True)[:2]
    best_2_quiz_marks = sorted(quiz_marks, reverse=True)[:2]
    total_test_marks = sum(best_2_test_marks)
    total_quiz_marks = sum(best_2_quiz_marks)
    total_matlab_marks = sum(matlab_marks)
    total_el_marks = sum(el_marks)
    total_marks = float(total_test_marks) * 0.4 + float(total_quiz_marks) + float(total_matlab_marks) + float(
        total_el_marks)
    total_marks_rounded = round(total_marks, 2)
    return total_marks_rounded

def calculate_chem_cie_marks(test_marks: list, quiz_marks: list, lab_marks: list, el_marks: list):
    best_2_test_marks = sorted(test_marks, reverse=True)[:2]
    best_2_quiz_marks = sorted(quiz_marks, reverse=True)[:2]
    total_test_marks = sum(best_2_test_marks)
    total_quiz_marks = sum(best_2_quiz_marks) / 2
    total_matlab_marks = sum(lab_marks)
    total_el_marks = sum(el_marks)
    total_marks = float(total_test_marks) * 0.3 + float(total_quiz_marks) + float(total_matlab_marks) + float(total_el_marks)
    total_marks_rounded = round(total_marks, 2)
    return total_marks_rounded


def calculate_esc_cie_marks(test_marks: list, quiz_marks: list, el_marks: list):
    best_2_test_marks = sorted(test_marks, reverse=True)[:2]
    best_2_quiz_marks = sorted(quiz_marks, reverse=True)[:2]
    total_test_marks = sum(best_2_test_marks)
    total_quiz_marks = sum(best_2_quiz_marks)
    total_el_marks = sum(el_marks)
    total_marks = float(total_test_marks) * 0.4 + float(total_quiz_marks) + float(total_el_marks)
    total_marks_rounded = round(total_marks, 2)
    return total_marks_rounded


def calculate_plc_cie_marks(test_marks: list, quiz_marks: list, lab_marks: list, el_marks: list):
    best_2_test_marks = sorted(test_marks, reverse=True)[:2]
    best_2_quiz_marks = sorted(quiz_marks, reverse=True)[:2]
    total_test_marks = sum(best_2_test_marks)
    total_quiz_marks = sum(best_2_quiz_marks) / 2
    total_matlab_marks = sum(lab_marks)
    total_el_marks = sum(el_marks)
    total_marks = float(total_test_marks) * 0.3 + float(total_quiz_marks) + float(total_matlab_marks) + float(
        total_el_marks)
    total_marks_rounded = round(total_marks, 2)
    return total_marks_rounded


def calculate_caeg_cie_marks(test_marks: list, lab_marks: list, el_marks: list):
    best_2_test_marks = sorted(test_marks, reverse=True)[:2]
    total_test_marks = sum(best_2_test_marks)
    total_lab_marks = sum(lab_marks)
    total_el_marks = sum(el_marks)
    total_marks = float(total_test_marks) * 0.2 + float(total_lab_marks) * 0.4 + float(total_el_marks)
    total_marks_rounded = round(total_marks, 2)
    return total_marks_rounded


def calculate_yoga_cie_marks(quiz_marks: list, lab_test_marks: list, el_marks: list):
    total_quiz_marks = sum(quiz_marks)
    total_lab_test_marks = sum(lab_test_marks)
    total_el_marks = sum(el_marks)
    total_marks = float(float(total_quiz_marks) * 2.5 + float(total_lab_test_marks)) * 0.4 + float(total_el_marks)
    total_marks_rounded = round(total_marks, 2)
    return total_marks_rounded


def calculate_english_cie_marks(test_marks: list, el_marks: list):
    total_test_marks = sum(test_marks)
    total_el_marks = sum(el_marks)
    total_marks = float(total_test_marks) * 0.4 + float(total_el_marks)
    total_marks_rounded = round(total_marks, 2)
    return total_marks_rounded


def calculate_ic_cie_marks(test_marks: list, quiz_marks: list, el_marks: list):
    best_2_test_marks = sorted(test_marks, reverse=True)[:2]
    best_2_quiz_marks = sorted(quiz_marks, reverse=True)[:2]
    total_test_marks = sum(best_2_test_marks)
    total_quiz_marks = sum(best_2_quiz_marks) / 2
    total_el_marks = sum(el_marks)
    total_marks = float(total_test_marks) * 0.3 + float(total_quiz_marks) + float(total_el_marks)
    total_marks_rounded = round(total_marks, 2)
    return total_marks_rounded

@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')