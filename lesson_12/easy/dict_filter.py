# Завдання: Фільтрація словника за умовою
# Дано словник зі студентами та їх віками. Створіть новий словник, що містить
# тільки тих студентів, вік яких менше 25 років, за допомогою Dictionary Comprehension.

students = {
    'Mikhaylo': 25,
    'Volodymyr': 22,
    'Elizaveta': 21,
    'Artem': 28,
    'Ilya': 20,
    'Maksym': 28,
    'Roman': 29
}
students_under_25 = {student: age for student, age in students.items() if age < 25}

print(students_under_25)
