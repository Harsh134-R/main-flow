import math

#Task 1: The sum of Two Numbers
def sumoftwonumbers():
    num1 = int(input("first number: "))
    num2 = int(input("second number: "))
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}")


# Task 2: Odd or Even
def odd_or_even():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


# Task 3: Factorial Calculation
def factorial_calculation():

    n = int(input("Enter a number for its factorial: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        factorial = math.factorial(n)
        print(f"The factorial of {n} is: {factorial}")


# Task 4: Fibonacci Sequence
def fibonacci_sequence():

    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    if n <= 0:
        print("Please enter a positive integer.")
        return
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    print(f"The first {n} Fibonacci numbers are: {fib_sequence}")


# Task 5: Reverse a String
def reverse_string():

    s = input("Enter a string to reverse: ")
    reversed_s = s[::-1]
    print(f"The reversed string is: {reversed_s}")


# Task 6: Palindrome Check
def palindrome_check():
    s = input("Enter a string: ")
    is_palindrome = s == s[::-1]
    print(f"Is the string a palindrome? {is_palindrome}")


# Task 7: Leap Year Check
def leap_year_check():
    year = int(input("Enter a year to check if it's a leap year: "))

    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    print(f"Is the year {year} a leap year? {is_leap}")


# Task 8: Armstrong Number
def armstrong_number_check():
    n = int(input("Enter a number to check if it's an Armstrong number: "))
    digits = [int(d) for d in str(n)]
    power = len(digits)
    armstrong_sum = sum(d ** power for d in digits)
    is_armstrong = n == armstrong_sum
    print(f"Is the number {n} an Armstrong number? {is_armstrong}")



if __name__ == "__main__":
    print("Task 1: Sum of Two Numbers")
    sumoftwonumbers()

    print("\nTask 2: Odd or Even")
    odd_or_even()

    print("\nTask 3: Factorial Calculation")
    factorial_calculation()

    print("Task 4: Fibonacci Sequence")
    fibonacci_sequence()

    print("\nTask 5: Reverse a String")
    reverse_string()

    print("\nTask 6: Palindrome Check")
    palindrome_check()

    print("\nTask 7: Leap Year Check")
    leap_year_check()

    print("\nTask 8: Armstrong Number")
    armstrong_number_check()
