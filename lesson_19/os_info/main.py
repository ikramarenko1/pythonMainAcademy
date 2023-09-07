# Виведіть інформацію про поточну операційну систему з використанням модулю os.
import os

os_info = {
    'Назва': os.name,
    'Загальна iнформацiя': os.uname(),
    'Поточна робоча директорiя': os.getcwd(),
    'Ідентифікатор процесу (PID)': os.getpid()
}

for key, value in os_info.items():
    print(f'{key}: {value}')
