# Обчисліть площу трикутника за допомогою лямбда-функції
# За допомогою основи та висоти: (основа * висоту) / 2
calculate_triangle = lambda base, height: (base * height) / 2

base = float(input('Введіть основу трикутника: '))
height = float(input('Введіть висоту трикутника: '))

print(f'Площа трикутника з основою {base} та висотою {height} = {calculate_triangle(base, height)}')
