# 1. Find Missing Number
def find_missing_number(arr, n):
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# 2. Check Balanced Parentheses
def is_balanced_parentheses(string):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in string:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack

# 3. Longest Word in a Sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# 4. Count Words in a Sentence
def count_words(sentence):
    return len(sentence.split())

# 5. Check Pythagorean Triplet
def is_pythagorean_triplet(a, b, c):
    a, b, c = sorted([a, b, c])
    return a**2 + b**2 == c**2

# 6. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 7. Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 8. Find Subarray with Given Sum
def find_subarray_with_sum(arr, target_sum):
    current_sum = 0
    start = 0
    for end in range(len(arr)):
        current_sum += arr[end]
        while current_sum > target_sum:
            current_sum -= arr[start]
            start += 1
        if current_sum == target_sum:
            return (start, end)
    return -1

# Test examples
if __name__ == "__main__":
    # 1. Find Missing Number
    print("Missing Number:", find_missing_number([1, 2, 4, 6, 3, 7, 8], 8))

    # 2. Check Balanced Parentheses
    print("Balanced Parentheses:", is_balanced_parentheses("{[()]}"))

    # 3. Longest Word in a Sentence
    print("Longest Word:", longest_word("The quick brown fox jumps over the lazy dog"))

    # 4. Count Words in a Sentence
    print("Word Count:", count_words("The quick brown fox jumps over the lazy dog"))

    # 5. Check Pythagorean Triplet
    print("Pythagorean Triplet:", is_pythagorean_triplet(3, 4, 5))

    # 6. Bubble Sort
    print("Bubble Sort:", bubble_sort([64, 34, 25, 12, 22, 11, 90]))

    # 7. Binary Search
    print("Binary Search:", binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))

    # 8. Find Subarray with Given Sum
    print("Subarray with Given Sum:", find_subarray_with_sum([1, 2, 3, 7, 5], 12))
