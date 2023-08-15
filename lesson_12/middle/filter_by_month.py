# Завдання: Відфільтрувати дати за місяцем
# Дано список дат у форматі 'YYYY-MM-DD'. Створіть список дат, які належать до вказаного місяця.
from datetime import datetime

dates = [
    '2023-08-12', '2024-08-15', '2022-08-21',
    '2023-11-30', '2023-11-25', '2024-01-01',
    '2024-01-14', '2024-03-20', '2024-03-15',
    '2024-05-30'
]
month_filter_by = 1
filtered_dates = [date for date in dates if datetime.strptime(date, '%Y-%m-%d').month == month_filter_by]

print(filtered_dates)