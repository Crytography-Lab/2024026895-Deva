"""Educational DSA/DSS-style digital signature demonstration.

Uses small toy parameters for readability. Do not use these parameters
or this implementation for real security.
"""
import hashlib
import secrets

# Small valid example parameters: p=23, q=11, g=2 (g has order q mod p).
P, Q, G = 23, 11, 2

def hash_message(message):
    return int.from_bytes(hashlib.sha256(message.encode("utf-8")).digest(), "big")

def generate_keys():
    private_key = secrets.randbelow(Q - 1) + 1
    public_key = pow(G, private_key, P)
    return private_key, public_key

def sign(message, private_key):
    z = hash_message(message)
    while True:
        k = secrets.randbelow(Q - 1) + 1
        r = pow(G, k, P) % Q
        if r == 0:
            continue
        s = (pow(k, -1, Q) * (z + private_key * r)) % Q
        if s != 0:
            return r, s

def verify(message, signature, public_key):
    r, s = signature
    if not (0 < r < Q and 0 < s < Q):
        return False
    w = pow(s, -1, Q)
    z = hash_message(message)
    u1 = (z * w) % Q
    u2 = (r * w) % Q
    v = ((pow(G, u1, P) * pow(public_key, u2, P)) % P) % Q
    return v == r

if __name__ == "__main__":
    message = input("Enter message to sign: ")
    private_key, public_key = generate_keys()
    signature = sign(message, private_key)
    print("Public key:", public_key)
    print("Signature (r, s):", signature)
    print("Signature valid:", verify(message, signature, public_key))
    altered = message + "!"
    print("Valid after message change:", verify(altered, signature, public_key))
