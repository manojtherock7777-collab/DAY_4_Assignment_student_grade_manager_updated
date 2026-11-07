
import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Student Marks Calculator",
    page_icon="🎓",
    layout="centered"
)

# Initialize student storage
if "students" not in st.session_state:
    st.session_state.students = []

# Grade calculation function
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

# Application title
st.title("🎓 Student Marks and Grade Calculator")
st.write("Enter student details and calculate grades automatically.")

st.divider()

# Student input section
st.subheader("📝 Enter Student Details")

with st.form("student_form"):
    name = st.text_input("Student Name")

    marks = st.number_input(
        "Enter Marks (0-100)",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=1.0
    )

    submit = st.form_submit_button("Add Student")

    if submit:
        if name.strip():
            student = {
                "Name": name.strip(),
                "Marks": marks,
                "Grade": calculate_grade(marks)
            }

            st.session_state.students.append(student)
            st.success(f"Student {name} added successfully!")
        else:
            st.error("Please enter student name.")

st.divider()

# Display student results
st.subheader("📊 Student Results")

if st.session_state.students:

    df = pd.DataFrame(st.session_state.students)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    # Calculate class statistics
    total_students = len(df)
    average = df["Marks"].mean()
    highest = df["Marks"].max()
    lowest = df["Marks"].min()

    # Display metrics
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Students", total_students)
    col2.metric("Class Average", f"{average:.2f}")
    col3.metric("Highest Marks", f"{highest:.2f}")
    col4.metric("Lowest Marks", f"{lowest:.2f}")

    # Grade distribution
    st.subheader("📈 Grade Distribution")

    grade_counts = df["Grade"].value_counts()

    st.bar_chart(grade_counts)

    # Download results
    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Student Results",
        data=csv,
        file_name="student_results.csv",
        mime="text/csv"
    )

    # Clear records
    if st.button("🗑️ Clear All Records"):
        st.session_state.students = []
        st.rerun()

else:
    st.info("No student records available. Please add students.")

st.divider()

st.caption("Student Marks and Grade Calculator | Built with Python and Streamlit")
