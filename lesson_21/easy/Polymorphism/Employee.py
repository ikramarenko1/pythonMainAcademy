# Створіть клас Employee з методом calculate_salary().
# Створіть підкласи Manager та Developer, які успадковують Employee та реалізовують свої
# власні методи calculate_salary(). Створіть список з працівниками обох типів та викличте
# метод calculate_salary() для кожного.
class Employee:
    def __init__(self, base_rate, hours_worked):
        self.base_rate = base_rate  # ставка в годину
        self.hours_worked = hours_worked  # годин вiдпрацьовано

    def calculate_salary(self):
        return self.base_rate * self.hours_worked


class Manager(Employee):
    def __init__(self, base_rate, hours_worked, num_projects):
        super().__init__(base_rate, hours_worked)
        self.num_projects = num_projects  # кiлькiсть проектiв

    def calculate_salary(self):
        bonus = 250 * self.num_projects
        return super().calculate_salary() + bonus


class Developer(Employee):
    def __init__(self, base_rate, hours_worked, overtime_hours):
        super().__init__(base_rate, hours_worked)
        self.overtime_hours = overtime_hours  # кiлькiсть перепрацьованих годин

    def calculate_salary(self):
        overtime_pay = 1.5 * self.base_rate * self.overtime_hours
        return super().calculate_salary() + overtime_pay


employees = [
    Manager(50, 160, 3),
    Developer(50, 250, 10)
]

salaries = [(type(employee).__name__, employee.calculate_salary()) for employee in employees]

for salary in salaries:
    print(salary)
