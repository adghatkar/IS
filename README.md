# CRYPTII - Cryptographic Analysis and Implementation  

## Team Members  
- Gauri Charpe (16010122027)  
- Ashish Ghatkar (16010122057)  
- Soumil Dhywershetty (16010122048)  

## Introduction  
[Cryptii.com](https://cryptii.com) is a powerful online cryptography tool that allows users to encode, decode, and analyze various ciphers. It serves as an educational platform for students, cryptography enthusiasts, and professionals who want to explore historical and modern encryption techniques.  

This project provides a comprehensive analysis of several encryption methods, including classical ciphers and their modern adaptations, along with an implementation of these techniques in Python.  

## Features  
✅ **Web-Based** – No installation required, accessible from any device.  
✅ **Supports Various Ciphers** – Includes classical substitution and transposition ciphers.  
✅ **Interactive UI** – Demonstrates encryption and decryption processes visually.  
✅ **Customizable Parameters** – Modify encryption settings for deeper analysis.  
✅ **Real-Time Encoding & Decoding** – Instant feedback while encrypting/decrypting.  
✅ **Open-Source** – Built with open-source technologies, allowing community contributions.  

## Implemented Ciphers  
### 🔐 Classical Ciphers  
- **Enigma Machine** – WWII-era mechanical cipher with rotor-based encryption.  
- **Caesar Cipher** – Simple letter shift cipher used by Julius Caesar.  
- **Affine Cipher** – Mathematical substitution cipher with modular arithmetic.  
- **Vigenère Cipher** – Polyalphabetic cipher using repeating keywords.  
- **Bacon Cipher** – Steganographic cipher encoding text in binary-like format.  
- **Rail Fence Cipher** – Transposition cipher rearranging letter positions.  

## Methodology  
Each cipher has been analyzed in detail, covering its:  
- **Historical Context**  
- **Encryption & Decryption Process**  
- **Example Usage**  
- **Strengths & Weaknesses**  

### 🔧 Improvements  
For better security, enhancements were made to traditional ciphers:  
- **Enigma Machine** – Uses randomly generated rotors.  
- **Caesar Cipher** – Implements a random shift instead of a fixed value.  
- **Affine Cipher** – Ensures modular inverse for guaranteed decryption.  
- **Vigenère Cipher** – Introduces an auto-key feature.  
- **Bacon Cipher** – Extended binary mapping for better flexibility.  
- **Rail Fence Cipher** – Uses a variable step pattern to strengthen encryption.  

## Implementation  
The project includes a Python-based CLI application that lets users encrypt and decrypt messages using the discussed ciphers.  

### 📜 Sample Code (Caesar Cipher)  
```python
import string

def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    alphabet = string.ascii_uppercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.upper().translate(table)

# Example Usage:
plaintext = "HELLO"
ciphertext = caesar_cipher(plaintext, shift=3)
print("Encrypted:", ciphertext)  # Output: KHOOR
