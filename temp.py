import pandas as pd
import numpy as np

# Number of student records
total_students = 500

# Number of lectures
num_lectures = 10

# Generate student roll numbers
roll_numbers = ['R' + str(i).zfill(4) for i in range(1, total_students + 1)]

# Generate lecture names
lecture_names = ['Lecture ' + str(i) for i in range(1, num_lectures + 1)]

# Generate student attendance for each lecture
attendance = np.random.randint(0, 31, size=(total_students, num_lectures))

# Calculate total attendance and attendance percentage
total_attendance = np.sum(attendance, axis=1)
attendance_percentage = (total_attendance / (num_lectures * 30)) * 100

# Generate student mail IDs
student_emails = ['student' + str(i).zfill(3) + '@example.com' for i in range(1, total_students + 1)]

# Generate parents mail IDs
parents_emails = ['parent' + str(i).zfill(3) + '@example.com' for i in range(1, total_students + 1)]

# Create DataFrame for student records
df = pd.DataFrame({
    'Roll Number': np.repeat(roll_numbers, num_lectures),
    'Lecture Name': np.tile(lecture_names, total_students),
    'Attendance (out of 30)': attendance.flatten(),
    'Attendance Percentage': np.repeat(attendance_percentage, num_lectures),
    'Student Email': np.repeat(student_emails, num_lectures),
    'Parent Email': np.repeat(parents_emails, num_lectures)
})

# Identify defaulters
defaulter_mask = (attendance_percentage < 40)
defaulter_indices = np.random.choice(np.where(defaulter_mask)[0], size=int(0.2 * total_students), replace=False)

# Mark defaulters
df.loc[df.index.isin(defaulter_indices), 'Attendance Percentage'] = 0  # Set attendance percentage to 0 for defaulters

# Save DataFrame to Excel file
df.to_excel('student_defaulter_attendance.xlsx', index=False)
