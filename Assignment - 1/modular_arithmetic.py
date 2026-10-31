"""Assignment 1: Modular Arithmetic

Demonstrate modular addition, subtraction, multiplication and
exponentiation for a positive modulus.
"""

def modular_arithmetic(a, b, modulus):
    if modulus <= 0:
        raise ValueError("Modulus must be a positive integer.")
    if b < 0:
        raise ValueError("For this program, the exponent must be non-negative.")

    return {
        "Addition": (a + b) % modulus,
        "Subtraction": (a - b) % modulus,
        "Multiplication": (a * b) % modulus,
        "Exponentiation (a^b)": pow(a, b, modulus),
    }


if __name__ == "__main__":
    print("MODULAR ARITHMETIC")
    try:
        a = int(input("Enter first integer (a): "))
        b = int(input("Enter second integer (b): "))
        m = int(input("Enter positive modulus (m): "))

        results = modular_arithmetic(a, b, m)
        print(f"Results modulo {m}:")
        for operation, result in results.items():
            print(f"{operation}: {result}")
    except ValueError as error:
        print("Error:", error)
