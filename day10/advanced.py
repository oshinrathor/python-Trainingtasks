import os
import re
import csv
from collections import Counter

# # Task 1: Log File Analyzer
log_filename = "server.log"
error_count = 0
error_lines = []

print("Task 1: Analyzing 'server.log' for ERROR entries...")

if os.path.exists(log_filename):
    with open(log_filename, "r") as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
                error_lines.append(line)

    with open("errors_only.log", "w") as errorfile:
        errorfile.writelines(error_lines)

    print(f"Total ERROR lines found: {error_count}\n")
else:
    print(f"{log_filename} not found for Task 1.\n")

# # Task 2: Word Frequency Counter
story_filename = "story.txt"
word_frequency = {}

print("Task 2: Counting word frequency in 'story.txt'...")

if os.path.exists(story_filename):
    with open(story_filename, "r") as file:
        text = file.read().lower()  # Read and convert to lowercase to count words uniformly
        words = re.findall(r'\b\w+\b', text)  # Find all words (handles punctuation)
        
        # Count word frequencies using Counter
        word_frequency = dict(Counter(words))

    # Write word frequencies to frequency.txt
    with open("frequency.txt", "w") as freq_file:
        for word, count in sorted(word_frequency.items()):
            freq_file.write(f"{word}: {count}\n")

    print("Word frequency written to 'frequency.txt'.\n")
else:
    print(f"{story_filename} not found for Task 2.\n")


# # Task 3: CSV Reader + Filter
# # Read and filter sales above ₹10,000
high_sales = []
with open('sales.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        amount = int(row['Amount'])
        if amount > 10000:
            high_sales.append(row)

# Display filtered sales
print("Sales above ₹10,000:")
for sale in high_sales:
    print(sale)

# Write filtered sales to a new CSV
with open('high_sales.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["Date", "Customer", "Product", "Amount"])
    writer.writeheader()
    writer.writerows(high_sales)


# # Task 4: Merge Multiple Files
# # List of chapter files to merge
chapters = ['chapter1.txt', 'chapter2.txt']

# Open full_book.txt in write mode
with open('full_book.txt', 'w', encoding='utf-8') as output_file:
    for chapter in chapters:
        with open(chapter, 'r', encoding='utf-8') as file:
            content = file.read()
            output_file.write(content + '\n')  # Add a newline after each chapter

# Task 5: Directory File Scanner
# Specify the folder path
folder_path = r'C:\Users\hp\OneDrive\Desktop\gla\softwareDEV\python-training(Personal)'  # Example: 'C:/Users/YourName/Documents'

# List all items in the folder
all_files = os.listdir(folder_path)

# Filter only .txt and .csv files
for file in all_files:
    if os.path.isfile(os.path.join(folder_path, file)) and (file.endswith('.txt') or file.endswith('.csv')):
        print(file)

