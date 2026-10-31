"""Polyalphabetic Vigenere cipher."""
def vigenere(message, key, decrypt=False):
    key = ''.join(ch.upper() for ch in key if ch.isalpha())
    if not key or not key.isascii():
        raise ValueError("Key must contain at least one English letter")
    result, index = [], 0
    for ch in message:
        if ch.isascii() and ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = ord(key[index % len(key)]) - ord('A')
            if decrypt:
                shift = -shift
            result.append(chr((ord(ch) - base + shift) % 26 + base))
            index += 1
        else:
            result.append(ch)
    return ''.join(result)

if __name__ == "__main__":
    message = input("Enter message: ")
    key = input("Enter keyword: ")
    encrypted = vigenere(message, key)
    print("Encrypted:", encrypted)
    print("Decrypted:", vigenere(encrypted, key, decrypt=True))
