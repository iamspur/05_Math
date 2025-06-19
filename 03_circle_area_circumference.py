import math
r = int(input("Enter a radius: "))
area = math.pi * (r ** 2)
circum = 2 * math.pi * r
print(f"Area of a circle with radius {r} is {area:.2f}")
print(f"Circumference of a circle with radius {r} is {circum:.2f}")