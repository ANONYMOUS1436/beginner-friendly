def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Get user input
user_input = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')
