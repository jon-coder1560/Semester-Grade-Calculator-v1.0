'''
    Semester Grade Calculator
    1. Enter assignment grades.
    2. Calculate the average.
    3. Reject grades outside the valid range.
    4. Display the final average and a corresponding letter grade.
'''

print("Welcome to the Semester Grade Calculator\n")

num_grades = int(
    input("How many grades would you like to enter: ")
)

while num_grades <= 0 or num_grades >= 20:
    print("Invalid Amount")
    num_grades = int(
        input("How many grades would you like to enter: ")
    )

print("") # insert a blank line

total = 0
for i in range(num_grades):
    grade = int(
        input("Please enter the grade: ")
    )

    while grade < 0 or grade > 100:
        print("Invalid Grade")
        grade = int(
            input("Please enter the grade: ")
        )
    total += grade


average = total / num_grades

print(f"\nYour semesmter average is {average:.2f}%")


