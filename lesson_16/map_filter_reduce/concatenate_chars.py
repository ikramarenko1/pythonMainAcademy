# Об'єднати символи рядка в одну строку за допомогою reduce.
from functools import reduce

string = 'sad wa d asa w das'

concatenate_string = lambda string: reduce(lambda char1, char2: char1 + char2 if char2 != ' ' else char1, string)

print(concatenate_string(string))
