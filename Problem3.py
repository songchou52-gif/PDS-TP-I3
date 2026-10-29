# Problem 3: Temperature Converter

# (a) Define two functions

def celsius_to_fahrenheit(c, round_to=1):
    value = c * 9 / 5 + 32
    return round(value, round_to)


def fahrenheit_to_celsius(f, round_to=1):
    value = (f - 32) * 5 / 9
    return round(value, round_to)


# (a) Print the conversion table

print("  °C |    °F")
print("------+-------")

for c in range(0, 101, 20):
    f = celsius_to_fahrenheit(c)
    print(f"{c:5} | {f:6.1f}")


# (b) Convert 98.6°F to Celsius

celsius = fahrenheit_to_celsius(98.6)
print(f"\n98.6 °F = {celsius} °C")


# (c) Convert 37°C to Fahrenheit and back again

fahrenheit = celsius_to_fahrenheit(37)
print(f"37 °C = {fahrenheit} °F")

celsius_again = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit} °F = {celsius_again} °C")

# Check whether we get 37.0 again
print("Do we get 37.0?", celsius_again == 37.0)


# (d) Call a function with round_to=3

result = celsius_to_fahrenheit(25, round_to=3)
print(f"\n25 °C = {result:.3f} °F")