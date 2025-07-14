def temp(a, b, c, t):
    return a*t*t + b*t + c

def single(filename):
    try:
        with open(filename) as f:
            a, b, c, t = map(float, f.readline().split())
        print("Single-set result:", temp(a, b, c, t))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print(f"Error: Invalid numbers in '{filename}'.")
    except Exception as e:
        print(f"Unexpected error in '{filename}': {e}")

def multiple(filename):
    try:
        with open(filename) as f:
            for i, line in enumerate(f, 1):
                try:
                    a, b, c, t = map(float, line.split())
                    print(f"Set {i} result:", temp(a, b, c, t))
                except ValueError:
                    print(f"Error: Invalid data on line {i} of '{filename}': '{line.strip()}'")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Unexpected error reading '{filename}': {e}")

if __name__ == "__main__":
    single('one.txt')
    multiple('many.txt')
