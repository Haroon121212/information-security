# Caesar Cipher Program

print("Welcome to Caesar Cipher")

# Encryption function
def caesar_encrypt(text, shift):
    encrypted_text = ''  # Stores encrypted result
    
    for ch in text:  # Loop through each character
        if ch in lower_letters:
            encrypted_text += lower_letters[(lower_letters.index(ch) + shift) % 26]
        elif ch in upper_letters:
            encrypted_text += upper_letters[(upper_letters.index(ch) + shift) % 26]
        else:
            encrypted_text += ch  # Keep spaces and symbols unchanged

    return encrypted_text  # Return encrypted text


# Decryption function
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ''  # Stores decrypted result
    
    for ch in ciphertext:
        if ch in lower_letters:
            decrypted_text += lower_letters[(lower_letters.index(ch) - shift) % 26]
        elif ch in upper_letters:
            decrypted_text += upper_letters[(upper_letters.index(ch) - shift) % 26]
        else:
            decrypted_text += ch

    return decrypted_text  # Return decrypted text


# Alphabet keys
lower_letters = 'abcdefghijklmnopqrstuvwxyz'
upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# Main Program (Taking input from user)
message = input("Enter your message: ")
shift_value = int(input("Enter shift value: "))

encrypted = caesar_encrypt(message, shift_value)
print("Encrypted Text:", encrypted)

decrypted = caesar_decrypt(encrypted, shift_value)
print("Decrypted Text:", decrypted)