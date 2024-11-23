Encryption is a method of data security that converts data from a readable format into an encoded format that can only be read or processed after it has been decrypted using a cryptographic key. It’s a common process in cryptography that encodes a message or information so that only authorized parties can access it and those who are not authorized cannot.

Encryption is essential to cybersecurity and data protection, as it protects private information and sensitive data and enhances the security of communication between client apps and servers. Encryption is critical to every organization because it protects confidential data by converting it into ciphertext.
This Python code implements the ROT13 cipher, a simple encryption and decryption method that shifts each letter of the text by 13 positions in the alphabet. It is often used as a lightweight way to obscure text, as applying ROT13 twice (once to encrypt and once to decrypt) returns the original text.

Step-by-Step Breakdown of the Code:
Introduction and User Input: The code starts by asking the user to input a text string that they want to either encrypt or decrypt using the ROT13 cipher.

Text Conversion to Lowercase: After the input is received, the text is converted to lowercase. This is done to ensure that the cipher works uniformly with both uppercase and lowercase letters.

Initialization of Variables: The variable final_text is initialized as an empty string, which will hold the final result (the encrypted or decrypted text).

Loop Through Each Letter: The code then enters a loop to iterate through each letter in the text. For each letter, the following steps are performed:

Convert Letter to ASCII: The ASCII value of the current letter is obtained using the ord() function. This function converts a character into its corresponding ASCII (or Unicode) number.

Check if the Character is Alphabetic: The code checks whether the current character is a lowercase alphabetic letter by verifying if its ASCII value is between 97 ('a') and 122 ('z').

Shift the ASCII Value by 13: If the character is alphabetic, it shifts the ASCII value by 13 places to encrypt or decrypt it. For example, 'a' (ASCII 97) becomes 'n' (ASCII 110), and 'z' (ASCII 122) wraps around to 'm' (ASCII 109).

Handle Wrapping Around the Alphabet: If the new shifted ASCII value exceeds 122 (i.e., it goes past 'z'), the code ensures the letter wraps around by subtracting 26 from the ASCII value, which shifts it back into the valid range for lowercase letters.

Construct the Final Text: After applying the shift, the code converts the new ASCII value back to a character using the chr() function and appends it to the final_text string. If the character was not alphabetic, it simply appends the original character.

Output the Result: After the loop finishes, the code prints the final encrypted or decrypted text to the user.
