# Виведіть поточний час та дату з використанням модулю datetime.
from datetime import datetime

current = datetime.now()

print(f"Час та дата на момент запуску програми: {current.strftime('%Y-%m-%d %H:%M:%S')}")

