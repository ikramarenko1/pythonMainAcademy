# Обробка великих об'ємів даних: Створіть декоратор, який буде автоматично обробляти великі
# об'єми даних, розбиваючи їх на частини.
def handle_big_data(func):
    def wrapper(data):
        chunk_size = 10
        chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

        result = 0
        for chunk in chunks:
            result += func(chunk)

        return result
    return wrapper


@handle_big_data
def sum_list_simple(lst):
    return sum(lst)


large_list = list(range(100))
print(sum_list_simple(large_list))
