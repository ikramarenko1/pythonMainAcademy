# Великі файли: Напишіть генератор, який буде читати великий текстовий файл рядок за рядком.
def read_string_by_string(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


file_path = 'file.txt'

file_reader = read_string_by_string(file_path)
first_10_lines = [next(file_reader) for _ in range(10)]

print('\n'.join(first_10_lines))
