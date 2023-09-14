import random
import string

def generate_password(length=12):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting 'length' characters from 'characters'
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

if __name__ == "__main__":
    # You can specify the length of the password as an argument to generate_password()
    password_length = int(input("Enter the desired password length: "))
    password = generate_password(password_length)
    print("Generated Password:", password)
