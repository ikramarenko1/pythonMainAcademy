# Приклад виводу для висоти піраміди 5

def print_pyramid(height):
    for i in range(1, height + 1):
        print(' ' * (height - i) + '*' * (2 * i - 1) + ' ' * (height - i))

        
print_pyramid(5)