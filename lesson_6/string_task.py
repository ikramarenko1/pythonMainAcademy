# Task 1
# Generate string with lowercase and uppercase alphabet plus numbers
# Print 1st symbol of string
# Print last symbol
# Print 3rd from start and 3rd from the end
# Slice first 8 symbols
# Print only symbols with index, which divides on 3 without remaining
# Print the symbol of the middle of the string text
# Reverse text using slice

test_string = 'Some string1234 to work with'
print(f'\n1st symbol of string - {test_string[0]}')
print(f'last symbol - {test_string[-1]}')
print(f'3rd from start and 3rd from the end - {test_string[2]} {test_string[-3]}')
print(f'first 8 symbols - {test_string[:8]}')

print(f'only symbols with index, which divides on 3 without remaining: '
      f'{[test_string[i] for i in range(len(test_string)) if i % 3 == 0 and i != 0]}')

print(f'the symbol of the middle of the string text - {test_string[len(test_string) // 2 - 1]}')

print(f'Reverse text using slice - {test_string[::-1]}')
