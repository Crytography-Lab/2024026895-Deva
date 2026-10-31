"""Monoalphabetic substitution cipher using a 26-letter substitution key."""
import string

ALPHABET = string.ascii_uppercase

def validate_key(key):
    key = key.upper()
    if len(key) != 26 or set(key) != set(ALPHABET):
        raise ValueError("Key must contain every English letter exactly once")
    return key

def encrypt(message, key):
    key = validate_key(key)
    table = str.maketrans(ALPHABET + ALPHABET.lower(),
                          key + key.lower())
    return message.translate(table)

def decrypt(ciphertext, key):
    key = validate_key(key)
    table = str.maketrans(key + key.lower(),
                          ALPHABET + ALPHABET.lower())
    return ciphertext.translate(table)

if __name__ == "__main__":
    message = input("Enter message: ")
    key = input("Enter 26-letter substitution key (e.g. QWERTYUIOPASDFGHJKLZXCVBNM): ")
    try:
        encrypted = encrypt(message, key)
        print("Encrypted:", encrypted)
        print("Decrypted:", decrypt(encrypted, key))
    except ValueError as error:
        print("Error:", error)
