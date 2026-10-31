"""Small-number RSA key generation, encryption and decryption demo.
Educational only: real RSA requires large keys and secure padding such as OAEP.
"""
from math import gcd

def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def mod_inverse(e, phi):
    return pow(e, -1, phi)

def generate_keys(p, q):
    if not is_prime(p) or not is_prime(q) or p == q:
        raise ValueError("Choose two distinct prime numbers")
    n = p*q
    phi = (p-1)*(q-1)
    e = 3
    while e < phi and gcd(e, phi) != 1:
        e += 2
    if e >= phi:
        raise ValueError("Could not find a valid public exponent")
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

def encrypt(message, public_key):
    e, n = public_key
    if any(ord(ch) >= n for ch in message):
        raise ValueError("Choose larger primes so n exceeds every character code")
    return [pow(ord(ch), e, n) for ch in message]

def decrypt(ciphertext, private_key):
    d, n = private_key
    return ''.join(chr(pow(value, d, n)) for value in ciphertext)

if __name__ == "__main__":
    p = int(input("Enter first small prime p (e.g. 61): "))
    q = int(input("Enter second small prime q (e.g. 53): "))
    message = input("Enter message (use p=61 and q=53 for ordinary text): ")
    try:
        public_key, private_key = generate_keys(p, q)
        encrypted = encrypt(message, public_key)
        print("Public key (e, n):", public_key)
        print("Private key (d, n):", private_key)
        print("Encrypted numbers:", encrypted)
        print("Decrypted message:", decrypt(encrypted, private_key))
    except ValueError as error:
        print("Error:", error)
