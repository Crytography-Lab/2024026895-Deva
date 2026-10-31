"""Hill cipher using a 2x2 key matrix modulo 26. Educational implementation."""
import math

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("Key matrix is not invertible modulo 26")

def inverse_key(key):
    a, b = key[0]
    c, d = key[1]
    det = (a*d - b*c) % 26
    inv_det = mod_inverse(det, 26)
    return [[(d*inv_det) % 26, (-b*inv_det) % 26],
            [(-c*inv_det) % 26, (a*inv_det) % 26]]

def transform(text, key):
    cleaned = ''.join(ch.upper() for ch in text if ch.isascii() and ch.isalpha())
    if len(cleaned) % 2:
        cleaned += 'X'
    output = []
    for i in range(0, len(cleaned), 2):
        x, y = ord(cleaned[i])-65, ord(cleaned[i+1])-65
        output.append(chr((key[0][0]*x + key[0][1]*y) % 26 + 65))
        output.append(chr((key[1][0]*x + key[1][1]*y) % 26 + 65))
    return ''.join(output)

if __name__ == "__main__":
    key = [[3, 3], [2, 5]]
    message = input("Enter message (letters only): ")
    encrypted = transform(message, key)
    print("Key matrix:", key)
    print("Encrypted:", encrypted)
    print("Decrypted:", transform(encrypted, inverse_key(key)))
