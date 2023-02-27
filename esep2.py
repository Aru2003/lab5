grades = {
    'Иванов': [4, 5, 3, 4],
    'Петров': [3, 4, 4, 5],
    'Сидоров': [5, 5, 4, 5]
}
def get_grades_by_student(name, grades_dict):
    if name in grades_dict:
        return grades_dict[name]
    else:
        return []

ivanov_grades = get_grades_by_student('Иванов', grades)
print(ivanov_grades)  # [4, 5, 3, 4]
smith_grades = get_grades_by_student('Смит', grades)
print(smith_grades)  # []
