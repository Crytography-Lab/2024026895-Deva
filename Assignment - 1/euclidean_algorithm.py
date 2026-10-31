"""Assignment 1: Euclidean Algorithm

Find the greatest common divisor (GCD) of two integers.
"""

def euclidean_gcd(a, b):
    a, b = abs(a), abs(b)

    while b != 0:
        a, b = b, a % b

    return a


if __name__ == "__main__":
    print("EUCLIDEAN ALGORITHM")
    try:
        a = int(input("Enter first integer: "))
        b = int(input("Enter second integer: "))
        print("GCD =", euclidean_gcd(a, b))
    except ValueError:
        print("Please enter valid integers.")
