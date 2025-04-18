# 📁 Python File Handling

This showcases my learning and practice with **file handling in Python**, covering beginner to advanced concepts through hands-on exercises, mini-projects, and utility scripts.

---

## 🧠 Concepts Covered

### ✅ Core File Handling
- Understanding how files work in Python: reading, writing, appending.
- Using `open()`, `read()`, `readline()`, and `readlines()`.
- Using `with` context managers for safe file operations.
- Closing files properly to free system resources.

### ✅ Text Processing
- Removing leading/trailing whitespace from text.
- Replacing tabs with spaces.
- Ignoring blank lines during file processing.
- Reversing lines and reformatting content.

### ✅ Working with Directories
- Using `os` and `os.path` to check file existence.
- Listing and filtering files in a directory.
- Creating folders and organizing output files.

### ✅ CSV File Operations
- Reading CSV files using `csv.reader` and `csv.DictReader`.
- Writing structured data using `csv.writer` and `csv.DictWriter`.
- Filtering CSV rows based on conditions (e.g., price, marks).
- Sorting CSV data programmatically.

### ✅ JSON Handling
- Converting structured text data to JSON format.
- Using Python dictionaries for structured data representation.
- Writing formatted JSON output using `json.dump`.

---

## 🧪 Skills Developed

- Line-by-line file iteration and text transformation.
- Basic data analytics (averaging, filtering, word frequency counting).
- Logging user input and events with timestamps.
- Backup system automation using timestamps in filenames.
- File merging, text formatting, and content organization.
- Structuring input/output into organized formats for reuse or sharing.

---

## 🚀 Projects & Mini Utilities

Throughout the journey, I built:
- An **Auto Backup System** for data versioning.
- A **Chat Logger** that records input with timestamps.
- A **Student Report Generator** that calculates pass/fail and stores output in structured format.
- A **CSV Sorter** to organize product listings by price.
- A **Log Analyzer** for extracting and summarizing error messages.
- A **Word Frequency Counter** for basic natural language processing.

---

## 💡 Key Takeaways

- **Always use `with`** for opening files – it ensures automatic closure.
- **File safety matters** – use `os.path.exists()` and handle `FileNotFoundError`.
- **Text is messy** – cleaning and formatting is essential before processing.
- **Structure matters** – converting data into JSON/CSV makes it easier to work with.
- **Practice builds confidence** – repetition across multiple file types (txt, csv, json) made operations second nature.

---