"""Find the modular multiplicative inverse using the extended Euclidean algorithm."""
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def modular_inverse(a, modulus):
    if modulus <= 1:
        raise ValueError("Modulus must be greater than 1")
    g, x, _ = extended_gcd(a, modulus)
    if g != 1:
        raise ValueError("Inverse does not exist: a and modulus are not coprime")
    return x % modulus

if __name__ == "__main__":
    a = int(input("Enter integer a: "))
    m = int(input("Enter modulus m: "))
    try:
        inverse = modular_inverse(a, m)
        print(f"Multiplicative inverse = {inverse}")
        print(f"Verification: ({a} * {inverse}) % {m} = {(a * inverse) % m}")
    except ValueError as error:
        print(error)
