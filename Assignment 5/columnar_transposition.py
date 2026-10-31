"""Columnar transposition cipher. Key must contain distinct characters."""
def column_order(key):
    if not key or len(set(key)) != len(key):
        raise ValueError("Key must be non-empty and contain distinct characters")
    return sorted(range(len(key)), key=lambda i: (key[i], i))

def encrypt(text, key):
    order = column_order(key)
    width = len(key)
    rows = [text[i:i+width] for i in range(0, len(text), width)]
    return ''.join(row[col] for col in order for row in rows if col < len(row))

def decrypt(ciphertext, key):
    order = column_order(key)
    width, length = len(key), len(ciphertext)
    row_count = (length + width - 1) // width
    short_cols = width * row_count - length
    col_lengths = [row_count - (1 if c >= width-short_cols and short_cols else 0)
                   for c in range(width)]
    columns, pos = [''] * width, 0
    for col in order:
        n = col_lengths[col]
        columns[col] = ciphertext[pos:pos+n]
        pos += n
    result = []
    for r in range(row_count):
        for c in range(width):
            if r < len(columns[c]):
                result.append(columns[c][r])
    return ''.join(result)

if __name__ == "__main__":
    text = input("Enter message: ")
    key = input("Enter key (distinct characters): ")
    try:
        encrypted = encrypt(text, key)
        print("Encrypted:", encrypted)
        print("Decrypted:", decrypt(encrypted, key))
    except ValueError as error:
        print("Error:", error)
