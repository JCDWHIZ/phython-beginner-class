import math


def calculations():
    raduis1_str = input("Enter a raduis ")
    raduis2_int = int(raduis1_str)
    circumference_int = 2 * math.pi * int(raduis2_int)
    area_int = math.pi * (raduis2_int ** 2)
    return "The circumference is:",circumference_int, "The area is:",area_int


print(calculations())
