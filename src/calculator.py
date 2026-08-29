
grades = [90, 80, 70, 60, 50]

def calculate_average(grades):

    total_sum = 0
    count = 0

for grade in grades:
    
    if type(grade) == int or type(grade) == float:
        total_sum += grade
        count += 1




average = calculate_average(grades)
print(average)