# Перевірка ключа: Створіть програму, яка приймає текстовий файл "grades.txt" зі
# списком студентів і їх оцінками. Зчитайте файл та перевірте, чи є у ньому запис про певного студента за іменем.
def check_student(name):
    with open('grades.txt', 'r') as file:
        for line in file.readlines():
            if line.split()[0].lower() == name.lower():
                return True

    return False


print(check_student('John'))
print(check_student('sasha'))
print(check_student('Ivan'))
