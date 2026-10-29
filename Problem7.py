
# Problem 7: Digit Tools

# Part (a): Sum the digits
def digit_sum(n):
    n = abs(n)
    total = 0

    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10

    return total


# Reverse the number
def reverse_number(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10

    return sign * reversed_num


# Check whether a number is a palindrome
def is_palindrome(n):
    if n < 0:
        return False

    return n == reverse_number(n)


# Test the three functions
for n in [2026, 12321, 9875]:
    print(
        f"{n}: digit sum = {digit_sum(n)}, "
        f"reversed = {reverse_number(n)}, "
        f"palindrome = {is_palindrome(n)}"
    )


# Part (b): Count palindromes from 10 to 999
count = 0

for n in range(10, 1000):
    if is_palindrome(n):
        count += 1

print("Palindromes from 10 to 999:", count)
