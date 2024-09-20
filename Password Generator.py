import random
import string

def generate_password(length):
    """Generate a random password of specified length."""
    # Define the character sets to use for the password
    lowercase = string.ascii_lowercase  # a-z
    uppercase = string.ascii_uppercase  # A-Z
    digits = string.digits              # 0-9
    punctuation = string.punctuation     # Special characters

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + punctuation

    # Generate a random password using the combined character set
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    """Run the password generator application."""
    print("Welcome to the Password Generator!")
    
    # Prompt user for the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 8 characters): "))
            if length < 8:
                print("Password length should be at least 8 characters. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

    # Generate and display the password
    generated_password = generate_password(length)
    print(f"\nGenerated Password: {generated_password}")

if __name__ == "__main__":
    main()