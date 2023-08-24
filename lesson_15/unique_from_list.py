# Задача зі списками: Напишіть програму, яка видаляє дублікати зі списку і залишає лише унікальні значення.
def get_unique(user_list):
    return list(set(user_list))


user_input = map(int, input('Введiть список чисел через пробiл для тесту: ').split())

print(f'Список з унiкальними числами: {get_unique(user_input)}')
