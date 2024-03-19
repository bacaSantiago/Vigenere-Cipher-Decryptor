# Import libraries used
import csv
from unidecode import unidecode

def loadCSVFile(csv_file):
    """
    Loads a database of artists from a CSV file and returns a set of artists.

    Args:
        csv_file (str): The path to the CSV file.

    Returns:
        set: A set containing the names of artists.
    """
    
    # Initialize an empty set to store artist names
    top_artists = set()

    try:
        # Open the CSV file in read mode with UTF-8 encoding
        with open(csv_file, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            # Iterate through each row in the CSV file
            for row in csv_reader:
                # Remove spaces and convert to uppercase using unidecode for each artist name
                artist = unidecode(row[0].replace(" ", "")).upper() 
                top_artists.add(artist)
                
    # Handle exceptions
    except FileNotFoundError:
        print(f"File '{csv_file}' was not found.")
    except Exception as e:
        print(f"Error loading CSV file: {e}")

    return top_artists


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


def bruteForceAttack(encrypted_message, top_artists, full_mode):
    """
    Performs a brute-force attack on the Vigenère cipher.

    Args:
        encrypted_message (str): The encrypted message.
        top_artists (set): A set of known artists' names.
        full_mode (bool): True for full artist name, False for first characters.

    Returns:
        int: 1 if a match is found, 0 otherwise.
    """
    
    # Initialize a variable to track if a boolean coincidence is found
    coincidence = 0
    
    for digit in range(10**len(encrypted_message)):
        # Convert the digit to a string and pad with zeros to match the length of the encrypted message
        key_str = str(digit).zfill(len(encrypted_message)) 
        # Decrypt the message using the Vigenère decryption function
        decrypted_message = vigenereDecryption(encrypted_message, key_str)
        
        # Check the mode (full or first characters)
        if full_mode:
            # Check if the decrypted message is in the list of top artists
            if decrypted_message in top_artists:
                print(f"Key: {key_str}, Decrypted Message: {decrypted_message}")
                coincidence = 1
        else:            
            # Find artists that start with the decrypted message
            matching_artists = [artist for artist in top_artists if artist.startswith(decrypted_message)]
            
            # Print the key and matching artists if there are any
            for artist in matching_artists:
                print(f"Key: {key_str}, Decrypted Message: {artist}")
            
            if matching_artists: coincidence = 1

    return coincidence


def __main__():
    # Load the list of top artists from the CSV file
    top_artists = loadCSVFile('3000artists.csv')
    
    # Display a welcome message and explain the program modes
    print("Welcome to the message decryptor program, which aims to decrypt the name of your favorite artist encrypted with the Vigenère cipher. \nThis program has 2 modes: \n\tOption 0.- The first 4 or 5 letters of your artist. \n\t\t   We recommend this variant when the length of the encrypted message is greater than or equal to 9 characters. \n\tOption 1.- Full name of your artist. \n\t\t   We recommend this variant when the length of the encrypted message is less than 9 characters. ")
          
    full_mode = 2 # True for full artist name / False for first chars.   1 / 0
    
    # Validate user input for the mode
    while full_mode not in {0,1}:
        full_mode = int(input("\nPress '0' for the first mode, or press '1' for the second one: "))
        if full_mode not in {0,1}: print("Invalid Option. Try again.")
        
    # Get the encrypted message from the user and convert it to uppercase
    encrypted_message = input("Enter the encrypted message: ").upper()

    # Check if a match is found using the brute-force attack function
    if not bruteForceAttack(encrypted_message, top_artists, full_mode):
        print("No match found... Try again.")
        
__main__()