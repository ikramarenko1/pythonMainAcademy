# def add(a,b):
#     return a+b
#
# print(add(1,2))
# import sys


# def greet(last_name, first_name):
#     print(f"Hi {first_name} {last_name}")
#
#
# greet(last_name="Smith", first_name="John")
#
#
# def sub(b, a):
#     print(b - a)
#
#
# sub(a=1, b=2)

# def power(base, exponent=2):
#     return base ** exponent
#
#
# print(power(2, 3))

# def calculate_sum(*args):
#     total = 0
#     for num in args:
#         total += num
#     print(total)
#     return total
#
# calculate_sum()
# def get_id_user():

# def print_me(string='Hello'):
#     return string
#
#
# def print_all(func,string=''):
#     b = func()
#     print(f"{b} {string}")
#
# print_all(print_me, "Bye")

# def print_info(arg1, *args):
#     print("Output is: ")
#     print(arg1)
#     for arg in args:
#         print(arg)
#     return arg1
#
# print_info("Hello")


# def myfunc(a, b, c, q, *args, **kwargs, ):
#     print(a)
#     print(b)
#     print(c)
#     print(q)
#     print(args)
#     print(kwargs)
#
#
# a = {
#     'name': 'John',
#     'age': 36,
#     'country': 'Norway'
# }
# myfunc(a,1, 2, 3, 4, 5, 6, 7, 8, 93)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# min_values = min(numbers)
# max_values = max(numbers)
# print(min_values)
# print(max_values)
#
# print(min(1,2,3))
# print(max(1,2,3))


# strings=['apple','banana','orange','k','pineapple']
# min_length = min(strings, key=len)
# max_length = max(strings, key=len)
# print(min_length)
# print(max_length)


# num_scop=[[1111,2,3],[4,51,6],[7,8,9]]
# min_num = min(num_scop, key=sum)
# print(min_num)

# num_scop = [[11,0,0],[132123123123123123],[1,2,3],[4,5,6],[7,8,9]]
# min_num = max(num_scop, key=lambda x: [sum(x),len(x)])
# print(min_num)

# def custom_print(*objects, sep='-', end='...', file=sys.stdout):
#     output =sep.join(str(obj) for obj in objects)+end
#     print(output, file=file)
#
# custom_print("Hello","World","!")
# custom_print("Hello","World","!",sep=' ',end='\n')

# def calculate_sum(a, b, c):
#     return a + b + c
#
# data = (10, 20, 30)
# result = calculate_sum(*data)
# print(result)


# def modify_list(lst):
#     lst.append(4)
#     print("Inside function:", lst)
#
# my_list = [1, 2, 3]
# modify_list(my_list)
# print("Outside function:", my_list)

# def calculate_average(grades: list) -> float:
#     total = sum(grades)
#     average = total / len(grades)
#     print(average)


