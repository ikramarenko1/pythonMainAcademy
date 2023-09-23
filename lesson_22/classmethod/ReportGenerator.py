# Генерація звіту: Напишіть класовий метод для генерації звіту на основі даних з бази даних.
import sqlite3


class ReportGenerator:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def fetch_data(self, query, parameters=None):
        if parameters:
            self.cursor.execute(query, parameters)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    @classmethod
    def generate_report(cls, db_name):
        report_generator = cls(db_name)

        data = report_generator.fetch_data('SELECT * FROM users')

        report = 'ЗВІТ:\n'
        for row in data:
            report += f'{row}\n'

        report_generator.connection.close()

        return report


report = ReportGenerator.generate_report('my_database.db')

print(report)
