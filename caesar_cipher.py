def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def brute_force_decrypt(text):
    print("\n🔍 Brute Force Results:")
    for shift in range(1, 26):
        decrypted = caesar_decrypt(text, shift)
        print(f"Shift {shift:2}: {decrypted}")

def menu():
    while True:
        print("\n=== Caesar Cipher Tool ===")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Brute-force decrypt")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            msg = input("Enter your message: ")
            shift = get_shift()
            encrypted = caesar_encrypt(msg, shift)
            print(f"\n🔐 Encrypted message: {encrypted}")

        elif choice == '2':
            msg = input("Enter your message: ")
            shift = get_shift()
            decrypted = caesar_decrypt(msg, shift)
            print(f"\n🔓 Decrypted message: {decrypted}")

        elif choice == '3':
            msg = input("Enter the encrypted message: ")
            brute_force_decrypt(msg)

        elif choice == '4':
            print("Goodbye! 👋")
            break

        else:
            print("⚠️ Invalid choice. Please try again.")

def get_shift():
    while True:
        try:
            return int(input("Enter shift value (0-25): "))
        except ValueError:
            print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    menu()
