"""
Caesar Cipher Tool
-------------------
This script allows users to encrypt or decrypt messages using the Caesar Cipher algorithm.
The Caesar Cipher shifts each letter in the message by a given number of positions.
"""

def caesar_cipher(text: str, shift: int, mode: str = 'encrypt') -> str:
    """
    Encrypts or decrypts a message using Caesar Cipher.

    Parameters:
        text (str): The input message to process.
        shift (int): The number of positions to shift each letter.
        mode (str): Either 'encrypt' or 'decrypt'.

    Returns:
        str: The resulting encrypted or decrypted message.
    """
    if mode == 'decrypt':
        shift = -shift

    result = []

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(shifted_char)
        else:
            result.append(char)

    return ''.join(result)


def get_user_input() -> tuple:
    """
    Prompts user for input.

    Returns:
        tuple: (mode, message, shift)
    """
    print("=== Caesar Cipher Tool ===")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        raise ValueError("Invalid mode. Choose 'encrypt' or 'decrypt'.")
    
    message = input("Enter your message: ")
    
    try:
        shift = int(input("Enter shift value (e.g., 3): "))
    except ValueError:
        raise ValueError("Shift must be an integer.")

    return mode, message, shift


def main():
    """
    Main function to run the Caesar Cipher tool.
    """
    try:
        mode, message, shift = get_user_input()
        result = caesar_cipher(message, shift, mode)
        print(f"\nResult ({mode.title()}ed): {result}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
