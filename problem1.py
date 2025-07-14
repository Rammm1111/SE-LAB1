import cmath

a, b, c = 1, 10, -24  

d = b*b - 4*a*c/2*a
root1 = (-b + cmath.sqrt(d)) / (2*a)
root2 = (-b - cmath.sqrt(d)) / (2*a)

print("Roots:", root1, root2)
