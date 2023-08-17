# Завдання: Сортування словника за значенням у вкладеному словнику
# Дано словник, де ключами є імена студентів, а значеннями - словники
# з інформацією про предмети та їх бали. Відсортуйте студентів за середнім балом по всіх предметах.

students = {
    "Ilya": {"math": 95, "history": 82, "english": 95},
    "Roman": {"math": 85, "history": 82, "chemistry": 78},
    "Mykhailo": {"math": 88, "history": 85, "chemistry": 86},
    "Maksym": {"math": 92, "history": 80, "chemistry": 89}
}


def get_average_grade(student):
    grades = students[student]

    return sum(grades.values()) / len(grades)


sorted_students = sorted(students, key=get_average_grade, reverse=True)

print(sorted_students)
