import random
import string

def generate_password(length):
   """Generate a random password of length characters."""
   characters = string.ascii_letters + string.digits + string.punctuation
   password = ''.join(random.choice(characters) for i in range(length))
   return password
if __name__ == "__main__":
    try:
        length = int(input("Enter the length of the password: "))
        if length < 4:
            print("Password length should be at least 4.")
        elif length > 12:
            print("Password length should be less than 12 characters.")
        else:
            print("Generated password:", generate_password(length))
    except ValueError:
        print("Please enter a valid number.")
   
   