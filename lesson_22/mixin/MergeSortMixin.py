# Реалізація складних алгоритмів обчислення:
# Створіть мікс, який дозволяє об'єкту виконувати складні обчислення або алгоритми,
# наприклад, для оптимізації обробки великих обсягів даних.
class MergeSortMixin:
    def merge_sort(self, data):
        if len(data) <= 1:
            return data

        mid = len(data) // 2
        left_data = self.merge_sort(data[:mid])
        right_data = self.merge_sort(data[mid:])

        return self.merge(left_data, right_data)

    def merge(self, left, right):
        result = []
        left_idx, right_idx = 0, 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1

        result += left[left_idx:]
        result += right[right_idx:]

        return result


class MyDataProcessor(MergeSortMixin):
    def __init__(self, data):
        self.data = data

    def process_data(self):
        self.data = self.merge_sort(self.data)


processor = MyDataProcessor([4, 7, 1, 3, 9, 0])

processor.process_data()
print(processor.data)
