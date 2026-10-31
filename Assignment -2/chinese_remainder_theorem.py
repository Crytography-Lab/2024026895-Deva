"""Chinese Remainder Theorem for pairwise-coprime positive moduli."""
from math import gcd

def chinese_remainder(remainders, moduli):
    if len(remainders) != len(moduli) or not moduli:
        raise ValueError("Provide equally sized, non-empty lists")
    if any(m <= 0 for m in moduli):
        raise ValueError("All moduli must be positive")
    for i in range(len(moduli)):
        for j in range(i + 1, len(moduli)):
            if gcd(moduli[i], moduli[j]) != 1:
                raise ValueError("Moduli must be pairwise coprime")
    product = 1
    for m in moduli:
        product *= m
    total = 0
    for r, m in zip(remainders, moduli):
        partial = product // m
        inverse = pow(partial, -1, m)
        total += r * partial * inverse
    return total % product

if __name__ == "__main__":
    count = int(input("How many congruences? "))
    remainders, moduli = [], []
    for i in range(count):
        remainders.append(int(input(f"Remainder r{i+1}: ")))
        moduli.append(int(input(f"Modulus m{i+1}: ")))
    try:
        print("Smallest non-negative solution =", chinese_remainder(remainders, moduli))
    except ValueError as error:
        print("Error:", error)
