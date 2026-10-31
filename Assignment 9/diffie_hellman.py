"""Diffie-Hellman key exchange demonstration with small classroom parameters.
Real systems must use standardized large groups and authenticated key exchange.
"""
def generate_public_key(private_value, prime, generator):
    return pow(generator, private_value, prime)

def generate_shared_secret(other_public, private_value, prime):
    return pow(other_public, private_value, prime)

if __name__ == "__main__":
    p = int(input("Enter prime modulus p (e.g. 23): "))
    g = int(input("Enter generator g (e.g. 5): "))
    alice_private = int(input("Enter Alice's private number: "))
    bob_private = int(input("Enter Bob's private number: "))

    alice_public = generate_public_key(alice_private, p, g)
    bob_public = generate_public_key(bob_private, p, g)
    alice_secret = generate_shared_secret(bob_public, alice_private, p)
    bob_secret = generate_shared_secret(alice_public, bob_private, p)

    print("Alice public key:", alice_public)
    print("Bob public key:", bob_public)
    print("Alice shared secret:", alice_secret)
    print("Bob shared secret:", bob_secret)
    print("Keys match:", alice_secret == bob_secret)
