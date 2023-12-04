def handle_decrypt(message, key):
    encrypted = []
    for char in message:
        if char.isalpha():
            shift = 65 if char.isupper() else 97  # ASCII value of 'A' or 'a'
            encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted_char = char
        encrypted.append(encrypted_char)
    return ''.join(encrypted)

def decrypt(encrypted, key):
    return handle_decrypt(encrypted, -key)