import math

with open("input_multiple.txt", "r") as infile, open("output.txt", "w") as outfile:
    lines = infile.readlines()

    for idx, line in enumerate(lines):
        try:
            a, b, c = map(float, line.strip().split())
            d = b**2 - 4*a*c

            outfile.write(f"Set {idx+1}: a={a}, b={b}, c={c}\n")
            if d >= 0:
                root1 = (-b + math.sqrt(d)) / (2*a)
                root2 = (-b - math.sqrt(d)) / (2*a)
                outfile.write(f"Roots: {root1}, {root2}\n\n")
            else:
                outfile.write("No real roots\n\n")
        except Exception as e:
            outfile.write(f"Error in set {idx+1}: {str(e)}\n\n")
