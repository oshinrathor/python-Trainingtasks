import shutil
import datetime
import os

# Define source and destination paths
source_file = 'sales.csv'
backup_folder = 'backup'

# Ensure the backup directory exists
os.makedirs(backup_folder, exist_ok=True)

# Create a dated filename
today = datetime.datetime.now().strftime('%Y-%m-%d')
backup_filename = f"data_backup_{today}.csv"
backup_path = os.path.join(backup_folder, backup_filename)

# Copy the file
shutil.copy2(source_file, backup_path)

print(f"Backup completed: {backup_path}")
