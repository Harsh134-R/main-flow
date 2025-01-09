import math

# 1. Prime Number
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 2. Sum of Digits
def sumofdigits(n):
    return sum(int(digit) for digit in str(abs(n)))

# 3. LCM and GCD
def lcmandgcd(a, b):
    gcd = math.gcd(a, b)
    lcm = abs(a * b) // gcd
    return lcm, gcd

# 4. List Reversal
def reverselist(lst):
    reversed_list = []
    for i in range(len(lst)-1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

# 5. Sort a List (Bubble Sort)
def bubblesort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

# 6. Remove Duplicates
def removeduplicates(lst):
    unique_elements = []
    for item in lst:
        if item not in unique_elements:
            unique_elements.append(item)
    return unique_elements

# 7. String Length
def stringlength(s):
    length = 0
    for _ in s:
        length += 1
    return length

# 8. Count Vowels and Consonants
def countvowelsandconsonants(s):
    vowels = set('aeiouAEIOU')
    vowel_count = 0
    consonant_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count


if __name__ == "__main__":
    # Test Prime Number
    print(isprime(17))

    # Test Sum of Digits
    print(sumofdigits(1234))

    # Test LCM and GCD
    print(lcmandgcd(12, 18))
    # Test List Reversal
    print(reverselist([1, 2, 3]))

    # Test Bubble Sort
    print(bubblesort([3, 2, 1]))

    # Test Remove Duplicates
    print(removeduplicates([1, 2, 2, 3]))

    # Test String Length
    print(stringlength("hello"))

    # Test Count Vowels and Consonants
    print(countvowelsandconsonants("hello"))
