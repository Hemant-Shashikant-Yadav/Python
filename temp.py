import random
import pandas as pd

# List of sample student names
boy_names = ["Michael", "John", "Robert", "William", "David", "Joseph", "Daniel", "James", "John", "Matthew"]
girl_names = ["Mary", "Jennifer", "Linda", "Patricia", "Elizabeth", "Susan", "Jessica", "Sarah", "Karen", "Nancy"]

def generate_student_records(num_records):
    records = []
    for i in range(num_records):
        roll_number = f"R{i + 1:03}"
        name = random.choice(boy_names) if i % 2 == 0 else random.choice(girl_names)
        gender = "Male" if i % 2 == 0 else "Female"
        attendance_out_of_30_days = random.randint(15, 30)
        attendance_percentage = (attendance_out_of_30_days / 30) * 100
        student_mail_id = f"student{i + 1}@example.com"
        parent_mail_id = f"parent{i + 1}@example.com"
        records.append([roll_number, name, gender, attendance_out_of_30_days, attendance_percentage, student_mail_id, parent_mail_id])
    return records

def introduce_defaulters(records):
    num_defaulters = int(0.2 * len(records))
    defaulter_indices = random.sample(range(len(records)), num_defaulters)
    for idx in defaulter_indices:
        records[idx][4] = random.randint(0, 39)  # Set attendance percentage of defaulters less than 40%

def generate_excel(records):
    df = pd.DataFrame(records, columns=["Roll Number", "Name", "Gender", "Attendance out of 30 days", "Attendance Percentage", "Student Mail ID", "Parent Mail ID"])
    df.to_excel("FY_A_ML2.xlsx", index=False)
    print("Excel file generated successfully.")

def main():
    num_records = 500
    records = generate_student_records(num_records)
    introduce_defaulters(records)
    generate_excel(records)

if __name__ == "__main__":
    main()
