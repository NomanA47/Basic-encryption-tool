"""
Basic Encryption & Decryption Tool
Caesar Cipher Implementation in Python

IPO model:
  Input   -> plaintext + shift key from the user
  Process -> shift each letter with ord(), chr() and % 26
  Output  -> ciphertext, decrypted text, and a validation check
"""


def shift_char(char, shift):
    """Shift one character. Letters wrap around A-Z / a-z, everything else is untouched."""
    if char.isupper() and char.isascii():
        base = ord("A")                      # 65
    elif char.islower() and char.isascii():
        base = ord("a")                      # 97
    else:
        return char                          # spaces, digits, punctuation stay as they are

    # char -> integer -> 0-25 position -> add key -> wrap with % 26 -> back to ASCII -> char
    return chr((ord(char) - base + shift) % 26 + base)


def encrypt(text, shift):
    """E(x) = (x + n) % 26"""
    return "".join(shift_char(c, shift) for c in text)


def decrypt(text, shift):
    """D(x) = (x - n) % 26  (same function, negative key)"""
    return "".join(shift_char(c, -shift) for c in text)


def read_shift():
    """Keep asking until the user enters a valid whole number."""
    while True:
        raw = input("Enter shift key (any whole number, e.g. 3): ").strip()
        try:
            return int(raw)
        except ValueError:
            print("  Invalid key. Please enter a whole number.")


def main():
    print("=" * 50)
    print("  DecodeLabs | Caesar Cipher Tool")
    print("=" * 50)

    plaintext = input("Enter your message: ")
    shift = read_shift()

    ciphertext = encrypt(plaintext, shift)
    decrypted = decrypt(ciphertext, shift)

    print("\n--- RESULT ---")
    print(f"Original text  : {plaintext}")
    print(f"Shift key      : {shift}")
    print(f"Encrypted text : {ciphertext}")
    print(f"Decrypted text : {decrypted}")

    # Validate with the decryption function (project deliverable #4)
    if decrypted == plaintext:
        print("Validation     : PASSED (decrypted text matches the original)")
    else:
        print("Validation     : FAILED (something is wrong in the logic)")


if __name__ == "__main__":
    main()
