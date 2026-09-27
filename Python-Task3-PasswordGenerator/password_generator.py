import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = ''.join(random.choice(characters) for _ in range(length))

        has_letter = any(char.isalpha() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_special = any(char in string.punctuation for char in password)

        types = sum([has_letter, has_digit, has_special])

        if types >= 2:
            return password


print("Random Password Generator")

while True:
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8.")
            continue

        password = generate_password(length)

        print("Generated Password:", password)

        again = input("Generate another password? (yes/no): ").lower()

        if again != "yes":
            print("Thank you!")
            break

    except ValueError:
        print("Please enter a valid number.")