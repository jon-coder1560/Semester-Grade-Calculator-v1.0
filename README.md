# Semester Grade Calculator

## Description

The Semester Grade Calculator is a beginner-friendly Python project that calculates a student's semester average based on grades entered by the user. It uses loops and conditional statements to validate input and calculate the average.

This project was created to practice fundamental Python programming concepts, including user input, `for` loops, `while` loops, variables, and arithmetic operations.

## Features

- **Grade Input:** Enter the number of grades you want to calculate.
- **Input Validation:** Rejects invalid grade counts and grades outside the 0–100 range.
- **Average Calculation:** Calculates the average of the entered grades.
- **Formatted Output:** Displays the semester average to two decimal places.

## Requirements

- Python 3.x

No external libraries are required.

## How to Run

1. Install Python 3 if you haven't already.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the program using:

   ```bash
   python main.py
   ```

   Replace `main.py` with the name of your Python file if it is different.

## Example Output

```text
Welcome to the Semester Grade Calculator

How many grades would you like to enter: 3

Please enter the grade: 85
Please enter the grade: 90
Please enter the grade: 95

Your semester average is 90.00%
```

## What I Learned

Through this project, I practiced:

- Using `input()` to collect user information.
- Using `int()` to convert input into integers.
- Using `while` loops to validate user input.
- Using `for` loops to repeat operations.
- Calculating averages with arithmetic operations.
- Formatting output using f-strings.

## Future Improvements

- Add letter grade calculations (A, B, C, D, and F).
- Handle non-numeric input without crashing.
- Fix the grade accumulation logic so every valid grade contributes to the average.
- Display the highest and lowest grades.
- Allow users to calculate multiple semester averages without restarting the program.
