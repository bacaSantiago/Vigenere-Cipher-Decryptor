def vigenereDecryption(encrypted_message, key):
    """
    Decrypts a message using the Vigenère cipher.

    Args:
        encrypted_message (str): The encrypted message.
        key (str): The key used for decryption.

    Returns:
        str: The decrypted message.
    """

    # Define the extended alphabet used for encryption
    extended_alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
    alphabet_indices = {char: idx for idx, char in enumerate(extended_alphabet)}
    # Repeat the key to match the length of the encrypted message
    key = key * (len(encrypted_message) // len(key)) + key[:len(encrypted_message) % len(key)]
    decrypted_message = [] # Empty list to store the decrypted chars

    for i in range(len(encrypted_message)):
        # Check if the character is an alphabet letter or a digit
        if encrypted_message[i].isalpha() or encrypted_message[i].isdigit():
            # Calculate the index of the decrypted character and add it to the decrypted message
            idx = alphabet_indices[encrypted_message[i]] - int(key[i])
            decrypted_message.append(extended_alphabet[idx])
        # If the character is not an alphabet letter or a digit, keep it unchanged
        else:
            decrypted_message.append(encrypted_message[i])

    return ''.join(decrypted_message)

def __main__():
    # Get the encrypted message and key, and decrypt it using the Vigenère decryption function
    encrypted_message = input("Enter the encrypted message: ").upper()
    key = input("Enter the key: ").upper()
    print("Decrypted message:", vigenereDecryption(encrypted_message, key))

__main__()