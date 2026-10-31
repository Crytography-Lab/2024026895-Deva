"""Fermat's Little Theorem: if p is prime and p does not divide a,
then pow(a, p-1, p) == 1.
"""
def fermat_test(a, p):
    if p < 2:
        raise ValueError("p must be at least 2")
    if p <= 1:
        return False
    return pow(a, p - 1, p) == 1

if __name__ == "__main__":
    a = int(input("Enter a: "))
    p = int(input("Enter prime candidate p: "))
    print("Fermat congruence holds." if fermat_test(a, p) else "Fermat congruence does not hold.")
    print("Note: this test alone does not prove that p is prime.")
