"""Deterministic trial-division primality test."""
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    for divisor in range(3, isqrt(n) + 1, 2):
        if n % divisor == 0:
            return False
    return True

if __name__ == "__main__":
    n = int(input("Enter an integer: "))
    print("Prime" if is_prime(n) else "Not prime")
