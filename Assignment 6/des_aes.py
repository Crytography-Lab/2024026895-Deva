"""DES and AES encryption/decryption demonstration using PyCryptodome.

Install dependency first:
    python -m pip install pycryptodome

DES is obsolete and included only for coursework. AES uses CBC mode with
PKCS#7 padding. This is a teaching demo, not a production protocol.
"""
import base64
from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def des_encrypt(message, key):
    if len(key) != 8:
        raise ValueError("DES key must be exactly 8 bytes")
    iv = get_random_bytes(8)
    cipher = DES.new(key, DES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(message.encode("utf-8"), DES.block_size))
    return base64.b64encode(iv + encrypted).decode("ascii")

def des_decrypt(token, key):
    raw = base64.b64decode(token)
    iv, ciphertext = raw[:8], raw[8:]
    cipher = DES.new(key, DES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), DES.block_size).decode("utf-8")

def aes_encrypt(message, key):
    if len(key) not in (16, 24, 32):
        raise ValueError("AES key must be 16, 24, or 32 bytes")
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(message.encode("utf-8"), AES.block_size))
    return base64.b64encode(iv + encrypted).decode("ascii")

def aes_decrypt(token, key):
    raw = base64.b64decode(token)
    iv, ciphertext = raw[:16], raw[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), AES.block_size).decode("utf-8")

if __name__ == "__main__":
    message = input("Enter message: ")
    des_key = b"8bytekey"
    aes_key = b"0123456789abcdef"
    des_token = des_encrypt(message, des_key)
    aes_token = aes_encrypt(message, aes_key)
    print("\\nDES encrypted:", des_token)
    print("DES decrypted:", des_decrypt(des_token, des_key))
    print("\\nAES encrypted:", aes_token)
    print("AES decrypted:", aes_decrypt(aes_token, aes_key))
