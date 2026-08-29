def calculate_average(grades: list):
    total = 0
    count = 0

    for grade in grades:
        if type(grade) == int or type(grade) == float:
            total += grade
            count += 1

    if count == 0:
        return 0

    return total / count


def calculate_weighted_grade(categories: dict):
    final_grade = 0
    active_weight = 0

    for category in categories:
        weight = categories[category]["weight"]
        grades = categories[category]["grades"]

   
        if len(grades) > 0:
            average = calculate_average(grades)

            final_grade += average * weight
            active_weight += weight

    if active_weight == 0:
        return 0
    
    return round(final_grade / active_weight, 2)
