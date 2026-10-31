"""Check whether two integers are relatively prime (coprime)."""
from math import gcd

def are_relative_primes(a, b):
    return gcd(a, b) == 1

if __name__ == "__main__":
    a = int(input("Enter first integer: "))
    b = int(input("Enter second integer: "))
    print("Relatively prime" if are_relative_primes(a, b) else "Not relatively prime")
