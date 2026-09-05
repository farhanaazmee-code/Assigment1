student_name = input("Enter student's name:")

mark1 = float(input("Enter marks of student 1:"))
mark2 = float(input("Enter marks of student 2:"))
mark3 = float(input("Enter marks of student 3:"))

total = mark1 + mark2 + mark3
average = total/3

if average >= 80:
    grade = "A+"
elif average >=70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

print(f"\nStudent Name:{student_name}")
print(f"Total Marks:{total:.0f}")
print(f"Average:{average:.2f}")
print(f"Grade:{grade}")