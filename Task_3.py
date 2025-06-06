import random
import string

def generate_password(length, use_digits=True, use_special=True):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    # Build character pool based on user's choice
    char_pool = letters
    if use_digits:
        char_pool += digits
    if use_special:
        char_pool += special_chars

    # Ensure the pool isn't empty
    if not char_pool:
        return "Error: No characters selected for password generation."

    # Generate password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("🔐 Password Generator 🔐")
    
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_digits, use_special)
    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
