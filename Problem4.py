
# Problem 4: Type-Conversion Detective
# Part A: Check the expressions

print(int("7") + 3.5)
print(str(10) * 3)
print(bool(""), bool(" "))
print(int(3.99))
print(float("1e3"))
print(int(True) + float("2.5"))
print(round(2.5), round(3.5))
print(type(10 / 2))

# Part B: Define safe_int()

def safe_int(text):
    text = text.strip()

    if text == "":
        return None

    try:
        return int(float(text))
    except ValueError:
        return None

# Test safe_int()

for sample in ["42", " -8 ", "3.9", "abc", ""]:
    print(repr(sample), "->", safe_int(sample))

# Part C: Ask the user for two numbers

first_text = input("Enter the first number: ")
second_text = input("Enter the second number: ")

first_number = safe_int(first_text)
second_number = safe_int(second_text)

if first_number is not None and second_number is not None:
    print("Sum =", first_number + second_number)
else:
    print("Please enter valid numbers.")
