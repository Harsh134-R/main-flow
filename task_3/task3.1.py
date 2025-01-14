def multiplication_table(n):
    print(f"Multiplication Table for {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
    print()


def swap_numbers(a, b):
    print(f"Original numbers: a = {a}, b = {b}")
    a, b = b, a
    print(f"Swapped numbers: a = {a}, b = {b}")
    print()


def check_substring(s1, s2):
    result = s2 in s1
    print(f"Is '{s2}' a substring of '{s1}'? {result}")
    print()


def decimal_to_binary(n):
    binary = bin(n)[2:]
    print(f"Decimal {n} in binary is {binary}")
    print()


def add_matrices(mat1, mat2):
    print("Matrix 1:")
    for row in mat1:
        print(row)
    print("Matrix 2:")
    for row in mat2:
        print(row)

    rows, cols = len(mat1), len(mat1[0])
    result = [[mat1[i][j] + mat2[i][j] for j in range(cols)] for i in range(rows)]
    print("Sum of Matrices:")
    for row in result:
        print(row)
    print()


def multiply_matrices(A, B):
    rows_A, cols_A = len(A), len(A[0])
    cols_B = len(B[0])
    result = [[0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    print("Matrix Multiplication Result:")
    for row in result:
        print(row)
    print()


def second_largest(nums):
    unique_nums = list(set(nums))
    unique_nums.sort()
    second = unique_nums[-2] if len(unique_nums) > 1 else None
    print(f"List: {nums}")
    print(f"Second largest: {second}")
    print()


def check_anagram(str1, str2):
    result = sorted(str1) == sorted(str2)
    print(f"Are '{str1}' and '{str2}' anagrams? {result}")
    print()


# Example executions
multiplication_table(5)
swap_numbers(3, 7)
check_substring("hello world", "world")
decimal_to_binary(10)
add_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])
multiply_matrices([[1, 2], [3, 4]], [[2, 0], [1, 2]])
second_largest([4, 1, 2, 2, 3])
check_anagram("listen", "silent")
