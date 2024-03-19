def vigenereEncryption(message, key):
    """
    Encrypts a message using the Vigenère cipher.

    Args:
        message (str): The message to be encrypted.
        key (str): The key used for encryption.

    Returns:
        str: The encrypted message.
    """

    # Define the extended alphabet used for encryption
    extended_alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
    alphabet_indices = {char: idx for idx, char in enumerate(extended_alphabet)}
    # Repeat the key to match the length of the message
    key = key * (len(message) // len(key)) + key[:len(message) % len(key)]
    encrypted_message = []  # Empty list to store the encrypted chars

    for i in range(len(message)):
        # Check if the character is an alphabet letter or a digit
        if message[i].isalpha() or message[i].isdigit():
            # Calculate the index of the encrypted character and add it to the encrypted message
            idx = (alphabet_indices[message[i]] + int(key[i])) % len(extended_alphabet)
            encrypted_message.append(extended_alphabet[idx])
        # If the character is not an alphabet letter or a digit, keep it unchanged
        else:
            encrypted_message.append(message[i])

    return ''.join(encrypted_message)

def __main__():
    # Get the message and key, and encrypt it using the Vigenère encryption function
    message = input("Enter the message: ").upper()
    key = input("Enter the key: ").upper()
    print("Encrypted message:", vigenereEncryption(message, key))
    
__main__()