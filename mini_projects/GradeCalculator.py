#Building a grade calculator simulation for students. Based on their marks they will recieve grades and a overall result. 
def calculate_grade(marks):
    if marks >= 80:
        return 'A'
    elif marks >= 60:
        return 'B'
    elif marks >= 40:
        return 'C'
    else:
        return 'D'


name = input("Enter your name: ")

marks = []
for i in range(1, 6):
    m = int(input(f"Enter marks for subject {i}: "))
    marks.append(m)

print("\nYour Grades:")
for i in range(5):
    print(f"Subject {i+1}: {calculate_grade(marks[i])}")

average = sum(marks) / len(marks)

if average >= 40:
    result = "PASS"
else:
    result = "FAIL"

print(f"\nAverage Marks: {average:.2f}")
print("Overall Result:", result)

    