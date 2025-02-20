import string
import random

def menu():
    print("\nChoose a cipher:")
    print("1. Enigma Machine")
    print("2. Caesar Cipher")
    print("3. Affine Cipher")
    print("4. Vigenère Cipher")
    print("5. Bacon Cipher")
    print("6. Rail Fence Cipher")
    print("7. Exit")
    return input("Enter your choice: ")

class EnigmaMachine:
    def __init__(self, rotors, reflector):
        self.rotors = rotors
        self.reflector = reflector
        self.alphabet = string.ascii_uppercase
    
    def encrypt_decrypt(self, text):
        result = ""
        for letter in text.upper():
            if letter in self.alphabet:
                for rotor in self.rotors:
                    letter = rotor[ord(letter) - ord('A')]
                letter = self.reflector[ord(letter) - ord('A')]
                for rotor in reversed(self.rotors):
                    letter = self.alphabet[rotor.index(letter)]
            result += letter
        return result

def generate_random_rotors():
    alphabet = string.ascii_uppercase
    return ["".join(random.sample(alphabet, len(alphabet))) for _ in range(3)]

def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    alphabet = string.ascii_uppercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.upper().translate(table)

def affine_cipher(text, a, b, decrypt=False):
    m = 26
    if decrypt:
        a_inv = pow(a, -1, m)
        return "".join(chr(((ord(char) - 65 - b) * a_inv % m) + 65) if char.isalpha() else char for char in text.upper())
    return "".join(chr(((a * (ord(char) - 65) + b) % m) + 65) if char.isalpha() else char for char in text.upper())

def vigenere_cipher(text, key, decrypt=False):
    key = (key + text)[:len(text)] if not decrypt else key
    key_indices = [ord(k) - 65 for k in key.upper()]
    text_indices = [ord(t) - 65 for t in text.upper()]
    result = ""
    for i, val in enumerate(text_indices):
        shift = key_indices[i] if not decrypt else -key_indices[i]
        result += chr((val + shift) % 26 + 65)
    return result

def bacon_cipher(text, decrypt=False):
    bacon_map = {char: format(i, '05b') for i, char in enumerate(string.ascii_uppercase)}
    if decrypt:
        reversed_map = {v: k for k, v in bacon_map.items()}
        return "".join(reversed_map[text[i:i+5]] for i in range(0, len(text), 5))
    return "".join(bacon_map[char] for char in text.upper() if char.isalpha())

def rail_fence_cipher(text, rails, decrypt=False):
    if decrypt:
        zigzag = [[] for _ in range(rails)]
        pattern = list(range(rails)) + list(range(rails-2, 0, -1))
        index_positions = sorted(range(len(text)), key=lambda x: pattern[x % len(pattern)])
        for i, index in enumerate(index_positions):
            zigzag[pattern[index % len(pattern)]].append(text[i])
        return "".join(sum(zigzag, []))
    zigzag = ["" for _ in range(rails)]
    pattern = list(range(rails)) + list(range(rails-2, 0, -1))
    for i, char in enumerate(text):
        zigzag[pattern[i % len(pattern)]] += char
    return "".join(zigzag)

while True:
    choice = menu()
    if choice == "1":
        rotors = generate_random_rotors()
        reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
        enigma = EnigmaMachine(rotors, reflector)
        text = input("Enter text: ")
        print("Encrypted/Decrypted:", enigma.encrypt_decrypt(text))
    elif choice == "2":
        text = input("Enter text: ")
        shift = int(input("Enter shift: "))
        print("Encrypted:", caesar_cipher(text, shift))
        print("Decrypted:", caesar_cipher(text, shift, decrypt=True))
    elif choice == "3":
        text = input("Enter text: ")
        a = int(input("Enter value for a: "))
        b = int(input("Enter value for b: "))
        print("Encrypted:", affine_cipher(text, a, b))
        print("Decrypted:", affine_cipher(affine_cipher(text, a, b), a, b, decrypt=True))
    elif choice == "4":
        text = input("Enter text: ")
        key = input("Enter key: ")
        print("Encrypted:", vigenere_cipher(text, key))
        print("Decrypted:", vigenere_cipher(vigenere_cipher(text, key), key, decrypt=True))
    elif choice == "5":
        text = input("Enter text: ")
        print("Encrypted:", bacon_cipher(text))
        print("Decrypted:", bacon_cipher(bacon_cipher(text), decrypt=True))
    elif choice == "6":
        text = input("Enter text: ")
        rails = int(input("Enter number of rails: "))
        print("Encrypted:", rail_fence_cipher(text, rails))
        print("Decrypted:", rail_fence_cipher(rail_fence_cipher(text, rails), rails, decrypt=True))
    elif choice == "7":
        break
    else:
        print("Invalid choice, try again.")
