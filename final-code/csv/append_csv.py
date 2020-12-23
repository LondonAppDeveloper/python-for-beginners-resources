import os
import csv


current_dir = os.getcwd()
output_dir_path = os.path.join(current_dir, 'output')
os.makedirs(output_dir_path, exist_ok=True)
csv_file_path = os.path.join(output_dir_path, 'drivers.csv')


with open(csv_file_path, 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['James', 34, True, True])