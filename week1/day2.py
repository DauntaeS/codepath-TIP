def is_acronym(words, s):
    acronym = "".join(word[0] for word in words)
    print(acronym)

    return acronym == s


def make_divisible_by_3(nums):

    count = 0

    for num in nums:
        if num % 3 == 1:
            count += 1
        elif num % 3 == 2:
            count += 1

    print(count)


def exclusive_elemts(lst1, lst2):

    result = []

    for item in lst1:
        if item not in lst2:
            result.append(item)

    for value in lst2:
        if value not in lst1:
            result.append(value)

    print(result)


def count_digits(n):
    s = str(n)
    count = 0

    for i in s:
        count += 1

    return count


def move_zeroes(nums):
    result = []
    zeros = []

    for num in nums:
        if num != 0:
            result.append(num)
        else:
            zeros.append(num)

    for z in zeros:
        result.append(z)

    return result


def reverse_vowels(s):
    vowels = set("aeiouAEIOU")  # creates a dict
    s = list(s)  # creates an arr
    i, j = 0, len(s) - 1

    while i < j:
        if s[i] in vowels and s[j] in vowels:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        if s[i] not in vowels:
            i += 1
        if s[j] not in vowels:
            j -= 1

    return "".join(s)


def highest_altitude(gain):
    # Im not sure
    pass


def left_right_difference(nums):
    pass


def common_elements(lst1, lst2):
    dict = {}
    result = []

    for i in lst1:
        if i not in dict:
            dict[i] = 1

    for j in lst2:
        if j in dict:
            result.append(j)

    return result


def expose_superman(trust, n):
    pass


def transpose(matrix):
    pass


def reverse_list(lst):
    if lst == 0:
        return False
    i, j = 0, len(lst) - 1

    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1

    return lst


def remove_dupes(items):
    i, j = 0, 1

    while j < len(items):
        if items[i] != items[j]:
            i += 1
            j += 1
        elif items[i] == items[j]:
            items.pop(j)
            i += 1
            j += 1
    return len(items)


def sort_by_parity(nums):
    result = []
    odds = []

    for num in nums:
        if num % 2 == 0:
            result.append(num)
        else:
            odds.append(num)

    for val in odds:
        result.append(val)

    return result


def most_honey(height):
    left, right = 0, len(height) - 1
    max_vol = 0

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_vol = max(max_vol, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_vol


def merge_intervals(intervals):
    pass


def add_matrices(matrix1, matrix2):
    sum_matrix = []

    for i in range(len(matrix1)):
        new_row = []

        for j in range(len(matrix1[i])):
            new_row.append(matrix1[i][j] + matrix2[i][j])

        sum_matrix.append(new_row)

    return sum_matrix


def is_palindrome(s):
    # if palindrome return True else False
    # string only contains lowercase characters
    # must use two pointer approach

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def squash_spaces(s):
    pass


s = "   Up,     up,   and  away! "
squash_spaces(s)

s = "With great power comes great responsibility."
squash_spaces(s)
