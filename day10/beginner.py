import os

filename = "unified.txt"

# 1. Write initial tasks to the file (overwrites if exists)
print("Writing initial tasks to 'unified.txt'...")
tasks = [
    "Buy groceries",
    "Call the bank",
    "Study for math test",
    "Walk the dog",
    "Water the plants"
]

with open(filename, "w") as file:
    for task in tasks:
        file.write(task + "\n")

print("5 tasks written.\n")

# 2. Append a new task to the same file
print("Appending a new task to 'unified.txt'...")
new_task = "Finish Python project"
with open(filename, "a") as file:
    file.write(new_task + "\n")

print("New task appended.\n")

# 3. Check if the file exists before reading
print("Checking if 'unified.txt' exists...")
if os.path.exists(filename):
    print("File exists. Proceeding to read...\n")
else:
    print("File does not exist. Exiting.")
    exit()

# 4. Read the file line by line
print("Reading file line-by-line:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())

# 5. Count the number of lines in the file
print("\nCounting lines in 'unified.txt'...")
with open(filename, "r") as file:
    lines = file.readlines()
    print(f"Total lines: {len(lines)}")
