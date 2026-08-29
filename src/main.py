from course import physics_1
from calculator import calculate_weighted_grade

def get_grades(category):
    while True:
        user_input = input(
            f"Enter {category} grades separated by commas: "
        )

        user_input = user_input.strip()

        if user_input == "":
            return []

        parts = user_input.split(",")
        grades = []

        try:
            for part in parts:
                part = part.strip()

                if part == "":
                    continue

                grade = float(part)

                if grade < 0 or grade > 100:
                    raise ValueError

                grades.append(grade)

            if len(grades) == 0:
                print("Please enter at least one valid grade.")
                continue

            return grades

        except ValueError:
            print("Invalid input. Enter numbers from 0 to 100 separated by commas.")

            

for category in physics_1["categories"]:
    grades = get_grades(category)

    physics_1["categories"][category]["grades"] = grades


grade = calculate_weighted_grade(physics_1["categories"])

print("Current grade:", round(grade, 2))

