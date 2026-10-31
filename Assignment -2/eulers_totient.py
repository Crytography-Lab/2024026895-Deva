"""Euler's Totient Function: count integers from 1 to n that are coprime to n."""
def euler_totient(n):
    if n < 1:
        raise ValueError("n must be a positive integer")
    result, value, p = n, n, 2
    while p * p <= value:
        if value % p == 0:
            while value % p == 0:
                value //= p
            result -= result // p
        p += 1
    if value > 1:
        result -= result // value
    return result

if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    print("phi(n) =", euler_totient(n))
