input_file = 'full_book.txt'

# Read and clean the lines
with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Process each line: strip spaces and replace tabs
cleaned_lines = [line.strip().replace('\t', '    ') for line in lines]  # Replace tabs with 4 spaces

# Write the cleaned lines back to the file (or to a new file if desired)
with open(input_file, 'w', encoding='utf-8') as f:
    for line in cleaned_lines:
        f.write(line + '\n')

print("Text formatting complete.")
