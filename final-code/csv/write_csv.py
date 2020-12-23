import os
import csv


current_dir = os.getcwd()
output_dir_path = os.path.join(current_dir, 'output')
os.makedirs(output_dir_path, exist_ok=True)
csv_file_path = os.path.join(output_dir_path, 'drivers.csv')

with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Driver Name', 'Age', 'Passed Theory', 'Passed Practical'])
    writer.writerows([
        ['Daisy', 22, True, False],
        ['Sadie', 26, True, False],
        ['Diva', 30, False, False],
    ])