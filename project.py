import random, string

def generate_password(length=12):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%^&*"

    all_chars = upper + lower + digits + symbols

    # Ensure password has at least one of each type
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill remaining length
    password += [random.choice(all_chars) for _ in range(length - 4)]
    random.shuffle(password)

    return "".join(password)

# Driver code
length = int(input("Enter password length: "))
print("Generated Password:", generate_password(length))
