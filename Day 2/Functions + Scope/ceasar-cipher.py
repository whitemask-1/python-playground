def caesar_cipher(text, shift, encrypt=True):
    if not isinstance(shift, int):
        return "Shift value must be an integer."
    elif shift < 0 or shift > 25:
        return "Shift value must be between 0 and 25."
    if not encrypt:
        shift = -shift
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    return text.translate(translation_table)

def encrypt(text, shift):
    return caesar_cipher(text, shift)
def decrypt(text, shift):
    return caesar_cipher(text, shift, encrypt=False)

encrypted_text = encrypt("fifty five on a chanel jacket", 3)
decrypted_text = decrypt(encrypted_text, 3)
print(encrypted_text)
print(decrypted_text)

