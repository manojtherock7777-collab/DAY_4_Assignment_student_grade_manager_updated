
# Student Marks and Grade Calculator

# Store student details
students = []

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


# Get number of students
total_students = int(input("Enter number of students: "))

# Collect student information
for i in range(total_students):
    print(f"\nStudent {i + 1}")

    name = input("Enter student name: ")
    marks = float(input("Enter marks (0-100): "))

    if marks < 0 or marks > 100:
        print("Invalid marks! Please enter marks between 0 and 100.")
        continue

    grade = calculate_grade(marks)

    students.append({
        "name": name,
        "marks": marks,
        "grade": grade
    })


# Display student results
print("\n========== STUDENT RESULTS ==========")
print(f"{'Name':<20} {'Marks':<10} {'Grade':<10}")
print("-" * 40)

for student in students:
    print(
        f"{student['name']:<20} "
        f"{student['marks']:<10.2f} "
        f"{student['grade']:<10}"
    )

# Calculate class average
if students:
    average = sum(s["marks"] for s in students) / len(students)
    print("-" * 40)
    print(f"Class Average: {average:.2f}")

print("\n========== END OF RESULTS ==========")