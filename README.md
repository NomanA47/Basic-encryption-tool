# Project2
# Caesar Cipher: Basic Encryption & Decryption

A small Python command-line tool that encrypts a message with a Caesar cipher, decrypts it back, and checks that the result matches the original.

## How it works

Follows the Input, Process, Output model:

1. **Input:** the user enters a message and a shift key.
2. **Process:** each letter is converted to its ASCII value with `ord()`, shifted, wrapped with `% 26`, and converted back with `chr()`.
3. **Output:** the encrypted text, the decrypted text, and a validation result.

```
Encrypt: E(x) = (x + n) % 26
Decrypt: D(x) = (x - n) % 26
```

Spaces, digits and punctuation are left unchanged. Upper and lower case are preserved.

## Run it

```
python caesar_cipher.py
```

Requires Python 3. No external libraries.

## Example

```
Enter your message: Hello, World! XYZ xyz 123
Enter shift key (any whole number, e.g. 3): 3

Original text  : Hello, World! XYZ xyz 123
Shift key      : 3
Encrypted text : Khoor, Zruog! ABC abc 123
Decrypted text : Hello, World! XYZ xyz 123
Validation     : PASSED (decrypted text matches the original)
```

## Limitations

The Caesar cipher is for learning only. It has just 25 usable keys, so it can be brute-forced instantly, and it keeps letter frequencies intact, so frequency analysis breaks it. Real systems use algorithms like AES.

## Author

Noman Atiq
