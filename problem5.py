import math

with open("input_multiple.txt", "r") as file:
    lines = file.readlines()

for idx, line in enumerate(lines):
    a, b, c = map(float, line.strip().split())
    d = b**2 - 4*a*c

    print(f"\nSet {idx+1}: a={a}, b={b}, c={c}")
    if d >= 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print(f"Roots: {root1}, {root2}")
    else:
        print("No real roots")
