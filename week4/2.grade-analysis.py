student_grades = [92, 95, 34, 34, 56, 78, 87, 65, 34, 22, 98, 13, 67, 89]

# First method
total_grades = sum(student_grades)
print(total_grades)

# Second method
total = 0

for student_grade in student_grades:
    total += student_grade

print(total)

# Find the highest grade
highest_grade = 0

for grade in student_grades:
    if grade > highest_grade:
        highest_grade = grade

print(highest_grade)
