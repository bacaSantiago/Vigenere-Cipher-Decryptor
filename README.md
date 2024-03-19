# Vigenère Cipher Decryptor

This repository contains Python scripts for decrypting messages encrypted with the Vigenère cipher, both with and without knowledge of the key. The Vigenère cipher is a method of encrypting alphabetic text using a simple form of polyalphabetic substitution.

## Programs Overview

### 1. **Vigenère Decryption with Key**

#### File: `vigenere_decrypt_with_key.py`

This program decrypts a message using the Vigenère cipher with a known key. It prompts the user to enter the encrypted message and the key, providing the decrypted message as output.

### 2. **Vigenère Encryption**

#### File: `vigenere_encrypt.py`

This program encrypts a message using the Vigenère cipher. Users are prompted to enter the message and the key, and the encrypted message is displayed.

### 3. **Vigenère Decryption without Key**

#### File: `vigenere_decrypt_without_key.py`

This program attempts to decrypt a message encrypted with the Vigenère cipher without knowledge of the key. It uses a brute-force approach, trying all possible keys and checking if the decrypted message corresponds to known artists' names. Users can choose between two modes: decrypting the full artist name or the first few characters.

## Introduction to the Vigenère Cipher

The Vigenère cipher is a method of encrypting alphabetic text using a simple form of polyalphabetic substitution. It uses a keyword to shift letters in the plaintext, creating a more secure encryption compared to the Caesar cipher. The keyword determines the shift for each letter in the message, making it resistant to frequency analysis.

## How to Use

1. **Vigenère Decryption with Key:**
   - Run the script: `python vigenere_decrypt_with_key.py`
   - Enter the encrypted message and the key when prompted.
   - The decrypted message will be displayed.

2. **Vigenère Encryption:**
   - Run the script: `python vigenere_encrypt.py`
   - Enter the message and the key when prompted.
   - The encrypted message will be displayed.

3. **Vigenère Decryption without Key:**
   - Run the script: `python vigenere_decrypt_without_key.py`
   - Choose between two modes:
     - Mode 0: Decrypt the first few characters of the artist's name.
     - Mode 1: Decrypt the full artist's name.
   - Enter the encrypted message when prompted.
   - The script will attempt a brute-force attack and display matching keys and artist names.

## Note
- Ensure you have Python installed on your system.
- The decryption without a key may take time as it involves a brute-force approach.
- The artist database for the decryption without a key is loaded from a CSV file (`3000artists.csv`). Ensure this file is available and correctly formatted.

Feel free to explore and experiment with these Vigenère cipher programs!