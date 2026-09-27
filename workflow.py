import json

print("Student Study Rule-Based Workflow")
print("----------------------------------")

# Load private student data
with open("private_data.json", "r") as file:
    data = json.load(file)

question = input("Ask your question: ").lower()

# Rule 1: Attendance
if "attendance" in question:
    for subject, details in data["subjects"].items():
        print(f"{subject}: {details['attendance']}% attendance")

# Rule 2: Internal marks
elif "mark" in question or "marks" in question:
    for subject, details in data["subjects"].items():
        print(f"{subject}: {details['internal_mark']} internal mark")

# Rule 3: Student information
elif "name" in question:
    print("Student Name:", data["student_name"])

elif "department" in question:
    print("Department:", data["department"])

elif "semester" in question:
    print("Semester:", data["semester"])

# Default rule
else:
    print("Sorry, I can answer only predefined student-data questions.")
    