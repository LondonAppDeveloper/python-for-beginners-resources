student_count = {
    'course1': 923,
    'course2': 7738,
    'course3': 112,
}
# Loop through items in dictionary
for k, v in student_count.items():
    print(f'{k}: {v}')

# Count the total number of students
total_students = 0
for k, v in student_count.items():
    total_students += v

print(f'Total Students: {total_students}')

# Get all keys from dictionary
courses = student_count.keys()
print(courses)