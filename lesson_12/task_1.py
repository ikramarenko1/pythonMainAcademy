# sentence = "Hello, world! How are you?"
#
# words=sentence.split()
# a=[]
# for word in words:
#     a.append(word.strip('.,?!'))
# print(a)
#
# words_even = [word.strip('.,?!') for word in sentence.split()]
# print(words_even)
# [expression for item in iterable if condition]
from pprint import pprint

# matrix = [[row * 3 + col for col in range(1,3)] for row in range(1,7,2)]
# print(matrix)
# for i in range(1,8):
#     print(i)

# text = "hello"
# uppercase_letters = [char.upper() for char in text]
# print(uppercase_letters)

# numbers = [1, 2, 3, 4, 5]
# new_list = [x if x % 2 == 0 else x * 2 for x in numbers]
# print(new_list)

# a = [-1, 3, 5, 6, -12, -2, -6]
# positive_num=[x for x in a if x>0]
# print(positive_num)
#
# text="Hello World!"
# reversed_text= ''.join([char for char in reversed(text)])
# print(reversed_text)

# sentence="apple,banana,kiwi,orange"
# words=[fruit.strip() for fruit in sentence.split(",")]
# print(words)


# new_dict = {key_expression: value_expression for item in iterable if condition}

# squares_dict = {x: x ** 2 for x in range(1, 6)}
# {1: 1, 8: 4, 27: 9, 64: 16, 125: 25}
# print(squares_dict)

# numbers_dict = {x: x ** 2 for x in range(1, 11)}
# print(numbers_dict)
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
# even_numbers_dict={key:value for key,value in numbers_dict.items() if key%2==0}
# print(even_numbers_dict)
#{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# text="hello"
# letter_position={char:index for char,index in enumerate(text)}
# print(letter_position)
#{0: 'h', 1: 'e', 2: 'l', 3: 'l', 4: 'o'}

# number_dict={
#     'a':3,
#     'b':6,
#     'c':9,
#     'd':11,
#     'q':19,
# }
# number={key:value for key,value in number_dict.items() if value>5}
# pprint(number)
# {'b': 6, 'c': 9, 'd': 11, 'q': 19}


# text='hello'
# letter_count={char:text.count(char) for char in text}
# print(letter_count)

# new_set = {expression for item in iterable if condition}

# squares_set = {x ** 2 for x in range(1, 6)}
# print(squares_set)
# print(type(squares_set))

# text = [1,2,3,5,6,7,6,5,4,3,2,1]
# unique_letters = {char for char in text}
# print(unique_letters)
#
# numbers = [1, 5, 8, 10, 3, 6, 9,10,10]
# even_numbers = {num for num in numbers if num % 2 == 0}
# print(even_numbers)

# text_1 = "hello"
# text_2 = "llone"
# common_letters = {char for char in text_1 if char in text_2}
# print(common_letters)


# list_1=[1,2,3,4]
# list_2=[3,4,5,6]
# unique_list=list(set(list_1+list_2))
# print(unique_list)

# def get_common_divisors(numbers):
#     def divisors(num):
#         return {i for i in range(1,num+1) if num%i==0}
#
#     common_divisors=divisors(numbers[0])
#
#     for num in numbers[1:]:
#         common_divisors = common_divisors&divisors(num)
#     return common_divisors
#
# numbers=[21,49,56]
# common_divisors=get_common_divisors(numbers)
# print(common_divisors)