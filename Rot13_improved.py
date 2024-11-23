def rot13_cipher(text):
    """Encrypt or decrypt a text using the ROT13 cipher."""
    final_text = []  # Use list to collect the characters

    for letter in text:
        if letter.isalpha():  # Check if the character is alphabetic
            # Handle uppercase and lowercase separately
            if letter.islower():
                base = ord('a')
            else:
                base = ord('A')
            
            # Shift the character by 13 places, and wrap around if needed
            shifted = (ord(letter) - base + 13) % 26 + base
            final_text.append(chr(shifted))
        else:
            # Non-alphabetic characters are not modified
            final_text.append(letter)

    return ''.join(final_text)


# Ask for the initial text from the user
text = input("Enter the text you want to encrypt/decrypt: ")

# Perform ROT13 cipher on the text
result = rot13_cipher(text)

# Output the result
print("The text has been converted:")
print(result)
