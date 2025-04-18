import json

input_file = 'data.txt'
output_file = 'students.json'

# Read the lines from the text file
with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Extract headers from the first line
headers = lines[0].strip().split(',')

# Convert each subsequent line into a dictionary
students = []
for line in lines[1:]:
    values = line.strip().split(',')
    student = dict(zip(headers, values))
    students.append(student)

# Write to a JSON file
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(students, f, indent=4)

print(f"Converted data saved to: {output_file}")
