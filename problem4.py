def discriminant_checker(a, b, c):
    D = b**2 - 4*a*c 
    if D > 0:
        return "Two real roots"
    elif D == 0:
        return "One real root"
    else:
        return "Two complex roots"

for coeffs in [(1, -5, 6), (1, 2, 1), (1, 0, 1)]:
    a, b, c = coeffs
    print(f"a={a}, b={b}, c={c} → {discriminant_checker(a, b, c)}")
