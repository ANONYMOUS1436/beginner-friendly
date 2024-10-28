def fibonacci_sequence(limit):
    a, b = 0, 1
    fibonacci_numbers = []

    while a <= limit:
        fibonacci_numbers.append(a)
        a, b = b, a + b

    return fibonacci_numbers

try:
    user_limit = int(input("Enter the limit for the Fibonacci sequence: "))
    if user_limit < 0:
        print("Please enter a non-negative integer.")
    else:
        sequence = fibonacci_sequence(user_limit)
        print("Fibonacci sequence up to", user_limit, ":", sequence)
except ValueError:


