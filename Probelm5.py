
# Problem 5: Letter Grade

def letter_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 97:
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# (a) Test the function

print(letter_grade(98))
print(letter_grade(95))
print(letter_grade(85))
print(letter_grade(75))
print(letter_grade(65))
print(letter_grade(50))
print(letter_grade(-5))
print(letter_grade(105))

# Queston b
# The test for A+ must come before A 
# because score >= 90 also includes scores that are 97 or higher. 
# If we check A first, a score of 99 will return "A" instead of "A+". 
# Therefore, we should check the higher grade first.