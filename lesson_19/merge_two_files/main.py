# Створіть програму, яка приймає два файли та об'єднує їх в один.
def merge_files(file1, file2, output_file):
    try:
        with open(file1, 'r') as file1:
            data1 = file1.read()

        with open(file2, 'r') as file2:
            data2 = file2.read()

        with open(output_file, 'w') as output_f:
            output_f.write(data1 + '\n' + data2)

        return 'Операцiя виконана успiшно!'

    except Exception as e:
        return f'Виникла помилка: {e}'


print(merge_files('file1.txt', 'file2.txt', 'output_file.txt'))
