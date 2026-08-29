from course import physics_1
from calculator import calculate_weighted_grade

def get_grades(category):
    user_input = input(f"Enter {category} grades separated by commas: ")

    parts = user_input.split(",")

    grades = []

    for part in parts:
        grades.append(float(part))

    return grades


for category in physics_1["categories"]:
    grades = get_grades(category)

    physics_1["categories"][category]["grades"] = grades


grade = calculate_weighted_grade(physics_1["categories"])

print("Current grade:", round(grade, 2))

