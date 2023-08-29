# Реалізуйте рекурсивну функцію для знаходження всіх перестановок
# символів у рядку.
def string_permutations(s):
    if len(s) == 0 or len(s) == 1:
        return [s]

    permutations = []

    for i in range(len(s)):
        char = s[i]
        remaining_str = s[:i] + s[i + 1:]
        remaining_permutations = string_permutations(remaining_str)

        for perm in remaining_permutations:
            permutations.append(char + perm)

    return permutations


print(string_permutations("hello"))
