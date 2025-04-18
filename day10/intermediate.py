import os

filename = "data.txt"

# Task 1: Remove blank lines and save cleaned content
print("Task 1: Removing blank lines...")
with open(filename, "r") as file:
    lines = file.readlines()

cleaned_lines = [line for line in lines if line.strip()]
with open(filename, "w") as file:
    file.writelines(cleaned_lines)
print("Blank lines removed.\n")

# Task 2: Replace 'Python' with 'PYTHON'
print("Task 2: Replacing 'Python' with 'PYTHON'...")
with open(filename, "r") as file:
    content = file.read().replace("Python", "PYTHON")

with open(filename, "w") as file:
    file.write(content)
print("Replacement done.\n")

# Task 3: Convert entire file content to uppercase
print("Task 3: Converting content to uppercase...")
with open(filename, "r") as file:
    content = file.read().upper()

with open(filename, "w") as file:
    file.write(content)
print("Uppercase conversion done.\n")

# Task 4: Student report: Add Pass/Fail based on Marks >= 50
print("Task 4: Generating student pass/fail report...")
report_lines = []
with open(filename, "r") as file:
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 2:
            name, mark_str = parts
            try:
                mark = float(mark_str)
                status = "PASS" if mark >= 50 else "FAIL"
                report_lines.append(f"{name},{mark_str},{status}\n")
            except ValueError:
                continue  # Skip lines that aren't valid marks

# Append report to file
with open(filename, "a") as file:
    file.write("\nSTUDENT REPORT:\n")
    file.writelines(report_lines)
print("Report generated and added to file.\n")

# Task 5: Reverse all lines and save to file
print("Task 5: Reversing lines in the file...")
with open(filename, "r") as file:
    lines = file.readlines()

with open(filename, "w") as file:
    file.writelines(reversed(lines))
print("Lines reversed and written back to file.\n")
