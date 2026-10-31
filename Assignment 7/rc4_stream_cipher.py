"""RC4 stream cipher demonstration. RC4 is cryptographically broken;
use only for coursework and never to protect real data."""
def rc4(data, key):
    if not key:
        raise ValueError("Key must not be empty")
    key_bytes = key if isinstance(key, bytes) else key.encode("utf-8")
    data_bytes = data if isinstance(data, bytes) else data.encode("utf-8")

    # Key Scheduling Algorithm (KSA)
    state = list(range(256))
    j = 0
    for i in range(256):
        j = (j + state[i] + key_bytes[i % len(key_bytes)]) % 256
        state[i], state[j] = state[j], state[i]

    # Pseudo-Random Generation Algorithm (PRGA)
    i = j = 0
    output = bytearray()
    for byte in data_bytes:
        i = (i + 1) % 256
        j = (j + state[i]) % 256
        state[i], state[j] = state[j], state[i]
        k = state[(state[i] + state[j]) % 256]
        output.append(byte ^ k)
    return bytes(output)

if __name__ == "__main__":
    message = input("Enter message: ")
    key = input("Enter key: ")
    encrypted = rc4(message, key)
    print("Encrypted (hex):", encrypted.hex())
    decrypted = rc4(encrypted, key).decode("utf-8")
    print("Decrypted:", decrypted)
