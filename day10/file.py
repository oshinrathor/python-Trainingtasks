import csv
import os

filename = "students.csv"

# Step 1: Create file with headers if it doesn't exist
if not os.path.exists(filename):
    with open(filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age', 'Grade'])

# Step 2: Take user input for multiple students
print("Enter student details. Type 'done' as name to finish.")

while True:
    name = input("Name: ")
    if name.lower() == 'done':
        break
    try:
        age = int(input("Age: "))
        grade = float(input("Grade: "))
    except ValueError:
        print("Invalid age or grade. Please try again.")
        continue

    # Save to file
    with open(filename, "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, age, grade])

print("\nData saved successfully.\n")

# Step 3: Read and display all students
print("All Students:")
with open(filename, "r") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    print(f"{header[0]:<15} {header[1]:<5} {header[2]:<6}")
    print("-" * 30)
    for row in reader:
        print(f"{row[0]:<15} {row[1]:<5} {row[2]:<6}")

# Step 4: Calculate and display average grade
total_grade = 0
student_count = 0

with open(filename, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            total_grade += float(row['Grade'])
            student_count += 1
        except ValueError:
            continue

if student_count > 0:
    average_grade = total_grade / student_count
    print(f"\nAverage grade of all students: {average_grade:.2f}")
else:
    print("\nNo valid student data found to calculate average.")

# Step 5: Filter students above a certain grade
try:
    threshold = float(input("\nEnter grade threshold to find top students: "))
except ValueError:
    print("Invalid input. Exiting.")
    exit()

print(f"\nStudents with grade above {threshold}:")
with open(filename, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    found = False
    for row in reader:
        try:
            if float(row['Grade']) > threshold:
                print(f"{row['Name']} - Grade: {row['Grade']}")
                found = True
        except ValueError:
            continue

    if not found:
        print("No students found above the threshold.")

# Step 6: Clear the file after all operations (except headers)
with open(filename, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Age', 'Grade'])

print("\nStudent data has been cleared. Program will start fresh next time.")
