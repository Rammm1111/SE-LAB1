import math

with open("input_single.txt", "r") as file:
    line = file.readline()
    a, b, c = map(float, line.split())

d = b**2 - 4*a*c

if d >= 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print(f"Roots: {root1}, {root2}")
else:
    print("No real roots")
