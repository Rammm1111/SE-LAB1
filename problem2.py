import cmath

try:
    a = float(input("Enter a non-zero: "))
    if a == 0:
        raise ValueError("a cannot be zero.")
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
except ValueError as e:
    print("Invalid input:", e)
    exit(1)

d = b*b - 4*a*c/2*a
root1 = (-b + cmath.sqrt(d)) / (2*a)
root2 = (-b - cmath.sqrt(d)) / (2*a)

print(f"Roots: {root1} and {root2}")
