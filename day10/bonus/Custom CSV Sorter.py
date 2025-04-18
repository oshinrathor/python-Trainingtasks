import csv

input_file = 'sales.csv'
output_file = 'high_sales.csv'

# Read the CSV into a list of dictionaries
with open(input_file, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    products = list(reader)

# Sort by 'Amount' (make sure to convert it to float)
products_sorted = sorted(products, key=lambda x: float(x['Amount']))

# Write sorted data back to a new CSV
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=products_sorted[0].keys())
    writer.writeheader()
    writer.writerows(products_sorted)

print(f"Sorted products written to: {output_file}")
