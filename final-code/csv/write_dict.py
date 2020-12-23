import os
import csv

current_dir = os.getcwd()
output_dir_path = os.path.join(current_dir, 'output')
os.makedirs(output_dir_path, exist_ok=True)
csv_file_path = os.path.join(output_dir_path, 'store.csv')

with open(csv_file_path, 'w', newline='') as csv_file:
    header = ['Product', 'Id', 'Quantity']
    writer = csv.DictWriter(csv_file, header)
    writer.writeheader()
    writer.writerow({'Product': 'Beans', 'Quantity': 1000, 'Id': 1,})
    writer.writerows([
        {'Product': 'Rice', 'Id': 2, 'Quantity': 500},
        {'Product': 'Hot Sauce', 'Id': 3, 'Quantity': 600},
    ])