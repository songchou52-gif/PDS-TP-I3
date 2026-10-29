
# Problem 8: Flexible Functions

# Part (a): *args
def describe(*numbers, decimals=2, label="Data"):
    if len(numbers) == 0:
        print(f"{label}: no values")
        return None

    count = len(numbers)
    smallest = min(numbers)
    largest = max(numbers)
    mean = round(sum(numbers) / count, decimals)

    print(
        f"{label}: n={count} min={smallest} "
        f"max={largest} mean={mean}"
    )

    return (count, smallest, largest, mean)


describe(12, 7, 30, 4)
describe(3.14159, 2.71828, decimals=3, label="Constants")
describe()


# Part (b): **kwargs
def make_tag(text, **style):
    attributes = ""

    for key, value in style.items():
        attributes += f' {key}="{value}"'

    return f"<span{attributes}>{text}</span>"


print(make_tag("Hello", color="red", size=14))


# Part (c): lambda
square = lambda x: x ** 2
is_adult = lambda age: age >= 18

print(square(9), is_adult(17), is_adult(21))
