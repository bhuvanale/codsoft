import random

def generate_password(length):
    # Define the character set: uppercase, lowercase, digits, and a few special characters
    char_set = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    
    # Generate a random password using the character set
    password = ''.join(random.choice(char_set) for _ in range(length))
    
    return password

def main():
    # Prompt the user to enter the desired length of the password
    length = int(input("Enter the desired length for the password: "))
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
