def caesar_cipher_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - start + shift) % 26 + start
            result += chr(shifted)
        else:
            result += char  
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)  # reverse shift for decryption

def main():
    print("Caesar Cipher Program")
    choice = input("Do you want to encrypt or decrypt? (e/d): ").strip().lower()
    
    if choice not in ['e', 'd']:
        print("Invalid choice.")
        return
    
    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (integer): "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return

    if choice == 'e':
        encrypted = caesar_cipher_encrypt(message, shift)
        print("Encrypted message:", encrypted)
    else:
        decrypted = caesar_cipher_decrypt(message, shift)
        print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()
