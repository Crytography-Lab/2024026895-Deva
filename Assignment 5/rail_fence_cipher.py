"""Rail Fence transposition cipher."""
def encrypt(text, rails):
    if rails < 2:
        raise ValueError("Rails must be at least 2")
    fence = ['' for _ in range(rails)]
    row, direction = 0, 1
    for ch in text:
        fence[row] += ch
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction
    return ''.join(fence)

def decrypt(ciphertext, rails):
    if rails < 2:
        raise ValueError("Rails must be at least 2")
    pattern, row, direction = [], 0, 1
    for _ in ciphertext:
        pattern.append(row)
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction
    counts = [pattern.count(r) for r in range(rails)]
    rail_text, pos = [], 0
    for count in counts:
        rail_text.append(list(ciphertext[pos:pos+count]))
        pos += count
    indexes = [0] * rails
    result = []
    for r in pattern:
        result.append(rail_text[r][indexes[r]])
        indexes[r] += 1
    return ''.join(result)

if __name__ == "__main__":
    text = input("Enter message: ")
    rails = int(input("Enter number of rails: "))
    encrypted = encrypt(text, rails)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypt(encrypted, rails))
