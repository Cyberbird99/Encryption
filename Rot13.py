"""ROT13 cipher(read as (“rotate by 13 places”) is a special case of the Ceaser cipher 
in which the shift is always 13. 
So every letter is shifted 13 places to encrypt or to decrypt the message. """

# We can ask the user to enter a text 
# and encrypt it using ROT13    

# Ask for the initial text 
text = input("Put in the text you want to encrypt/decrypt.")
# Change the text to lower-case 
text = text.lower()
final_text = ""

# Let it loop through each letter in the text
# And change each letter into ASCII equivalent
# Check to see if it is an alphabetic character
# If not, skip
for letter in text:
    ascii_num = ord(letter)
    
    if ascii_num >= 97 and ascii_num <= 122:
        # Add 13 to ascii_num to "shift" it by 13
        # Confirm new character will be alphabetic
        ascii = ascii_num + 13
        
        if ascii > 122:
            # if not, wrap around
            ascii = ascii - 26
        final_text = final_text + chr(ascii)
    else:
        final_text = final_text + chr(ascii_num)

# Print converted text
print("The text has been converted")
print(final_text)
