"""Playfair cipher using I/J combined and X as the default filler."""
import string

def make_square(key):
    chars = []
    for ch in (key + string.ascii_uppercase):
        ch = ch.upper()
        if ch == 'J':
            ch = 'I'
        if ch in string.ascii_uppercase and ch not in chars:
            chars.append(ch)
    return [chars[i:i+5] for i in range(0, 25, 5)]

def prepare(text):
    text = ''.join(c.upper().replace('J', 'I') for c in text if c.isascii() and c.isalpha())
    pairs, i = [], 0
    while i < len(text):
        a = text[i]
        if i + 1 >= len(text):
            b, i = 'X', i + 1
        elif text[i+1] == a:
            b, i = 'X', i + 1
        else:
            b, i = text[i+1], i + 2
        pairs.append((a, b))
    return pairs

def playfair(text, key, decrypt=False):
    square = make_square(key)
    positions = {square[r][c]: (r, c) for r in range(5) for c in range(5)}
    result = []
    step = -1 if decrypt else 1
    for a, b in prepare(text):
        ra, ca = positions[a]
        rb, cb = positions[b]
        if ra == rb:
            result.extend([square[ra][(ca+step)%5], square[rb][(cb+step)%5]])
        elif ca == cb:
            result.extend([square[(ra+step)%5][ca], square[(rb+step)%5][cb]])
        else:
            result.extend([square[ra][cb], square[rb][ca]])
    return ''.join(result)

if __name__ == "__main__":
    key = input("Enter keyword: ")
    message = input("Enter message: ")
    encrypted = playfair(message, key)
    print("Encrypted:", encrypted)
    print("Decrypted (may contain filler X):", playfair(encrypted, key, decrypt=True))
