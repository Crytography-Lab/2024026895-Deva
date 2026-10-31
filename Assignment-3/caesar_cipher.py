"""Caesar cipher encryption and decryption (preserves case and punctuation)."""
def caesar_encrypt(text, shift):
    result = []
    for ch in text:
        if ch.isascii() and ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    message = input("Enter message: ")
    shift = int(input("Enter shift: "))
    encrypted = caesar_encrypt(message, shift)
    print("Encrypted:", encrypted)
    print("Decrypted:", caesar_decrypt(encrypted, shift))
