course_a = {'James', 'Brooke', 'Kath', 'Mark', 'Peter', 'Anand'}
course_b = {'Sadie', 'Suresh', 'Simon', 'Peter', 'Greg', 'Kath'}

# Students who took both courses (intersection)
intersect = course_a & course_b
print(f'Took both courses: {intersect}')

# Students from both courses combined (union)
union = course_a | course_b
print(f'All students: {union}')

# Create a set of students who took only one course (symmetric_difference)
sym_diff = course_a ^ course_b
print(f'Took one course: {sym_diff}')